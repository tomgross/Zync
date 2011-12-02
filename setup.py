#!/usr/bin/env python

from setuptools import setup, find_packages

long_description = '\n\n'.join([
   open('README.txt').read().strip(),
   open('CHANGES.txt').read().strip()])

setup(
    name="zync",
    license="ZPL 2.1",
    version="1.0dev",
    description="A GUI for syncing ZODBs",
    author="Tom Gross",
    author_email="itconsense@gmail.com",
    url="http://github.com/tomgross/zync",
    packages=find_packages(),
    long_description=long_description,
    zip_safe=True,
    install_requires=[
        'fabric',
#        'PyQt'
    ],
    test_suite = 'zync.tests.test_suite',
    entry_points={
        'console_scripts': [
            'zync = zync:main']},
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 2.5",
        "Environment :: Console",
        "Environment :: X11 Applications :: Qt",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: Zope Public License",
        "Programming Language :: Python",
        "Topic :: System :: Systems Administration",
        "Topic :: Utilities",
        ])

