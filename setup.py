#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from setuptools import setup, find_packages
from setup_utils import PACKAGE_NAME, read


setup(
    name=PACKAGE_NAME,
    version=read(("src", PACKAGE_NAME, "__init__.py",), "__version__"),
    description=(
        "A collection of commnad line tools to automate various online "
        "marketing processes"
    ),
    long_description=read(("README.md",)),
    long_description_content_type="text/markdown",
    author="Alex Seitsinger",
    author_email="contact@alexseitsinger.com",
    url="https://github.com/alexseitsinger/{}".format(PACKAGE_NAME),
    install_requires=["requests", "click", "python-slugify"],
    entry_points={"console_scripts": ["bht={}.cli:main".format(PACKAGE_NAME)]},
    package_dir={"": "src"},
    packages=find_packages("src", exclude=["tests"]),
    include_package_data=True,
    license="BSD 2-Clause License",
    classifiers=[
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 3",
    ]
)
