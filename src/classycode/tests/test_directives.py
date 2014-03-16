from unittest import TestCase

from mock import patch
from docutils import nodes
from sphinx.builders.html import StandaloneHTMLBuilder

from classycode.tests.util import (
    make_document,
    with_sphinx,
    TestApp,
)
from classycode import directives


class ParseLineNosTests(TestCase):

    def test_parse_single_entry(self):

        self.assertEqual(
            directives.parselinenos('1(one)'),
            {1: 'one'},
        )

    def test_parse_range_entry(self):

        self.assertEqual(
            directives.parselinenos('1-2(one-two)'),
            {
                1: 'one-two',
                2: 'one-two',
            },
        )

    def test_parse_multiple_entries(self):

        self.assertEqual(
            directives.parselinenos('1(one),2-3(two-three)'),
            {
                1: 'one',
                2: 'two-three',
                3: 'two-three',
            },
        )


class CodeBlockTests(TestCase):

    def setUp(self):

        self.app = TestApp(buildername='html')

    def test_codeblock_processes_line_classes(self):

        document = make_document(
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
        codeblock = document.traverse(nodes.literal_block)[0]

        self.assertEqual(
            codeblock['highlight_args']['hl_lines'],
            {1: 'one',
             2: 'two-three',
             3: 'two-three',
            },
        )

    def test_codeblock_supports_emphasize_lines_functionality(self):

        document = make_document(
            'testing',
            """\
Title
-----

.. code-block:: none
   :emphasize-lines: 1-2

   1
   2
   3

Additional Text

""",
        )
        codeblock = document.traverse(nodes.literal_block)[0]

        self.assertEqual(
            codeblock['highlight_args']['hl_lines'],
            {1: 'hll',
             2: 'hll',
            },
        )

    def test_mix_emphasize_lines_and_classes(self):

        document = make_document(
            'testing',
            """\
Title
-----

.. code-block:: none
   :emphasize-lines: 1
   :line-classes: 2(two)

   1
   2
   3

Additional Text

""",
        )
        codeblock = document.traverse(nodes.literal_block)[0]

        self.assertEqual(
            codeblock['highlight_args']['hl_lines'],
            {1: 'hll',
             2: 'two',
            },
        )

class LiteralIncludeTests(TestCase):

    def setUp(self):

        self.app = TestApp(buildername='html')

    def test_codeblock_processes_line_classes(self):

        with patch.object(self.app.env, 'note_dependency'):
            document = make_document(
                'testing',
                """\
Title
-----

.. literalinclude:: /test.py
   :line-classes: 1(one),2-3(two-three)

Additional Text

""",
                env=self.app.env,
            )

        include = document.traverse(nodes.literal_block)[0]

        self.assertEqual(
            include['highlight_args']['hl_lines'],
            {1: 'one',
             2: 'two-three',
             3: 'two-three',
            },
        )

    def test_codeblock_supports_emphasize_lines_functionality(self):

        with patch.object(self.app.env, 'note_dependency'):
            document = make_document(
                'testing',
                """\
Title
-----

.. literalinclude:: /test.py
   :emphasize-lines: 1-2

Additional Text

""",
                env=self.app.env,
            )

        codeblock = document.traverse(nodes.literal_block)[0]

        self.assertEqual(
            codeblock['highlight_args']['hl_lines'],
            {1: 'hll',
             2: 'hll',
            },
        )

    def test_mix_emphasize_lines_and_classes(self):

        with patch.object(self.app.env, 'note_dependency'):
            document = make_document(
                'testing',
                """\
Title
-----

.. literalinclude:: /test.py
   :emphasize-lines: 1
   :line-classes: 2(two)

Additional Text

""",
                env=self.app.env,
            )

        codeblock = document.traverse(nodes.literal_block)[0]

        self.assertEqual(
            codeblock['highlight_args']['hl_lines'],
            {1: 'hll',
             2: 'two',
            },
        )
