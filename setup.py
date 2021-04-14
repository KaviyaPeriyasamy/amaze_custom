# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in amaze_custom/__init__.py
from amaze_custom import __version__ as version

setup(
	name='amaze_custom',
	version=version,
	description='Custom script for customer and supplier primary contact',
	author='vautodesk',
	author_email='vautodesk@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
