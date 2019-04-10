=====
Usage
=====

To use acs_download in a project::

.. code:: python

   import acs_download as acs

   acs.get_data(
       year = 2017,
       state = 'California',
       download_path = '../data/raw/',
       extract = True,
       extract_path = '../data/interim/',
   )

