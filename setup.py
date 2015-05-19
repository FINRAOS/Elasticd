#!/usr/bin/python

from imp import load_source
from distutils.core import setup

core = load_source("core", "elasticd/__init__.py")

setup(
    name=core.__app_name__,
    version=core.__version__,
    license="Apache",
    description="""This utility allows frontends to communicate with
                backends using IP addresses in dynamic cloud environments.""",
    author=core.__author__,
    author_email=core.__email__,
    maintainer=core.__author__,
    maintainer_email=core.__email__,
    platforms=["Linux"],
    url="http://github.com/finros/elasticd",
    download_url="http://github.com/finraos/elasticd",
    packages=["elasticd"]
)
