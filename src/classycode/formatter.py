import pygments.formatters.html


class HtmlFormatter(pygments.formatters.html.HtmlFormatter):

    def __init__(self, **options):

        hl_lines = options.pop('hl_lines', None)
        super(HtmlFormatter, self).__init__(**options)

        self.hl_lines = {}
        if hl_lines:
            for line_no in hl_lines:
                try:
                    self.hl_lines[int(line_no)] = hl_lines[line_no]
                except ValueError:
                    pass

    def _highlight_lines(self, tokensource):
        """
        Highlighted the lines specified in the `hl_lines` option by
        post-processing the token stream coming from `_format_lines`.
        """
        hls = self.hl_lines

        for i, (t, value) in enumerate(tokensource):
            if t != 1:
                yield t, value
            if i + 1 in hls: # i + 1 because Python indexes start at 0
                if self.noclasses:
                    style = ''
                    if self.style.highlight_color is not None:
                        style = (' style="background-color: %s"' %
                                 (self.style.highlight_color,))
                    yield 1, '<span%s>%s</span>' % (style, value)
                else:
                    yield 1, '<span class="%s">%s</span>' % (
                        hls[i+1],
                        value,
                    )
            else:
                yield 1, value
