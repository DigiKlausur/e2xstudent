#!/usr/bin/env python

import os
from setuptools import setup, find_packages

# get paths to all the extension files
extension_files = []
for (dirname, dirnames, filenames) in os.walk("e2xstudent/nbextensions"):
    root = os.path.relpath(dirname, "e2xstudent")
    for filename in filenames:
        if filename.endswith(".pyc"):
            continue
        extension_files.append(os.path.join(root, filename))

name = u'e2xstudent'

setup_args = dict(
    name=name,
    version='0.0.1',
    description='Student extensions for nbgrader',
    author='Tim Metzler',
    author_email='tim.metzler@h-brs.de',
    license='MIT',
    url='https://github.com/DigiKlausur/e2xstudent',
    keywords=['Notebooks', 'Grading', 'Homework', 'Exam'],
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    packages=find_packages(),
    package_data={
        'e2xstudent': extension_files,
    },
    install_requires=[
        "jupyter",
        "notebook>=4.2",
        "nbconvert==5.6.1",
    ]
)

if __name__ == "__main__":
    setup(**setup_args)