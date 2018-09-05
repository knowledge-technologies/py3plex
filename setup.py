
## Py3plex installation file. Cython code for fa2 is the courtesy of Bhargav Chippada.
## https://github.com/bhargavchippada/forceatlas2

from os import path
from setuptools import setup,find_packages
from setuptools.extension import Extension
import argparse


here = path.abspath(path.dirname(__file__))

# Get the long description from the README file


cythonopts = {"py_modules": ["py3plex/visualization/fa2.fa2util"]}
    
setup(name='py3plex',
      version='0.42',
      description="A Multilayer network analysis python3 library",
      url='http://github.com/skblaz/py3plex',
      author='Blaž Škrlj',
      author_email='blaz.skrlj@ijs.si',
      license='MIT',
      packages=find_packages(),
      zip_safe=False,
      install_requires=['rdflib','numpy','networkx','scipy'],
      include_package_data=True,
      **cythonopts)
