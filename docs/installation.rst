.. _install:

Installation
============

The following instructions will allow you to install PACKAGE


.. _install-prereq:

Prerequisites
-------------

.. image:: figures/poweredbypysat.png
    :width: 150px
    :align: right
    :alt: powered by pysat Logo, blue planet with orbiting python


PACKAGE uses common Python modules, as well as modules developed by
and for the Space Physics community.  This module officially supports
Python 3.6+.

 ============== =================
 Common modules Community modules
 ============== =================
  numpy         pysat >= 3.1.0
  pandas
  xarray
 ============== =================


.. _install-opt:


Installation Options
--------------------


.. _install-opt-pip:

PyPi
^^^^
All official pysatSpaceWeather releases are `available <link>`_ through the
PyPi package manager.
::


   pip install PACKAGENAME



.. _install-opt-git:

GitHub
^^^^^^
You can keep up to date with the latest changes at the GitHub repository.

1. Clone the git repository
::


   git clone https://github.com/PACKAGE_REPOSITORY


2. Install PACKAGENAME:
   Change directories into the repository folder and run the setup.py file.
   There are a few ways you can do this:

   A. Install on the system (will install locally without root privileges)::


        python -m build
	pip install .

   B. Install with the intent to develop locally::


        python -m build
	pip install -e .
