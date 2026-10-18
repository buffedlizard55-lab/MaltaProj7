"""Offline regression tests; temporary fixtures never modify published pages."""
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import verify


class LocalLinkTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.page = self.root / 'index.html'
        self.page.write_text('')
        verify.ERRORS.clear()
        self.addCleanup(verify.ERRORS.clear)
        self.patch = patch.object(verify, 'ROOT', self.root)
        self.patch.start()
        self.addCleanup(self.patch.stop)

    def check(self, text):
        self.page.write_text(text)
        verify.check_internal_links(self.page, text)
        return verify.ERRORS

    def test_valid_same_page_fragment(self):
        self.assertEqual(self.check('<h2 id="free-events"></h2><a href="#free-events">Go</a>'), [])

    def test_missing_same_page_fragment(self):
        self.assertIn('broken local fragment', self.check('<a href="#missing">Go</a>')[0])

    def test_cross_page_encoded_fragment(self):
        (self.root / 'other.html').write_text("<h2 id='free events'>Events</h2>")
        self.assertEqual(self.check('<a href="other.html#free%20events">Go</a>'), [])

    def test_missing_cross_page_fragment(self):
        (self.root / 'other.html').write_text('<h2 id="actual">Events</h2>')
        self.assertIn('broken local fragment', self.check('<a href="other.html#missing">Go</a>')[0])

    def test_missing_file(self):
        self.assertIn('broken local link', self.check('<a href="missing.html">Go</a>')[0])

    def test_directory_index(self):
        (self.root / 'category').mkdir()
        (self.root / 'category' / 'index.html').write_text('<h2 id="music">Music</h2>')
        self.assertEqual(self.check('<a href="category/#music">Go</a>'), [])

    def test_directory_without_index(self):
        (self.root / 'category').mkdir()
        self.assertIn('no index.html', self.check('<a href="category/">Go</a>')[0])

    def test_escape(self):
        self.assertIn('escapes repository', self.check('<a href="../private">Go</a>')[0])

    def test_external_link_not_fetched(self):
        self.assertEqual(self.check('<a href="https://example.org/#unvalidated">Go</a>'), [])

    def test_duplicate_id(self):
        self.assertIn('duplicate HTML id', self.check('<h2 id="x"></h2><h3 id="x"></h3>')[0])

    def test_missing_accessibility_label(self):
        self.assertIn('missing id', self.check('<section aria-labelledby="missing"></section>')[0])


if __name__ == '__main__':
    unittest.main()
