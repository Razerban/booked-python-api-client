# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='booked_api_client',
    version='0.1.0',
    description='Booked Python API Client Library',
    long_description=readme,
    author='Ahmed Abdelkafi',
    author_email='abdelkafiahmed@yahoo.fr',
    url='',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

