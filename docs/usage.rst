=====
Usage
=====

To use deck2pdf, you can do either approaches.

* Use as only CLI tool (isolated environment)
* Use as a library

As CLI tool
===========

You can use pipx, uvx and more to run this as CLI.

.. code-block:: console
   :caption: Run by pipx

   pipx run deck2pdf URL OUTPUT

.. code-block:: console
   :caption: Run by uvx (included with uv)

   uvx deck2pdf URL OUTPUT

If you want to know detail usage, run with ``--help`` argument.

As library
==========

If you want to use internal process of your application,
install as library from PyPI.

.. code-block:: console

   pip install deck2pdf
