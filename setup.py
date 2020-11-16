import os
import pathlib

from setuptools import setup, find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

setup(
    name="bigninja",
    version="0.0.1",
    description="pyspark helpers",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/aloneguid/bigninja",
    author="Ivan Gavryliuk",
    author_email="aloneguid@outlook.com",
    license="Apache-2.0",
    packages=find_packages(),
    include_package_data=True
)

# 1. run python setup.py bdist_wheel
# 2. twine upload dist/*

# https://realpython.com/pypi-publish-python-package/#adding-files-to-your-package