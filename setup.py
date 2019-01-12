# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='python-fritz-office-365-sync',
    version='0.1.0',
    description='A python script to control fritzbox thermostats by office365 calendar',
    long_description=readme,
    author='Yannik Korzikowski',
    author_email='yannik@korzikowski.de',
    url='https://github.com/ykorzikowski/python-fritz-office-365-sync',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

