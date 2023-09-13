"""Core library for PACKAGENAME.

DESCRIPTION.

"""

try:
    from importlib import metadata
except ImportError:
    import importlib_metadata as metadata

from PACKAGENAME import instruments  # noqa F401

__version__ = metadata.version('PACKAGENAME')
