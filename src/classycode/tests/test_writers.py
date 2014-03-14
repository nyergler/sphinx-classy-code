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
