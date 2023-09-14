This repository provides a template for creating a pysat Ecosystem package. The
files within are all examples for the GitHub community standards, continuous
integration, PyPi support, documentation, and basic installation documents
needed for a pysat Ecosystem package. Adhering to these standards is not
required, but will assist in package maintenance.

In all of these documents, PACKAGENAME is used in place of the pysat Ecosystem
package name. Please proof read each document carefully before applying it and
consider submitting changes and improvements to these templates as Issues or
Pull Requests to this repository.

Contents
========

Community Documents
-------------------

* README.md
* CODE_OF_CONDUCT.md
* CONTRIBUTING.md
* LICENSE
* .gitignore
* .github/pull_request_template.md
* .github/ISSUE_TEMPLATE/bug_report.md
* .github/ISSUE_TEMPLATE/feature_request.md
* .github/ISSUE_TEMPLATE/question.md

Continuous Integration
----------------------

* .github/workflows/docs.yml
* .github/workflows/main.yml
* .github/workflows/pip_rc_install.yml
* .github/workflows/pysat_rc.yml

Documentation
-------------

* .readthedocs.yml
* docs/Makefile
* docs/conf.py
* docs/figures/packagename_logo.jpg

Installation/Python Basics
--------------------------

* MANIFEST.in
* pyproject.toml
* requirements.txt
* setup.cfg
* test_requirements.txt
* PACKAGENAME/__init__.py

Release Support
---------------

* .zenodo.json
