#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=6.0', 'us>=1.0', 'tqdm>=4.31', 'requests>=2.21']

setup_requirements = ['Click>=6.0', 'us>=1.0', 'tqdm>=4.31', 'requests>=2.21']

test_requirements = ['Click>=6.0', 'us>=1.0', 'tqdm>=4.31', 'requests>=2.21']

setup(
    author="Sergio Sánchez Zavala",
    author_email='sergio@cimarron.io',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    description="Download American Community Survey (ACS) complete Public Use Micro Sample (PUMS) data files from census FTP server.",
    entry_points={
        'console_scripts': [
            'acs_download=acs_download.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='acs_download',
    name='acs_download',
    packages=find_packages(include=['acs_download']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/chekos/acs_download',
    version='0.1.5',
    zip_safe=False,
)
