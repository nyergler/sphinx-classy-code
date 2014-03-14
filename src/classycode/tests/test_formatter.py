from unittest import TestCase

import classycode.formatter


class HtmlFormatterTests(TestCase):

    def test_highlight_lines(self):

        formatter = classycode.formatter.HtmlFormatter(
            hl_lines={
                1: 'hll',
                2: 'hll',
            },
        )

        self.assertEqual(
            list(
                formatter._highlight_lines(
                    [
                        (1, 'one'),
                        (1, 'two'),
                        (1, 'three'),
                    ],
                ),
            ),
            [
                (1, '<span class="hll">one</span>'),
                (1, '<span class="hll">two</span>'),
                (1, 'three'),
            ],
        )

    def test_different_line_classes(self):

        formatter = classycode.formatter.HtmlFormatter(
            hl_lines={
                1: 'one',
                2: 'two',
            },
        )

        self.assertEqual(
            list(
                formatter._highlight_lines(
                    [
                        (1, 'one'),
                        (1, 'two'),
                        (1, 'three'),
                    ],
                ),
            ),
            [
                (1, '<span class="one">one</span>'),
                (1, '<span class="two">two</span>'),
                (1, 'three'),
            ],
        )

    def test_keys_cast_to_ints(self):

        formatter = classycode.formatter.HtmlFormatter(
            hl_lines={
                '1': 'hll',
            },
        )
        self.assertEqual(formatter.hl_lines, {1: 'hll'})

    def test_non_int_key_ignored(self):

        formatter = classycode.formatter.HtmlFormatter(
            hl_lines={
                'a': 'hll',
            },
        )
        self.assertEqual(formatter.hl_lines, {})
