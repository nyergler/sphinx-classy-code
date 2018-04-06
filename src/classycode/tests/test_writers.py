import tempfile
from unittest import TestCase

from sphinx.builders.html import StandaloneHTMLBuilder
from sphinx_testing import with_app

from classycode.tests.util import (
    TestApp,
    test_root,
)

import classycode.formatter


class MonkeyPatchTests(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.app = TestApp(buildername='html')
        cls.builder = StandaloneHTMLBuilder(cls.app)

    @classmethod
    def tearDownClass(cls):
        cls.app.cleanup()

    def test_our_formatter_used(self):
        import sphinx.highlighting

        self.assertEqual(
            sphinx.highlighting.PygmentsBridge.html_formatter,
            classycode.formatter.HtmlFormatter,
        )


class SphinxOutputTests(TestCase):

    @with_app(srcdir=test_root)
    def test_output(self, sphinx_app, *args):

        sphinx_app.build()

        with open(sphinx_app.builddir/'html'/'index.html') as html_file:
            html = html_file.read()

            self.assertIn('<span class="one">1\n</span>', html)
            self.assertIn('<span class="two-three">2\n</span>', html)
            self.assertIn('<span class="two-three">3\n</span>', html)
            self.assertIn('</span>4\n</pre>', html)
