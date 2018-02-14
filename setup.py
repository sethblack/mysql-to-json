#!/usr/bin/env python3

from setuptools import setup
from distutils.command.install import install as _install

setup(
    name = 'mysql-to-json',
    version = '1.0.0',
    description = 'Connects to a MySQL database and exports selected data to JSON.',
    author = 'Seth Black',
    author_email = 'sblack@sethserver.com',
    url = 'https://github.com/sethblack/mysql-to-json',
    packages = ['mysqljson'],
    keywords = ['',],
    package_data={'mysql-to-json': ['templates/index.html']},
    include_package_data = True,
    install_requires = [
        'mysqlclient'
    ],
    entry_points = {
        'console_scripts' : [
            'mysql-to-json = mysqljson.__main__:main'
        ]
    },
    classifiers = [
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
    long_description = """\
MySQL to JSON
-----------
"""
)
