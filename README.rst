==================
Sphinx Classy Code
==================

.. image:: https://travis-ci.org/nyergler/sphinx-classy-code.png?branch=master
   :target: https://travis-ci.org/nyergler/sphinx-classy-code

.. image:: https://coveralls.io/repos/nyergler/sphinx-classy-code/badge.png
  :target: https://coveralls.io/r/nyergler/sphinx-classy-code


Drop-in replacements for Sphinx_\ ' ``code-block`` and
``literalinclude`` directives. In addition to specifying
`emphasize-lines`_, you can specify arbitrary classes to add on a
per-line basis.

For example::

  .. code-block:: python
     :line-classes: 1(python-def)

     def stay(classy):
         pass

Will wrap the function declaration in ``<span
class="python-def">...</span>``.

Valid line + class specifiers include:

* ``1(classname)``

  Apply ``classname`` to line 1.

* ``1-5(classname)``

  Apply ``classname`` to lines 1 through 5.

* ``2-(classname)``

  Apply ``classname`` to line 2 *and all subsequent lines*
  (``codeblock`` only).

You can separate multiple specifiers with a comma.

You can use both ``line-classes`` and ``emphasize-lines`` in the same
block.

Installation
============

To install, simply install the package::

  $ pip install sphinx-classy-code

Then add it to the list of Sphinx extensions in your ``conf.py``::

  extensions = ['classycode']

License
=======

**sphinx-classy-code** is made available under a BSD license; see
LICENSE for details.


.. _Sphinx: http://sphinx-doc.org/
.. _`emphasize-lines`: http://sphinx-doc.org/markup/code.html?highlight=literalinclude#line-numbers
