==================
Sphinx Classy Code
==================

Drop-in replacements for Sphinx_\ ' code example directives. In
addition to specifying `emphasize-lines`_, you can specify arbitrary
classes to add on a per-line basis.

For example::

  .. code-block:: python
     :line-classes: 1(def)

     def stay(classy):
         pass

Will wrap the function declaration in ``<span
class="def">...</span>``.

Valid line + class specifiers include:

* ``1(classname)``
* ``1-5(classname)``

You can separate multiple specifiers with a comma.
