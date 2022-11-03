#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='db_automation',
      version='0.0.1',
      description='for scraping ffiec data',
      author='jacob danner',
      author_email='jacob.danner@drake.edu',
      packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
      license='LICENSE.txt',
    )
