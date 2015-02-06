#!/usr/bin/env python

# This snippet is in public domain
# https://gist.github.com/techtonik/4066623/

def get_version(relpath):
    """Read version info from a file without importing it"""
    from os.path import dirname, join

    # Allow to use function interactively
    if '__file__' not in globals():
        root = '.'
    else:
        root = dirname(__file__)

    # The code below reads text file with unknown encoding in
    # in Python2/3 compatible way. Reading this text file
    # without specifying encoding will fail in Python 3 on some
    # systems (see http://goo.gl/5XmOH). Specifying encoding as
    # open() parameter is incompatible with Python 2

    # cp437 is the encoding without missing points, safe against:
    #   UnicodeDecodeError: 'charmap' codec can't decode byte ...

    for line in open(join(root, relpath), 'rb'):
        line = line.decode('cp437')
        if '__version__' in line:
            if '"' in line:
                # __version__ = "0.9"
                return line.split('"')[1]
            elif "'" in line:
                return line.split("'")[1]


def get_description(relpath):
    from os.path import dirname, join
    text = open(join(dirname(__file__), 'README.txt'), 'rb').read()
    return text.decode('utf-8')


# --- distutils config

import os
import textwrap
import zipfile
from distutils.core import setup

# Distutils 'API' to ship test data along with hexdump.py
# http://stackoverflow.com/questions/1612733/including-non-python-files-with-setup-py
from distutils.command.install import INSTALL_SCHEMES
for scheme in INSTALL_SCHEMES.values():
  scheme['data'] = scheme['purelib']

# Override sdist to always produce .zip archive (initialize_options)
# and make the .zip file executable (run method)
# https://docs.python.org/2/distutils/extending.html
# https://docs.python.org/2/distutils/apiref.html#creating-a-new-distutils-command
from distutils.command.sdist import sdist as _sdist
class sdistzip(_sdist):
    mainpy_tpl = textwrap.dedent("""\
        import os
        import sys

        # add .zip/package to python lookup path
        zippath = os.path.dirname(__file__)
        imppath = os.path.join(zippath, '{importdir}')
        sys.path.insert(0, imppath)

        import {modname}
        sys.exit({modname}.main())
        """)
    def initialize_options(self):
        _sdist.initialize_options(self)
        self.formats = 'zip'
    def run(self):
        _sdist.run(self)
        for archive in self.archive_files:
            if archive.endswith('.zip'):
                self.make_executable(archive)
    def make_executable(self, archive):
        zf = zipfile.ZipFile(archive, 'a', zipfile.ZIP_DEFLATED)
        tplvars = dict(
            modname = self.distribution.get_name(),
            importdir = self.distribution.get_fullname())
        text = self.mainpy_tpl.format(**tplvars)
        zf.writestr('__main__.py', text)
        zf.close()

# /-- distutils config

setup(
    name='hexdump',
    version=get_version('hexdump.py'),
    author='anatoly techtonik <techtonik@gmail.com>',
    url='https://bitbucket.org/techtonik/hexdump/',

    description="view/edit your binary with any text editor",
    license="Public Domain",
    classifiers=[
        #'Environment :: Console',
        'License :: Public Domain',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries :: Python Modules',
        #'Topic :: Utilities',
    ],

    py_modules=['hexdump'],
    data_files=[('', ['hexfile.bin'])],

    long_description=get_description('README.txt'),

    cmdclass={'sdist': sdistzip},
)
