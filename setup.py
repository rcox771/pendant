#!/usr/bin/env python
import io
import re
from setuptools import setup, find_packages
import sys

with io.open("./pendant/__init__.py", encoding="utf8") as version_file:
    version_match = re.search(
        r"^__version__ = ['\"]([^'\"]*)['\"]", version_file.read(), re.M
    )
    if version_match:
        version = version_match.group(1)
    else:
        raise RuntimeError("Unable to find version string.")


with io.open("README.rst", encoding="utf8") as readme:
    long_description = readme.read()


setup(
    name="pendant",
    version=version,
    description="Utility for interacting with obsidian markdown",
    long_description=long_description,
    author="Russ Cox",
    author_email="",
    license="MIT license",
    packages=find_packages(
        exclude=[
            "docs",
            "tests",
            "windows",
            "macOS",
            "linux",
            "iOS",
            "android",
            "django",
        ]
    ),
    classifiers=[
        "Development Status :: 1 - Planning",
        "License :: OSI Approved :: MIT license",
    ],
    install_requires=[],
    options={
        "app": {"formal_name": "pendant", "bundle": "pendant"},
        # Desktop/laptop deployments
        "macos": {"app_requires": []},
        "linux": {"app_requires": []},
        "windows": {"app_requires": []},
    },
)
