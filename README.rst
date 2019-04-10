============
acs_download
============


.. image:: https://img.shields.io/pypi/v/acs_download.svg
        :target: https://pypi.python.org/pypi/acs_download

.. image:: https://img.shields.io/travis/chekos/acs_download.svg
        :target: https://travis-ci.org/chekos/acs_download

.. image:: https://readthedocs.org/projects/acs-download/badge/?version=latest
        :target: https://acs-download.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status




Download American Community Survey (ACS) complete Public Use Micro Sample (PUMS) data files from census FTP server.


* Free software: MIT license
* Documentation: https://acs-download.readthedocs.io.

Usage
-----

.. code:: python

   import acs_download

   acs_download(
       year = 2017,
       state = 'California',
       download_path = '../data/raw/',
       extract = True,
       extract_path = '../data/interim/',
   )

This will download ACS PUMS data file of California to your
``../data/raw/`` folder and extract it to ``../data/interim/`` folder.

``acs_download`` uses pypi package ``us``, which uses ``jellyfish``, to
handle ``state`` input so you can use variations

Features
--------

* TODO

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
