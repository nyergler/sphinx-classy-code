import re

from docutils.parsers.rst import directives
import sphinx.directives.code


LINECLASS_RE = re.compile(r'((?P<start>\d+)(?P<range>-(?P<end>\d+)?)?)\((?P<class>[a-z0-9-]+)\)')


def parselinenos(spec, nlines=None):
    """Parse a line class spec into a dict of line no: class name

    """

    items = {}
    parts = spec.split(',')

    for part in parts:
        line_class = LINECLASS_RE.match(part)
        start = int(line_class.group('start'))

        if line_class.group('range'):
            if line_class.group('end'):
                end = int(line_class.group('end'))
            else:
                end = nlines

            for line_no in range(start, end + 1):
                items[line_no] = line_class.group('class')

        else:
            items[start] = line_class.group('class')

    return items


class LineClassesSupportMixin(object):
    """Mixin class that adds the line-classes to Sphinx code directives."""

    option_spec = {
        'linenos': directives.flag,
        'emphasize-lines': directives.unchanged_required,
        'line-classes': directives.unchanged_required,
    }

    def _get_line_count(self):
        """Return the line count for this directive's content."""

        return len(self.content)

    def run(self):

        result = super(LineClassesSupportMixin, self).run()
        hl_lines = result[0].get('highlight_args', {}).get('hl_lines', {})

        if self.options.get('emphasize-lines') and hl_lines:

            # convert emphasize-lines params to line-class dict
            hl_lines = dict(
                [
                    (line, 'hll')
                    for line in result[0]['highlight_args']['hl_lines']
                 ]
            )

        if self.options.get('line-classes'):
            line_classes = parselinenos(
                self.options['line-classes'],
                nlines=self._get_line_count(),
            )
            for line in line_classes:
                if line in hl_lines:
                    hl_lines[line] = '%s %s' % (hl_lines[line], line_classes[line])
                else:
                    hl_lines[line] = line_classes[line]

        result[0].setdefault('highlight_args', {})['hl_lines'] = hl_lines

        return result


class CodeBlock(LineClassesSupportMixin, sphinx.directives.code.CodeBlock):
    """CodeBlock directive with support for custom classes applied to lines.

    """


class LiteralInclude(LineClassesSupportMixin,
                     sphinx.directives.code.LiteralInclude):
    """LiteralInclude directive with support for custom classes on lines.

    """

    option_spec = {
        'linenos': directives.flag,
        'tab-width': int,
        'language': directives.unchanged_required,
        'encoding': directives.encoding,
        'pyobject': directives.unchanged_required,
        'lines': directives.unchanged_required,
        'start-after': directives.unchanged_required,
        'end-before': directives.unchanged_required,
        'prepend': directives.unchanged_required,
        'append': directives.unchanged_required,
        'emphasize-lines': directives.unchanged_required,
        'line-classes': directives.unchanged_required,
    }
