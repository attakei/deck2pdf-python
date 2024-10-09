=================================================
deck2pdf: Convert HTML presentation into PDF file
=================================================

.. image:: https://img.shields.io/pypi/v/deck2pdf.svg
   :target: https://pypi.python.org/pypi/deck2pdf
   :alt: PyPI latest

.. image:: https://img.shields.io/circleci/project/attakei/deck2pdf-python.svg
   :target: https://circleci.com/gh/attakei/deck2pdf-python
   :alt: CircleCI Status (not all tests)

.. image:: https://img.shields.io/codeclimate/github/attakei/deck2pdf-python.svg
   :target: https://codeclimate.com/github/attakei/deck2pdf-python
   :alt: CodeClimate GPA

deck2pdf is converter from your html slide into PDF format keeping slide layout.

Use as CLI only
===============

.. code:: console

   pipx run deck2pdf https://slides.attakei.net/pyconjp-2022/ output.pdf

.. code:: console

   uvx deck2pdf https://slides.attakei.net/pyconjp-2022/ output.pdf

Getting started
===============

Installation
------------

.. code:: console

   pip install deck2pdf

Use as CLI
----------

.. code:: console

   deck2pdf https://slides.attakei.net/pyconjp-2022/ output.pdf

Supporting presentation tools
=============================

* Reveal.js
* More generic types that forwards slide by SPACE key.

IMPORTANT
=========

It has very breaking changes of architecture.
This name is same from old version, , but not same about argument and behaviors.

Notes
=====

This is inspred from deck2pdf (Java library) and decktape (NPM CLI).
