#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from setuptools import setup, find_packages
from setup_utils import read, read_section

PACKAGE_NAME = "birdhouse-toolbox"
SOURCE_DIR_NAME = "birdhouse_toolbox"
HOMEPAGE_URL = "https://www.alexseitsinger.com/packages/python/{}".format(PACKAGE_NAME)
GITHUB_URL = "https://github.com/alexseitsinger/{}".format(PACKAGE_NAME)
README_NAME = "README.md"

setup(
    name=PACKAGE_NAME,
    version=read(("src", SOURCE_DIR_NAME, "__init__.py"), "__version__"),
    description=read_section((README_NAME,), "Description", (0,)),
    long_description=read((README_NAME,)),
    long_description_content_type="text/markdown",
    author="Alex Seitsinger",
    author_email="software@alexseitsinger.com",
    url=HOMEPAGE_URL,
    install_requires=[
        "requests",
        "click",
        "python-slugify",
        "maya",
        "google-api-python-client",
        "bs4",
        "validators",
    ],
    entry_points={"console_scripts": ["bht={}.cli:main".format(SOURCE_DIR_NAME)]},
    package_dir={"": "src"},
    packages=find_packages("src", exclude=["tests"]),
    include_package_data=True,
    license="BSD 2-Clause License",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Information Technology",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Topic :: Communications",
        "Topic :: Internet :: WWW/HTTP :: Site Management",
        "Topic :: Text Processing :: Markup :: HTML",
    ],
    project_urls={
        "Documentation": HOMEPAGE_URL,
        "Source": GITHUB_URL,
        "Tracker": "{}/issues".format(GITHUB_URL),
    },
)
