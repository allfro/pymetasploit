#!/usr/bin/env python

from setuptools import setup, find_packages
from os import path

def read(fname):
    return open(path.join(path.dirname(__file__), fname)).read()

setup(
    name='pymetasploit',
    author='Nadeem Douba',
    version='2.0',
    author_email='ndouba@gmail.com',
    description='A full-fledged msfrpc library for Metasploit framework.',
    license='GPL',
    packages=find_packages('src'),
    package_dir={ '' : 'src' },
    scripts=[
        'src/scripts/pymsfconsole',
        'src/scripts/pymsfrpc'
    ],
    install_requires=[
        'msgpack-python>=0.1.12'
    ],
    url='https://github.com/allfro/pymetasploit',
    download_url='https://github.com/allfro/pymetasploit/zipball/master',
    long_description=read('README')
)
