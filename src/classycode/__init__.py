import classycode.directives


def setup(app):

    app.add_directive('code-block', classycode.directives.CodeBlock)
