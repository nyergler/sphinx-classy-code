import sphinx.highlighting
import classycode.directives

from . import formatter


def setup(app):

    app.add_directive('code-block', classycode.directives.CodeBlock)

    sphinx.highlighting.PygmentsBridge.html_formatter = \
        formatter.HtmlFormatter
