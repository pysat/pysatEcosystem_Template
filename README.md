<div align="left">
        <img height="0" width="0px">
        <img width="20%" src="https://raw.githubusercontent.com/pysat/pysatEcosystem_Template/main/docs/figures/pysatEcosystem_Template.png" alt="PACKAGENAME" title="PACKAGENAME" </img>
</div>

# PACKAGENAME: pysat support for THIS TYPE OF DATA OR ANALYSIS
[![Pytest with Flake8](https://github.com/pysat/pysatEcosystem_Template/actions/workflows/main.yml/badge.svg)](https://github.com/pysat/pysatEcosystem_Template/actions/workflows/main.yml)
[Coverage Status] (ADD COVERALLS LINK)
[DOI] (ADD ZENODO LINK) [Documentation] (ADD READTHEDOCS LINK)
[PyPI] version (ADD PYPI LINK)


This package DOES THIS THING.

# Installation

The following instructions provide a guide for installing PACKAGENAME and
give some examples on how to use the routines.

## Prerequisites

PACKAGENAME uses common Python modules, as well as modules developed by
and for the Space Physics community.  This module officially supports
Python 3.X+.

| Common modules | Community modules |
| -------------- | ----------------- |
| numpy          | pysat >= 3.0.4    |
| pandas         |                   |
| xarray         |                   |


## PyPi Installation
```
pip install PACKAGENAME
```

## GitHub Installation
```
git clone https://github.com/pysat/PACKAGENAME.git
```

Change directories into the repository folder and run the setup.py file.  For
a local install use the "--user" flag after "install".

```
cd PACKAGENAME/
python setup.py install
```

Note: pre-0.1.0 version
-----------------------
Only include this if PACKAGENAME is currently in an alpha development phase.  Feedback and
contributions are appreciated.

# Examples

The instrument modules are portable and designed to be run like any pysat
instrument.

```
import pysat
import PACKAGENAME
inst = pysat.Instrument(inst_module=PACKAGENAME.instruments.EX_INST)
```

Another way to use the instruments in an external repository is to register the
instruments.  This only needs to be done the first time you load an instrument.
Afterward, pysat will identify them using the `platform` and `name` keywords.

```
pysat.utils.registry.register('PACKAGENAME.instruments.EX_INST')
inst = pysat.Instrument('EX', 'INST')
```

The package include analysis tools as well.  Detailed examples are in the documentation (LINK TO READTHEDOCS).
