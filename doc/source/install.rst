.. _ref_install:

==================
Installation guide
==================

.. toctree::
   :maxdepth: 2


There are different ways to install the pyfeat package.



From the repository
===================

First step: get the repository!

Go to your shell and type

.. code-block:: bash

   git clone https://github.com/markovmodel/pyfeat.git

Then, install the package from source.


via pip
-------

Go to the repository's root directory and type

.. code-block:: bash

   pip install .


via setup
---------

Go to the repository's root directory and type:

.. code-block:: bash

   python setup.py install [--user]

For a development installation run:
   
.. code-block:: bash

   python setup.py develop --user --verbose



From the python package index
=============================

Go to your shell and type

.. code-block:: bash

   pip install pyfeat

or

.. code-block:: bash

   easy_install pyfeat
