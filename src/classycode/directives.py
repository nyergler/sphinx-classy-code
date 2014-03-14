import re

from docutils.parsers.rst import directives
import sphinx.directives.code


LINECLASS_RE = re.compile(r'((?P<start>\d+)(-(?P<end>\d+))?)\((?P<class>[a-z0-9-]+)\)')


def parselinenos(spec):
    """Parse a line class spec into a dict of line no: class name

    """

    items = {}
    parts = spec.split(',')

    for part in parts:
        line_class = LINECLASS_RE.match(part)
        start = int(line_class.group('start'))

        if line_class.group('end'):
            for line_no in xrange(start, int(line_class.group('end')) + 1):
                items[line_no] = line_class.group('class')

        else:
            items[start] = line_class.group('class')

    return items


class CodeBlock(sphinx.directives.code.CodeBlock):

    option_spec = {
        'linenos': directives.flag,
        'emphasize-lines': directives.unchanged_required,
        'line-classes': directives.unchanged_required,
    }

    def run(self):

        result = super(CodeBlock, self).run()

        if self.options.get('line-classes'):
            result[0]['highlight_args'] = {
                'hl_lines': parselinenos(
                    self.options['line-classes'],
                ),
            }

        return result
