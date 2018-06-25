#!/usr/bin/env python
from distutils.core import setup
from setuptools import setup, find_packages

setup(
    name='RxFlask',
    version='0.0.1',
    description='RxPy x Flask',
    long_description='readme',
    author='TakenokoTech',
    author_email='takenoko.tech@gmail.com',
    url='https://github.com/nokotech/RxFlask',
    license=license,
    packages=find_packages(exclude=('test')),
    install_requires=['numpy'],
    test_suite='test'
)
