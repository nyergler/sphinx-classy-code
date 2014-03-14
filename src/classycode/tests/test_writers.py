from unittest import TestCase

from sphinx.builders.html import StandaloneHTMLBuilder

from classycode.tests.util import (
    make_document,
    with_sphinx,
    TestApp,
)

import classycode.formatter


class MonkeyPatchTests(TestCase):

    def setUp(self):

        self.app = TestApp(buildername='html')
        self.builder = StandaloneHTMLBuilder(self.app)

    def test_our_formatter_used(self):
        import sphinx.highlighting

        self.assertEqual(
            sphinx.highlighting.PygmentsBridge.html_formatter,
            classycode.formatter.HtmlFormatter,
        )


class SphinxOutputTests(TestCase):

    @with_sphinx()
    def test_output(self, sphinx_app):

        sphinx_app.build()

        with open(sphinx_app.builddir/'html'/'index.html') as html_file:
            html = html_file.read()

            self.assertIn('<span class="one">1\n</span>', html)
            self.assertIn('<span class="two-three">2\n</span>', html)
            self.assertIn('<span class="two-three">3\n</span>', html)
            self.assertIn('</span>4\n</pre>', html)
