from unittest import TestCase

from docutils import nodes
from sphinx.builders.html import StandaloneHTMLBuilder

from classycode.tests.util import (
    make_document,
    with_sphinx,
    TestApp,
)
from classycode import directives


class CodeBlockTests(TestCase):

    def setUp(self):

        self.app = TestApp(buildername='html')
        self.builder = StandaloneHTMLBuilder(self.app)
        self.document = make_document(
            'testing',
            """\
Title
-----

.. code-block:: none
   :line-classes: 1(one),2-3(two-three)

   1
   2
   3

Additional Text

""",
        )
        self.builder.init_templates()

    def test_codeblock_accepts_line_classes(self):

        codeblock = self.document.traverse(nodes.literal_block)[0]

        self.assertEqual(
            codeblock['highlight_args']['hl_lines'],
            {0: 'one',
             1: 'two-three',
             2: 'two-three',
            },
        )


class LineClassParseTests(TestCase):

    def test_parse_single_entry(self):

        self.assertEqual(
            directives.parselinenos('1(one)'),
            {0: 'one'},
        )

    def test_parse_range_entry(self):

        self.assertEqual(
            directives.parselinenos('1-2(one-two)'),
            {
                0: 'one-two',
                1: 'one-two',
            },
        )

    def test_parse_multiple_entries(self):

        self.assertEqual(
            directives.parselinenos('1(one),2-3(two-three)'),
            {
                0: 'one',
                1: 'two-three',
                2: 'two-three',
            },
        )
