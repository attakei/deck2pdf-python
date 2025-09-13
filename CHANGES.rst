===========
Change logs
===========

v0.9.0
======

:Date: 2025/09/13 (Asia/Tokyo)

Features
--------

* Add ``custom`` type of ``--format`` option.

v0.8.0
======

:Date: 2024-10-21 (JST)

Features
--------

* Support local filepath as target url.

v0.7.0
======

:Date: 2024-10-10 (JST)

Features
--------

* Add new options

  * ``--size`` is used to specify size of PDF.
  * ``--format`` is used to specify used presentation tool of html.

* CLI detect format if ``--format`` is not set.

Others
------

* Add repository url on PyPI.

v0.6.0
======

:date: 2024-10-09 (JST)

Regenerate for current usecases.

Breaking changes
----------------

* Drop all arguments and options of v0.5.
* Drop supporting for Python 2.x.

Features
--------

* Implement Chromium-based presentation reader.
* Decide size of pdf from viewport.
* Support Reveal.js (only it).
* Support Python 3.8 and over.
