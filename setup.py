# coding: utf-8

"""

cloudtower operation API and SDK  # noqa: E501

The version of the OpenAPI document: 2.20.0
Contact: info@smartx.com
Generated by: https://openapi-generator.tech
"""

import os
from setuptools import setup, find_packages  # noqa: H301

NAME = "cloudtower-sdk"
VERSION = "2.20.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.25.3", "six >= 1.10", "python-dateutil"]
packages = find_packages(exclude=["test", "test.*"])


# 读取 README.md 文件内容
def read_file(filename):
    with open(os.path.join(os.path.dirname(__file__), filename), "rb") as f:
        return f.read().decode("utf-8")


setup(
    name=NAME,
    version=VERSION,
    description="",
    author="Cloudtower developers",
    author_email="info@smartx.com",
    url="https://github.com/smartxworks/cloudtower-python-sdk",
    keywords=["OpenAPI", "OpenAPI-Generator", ""],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    long_description_content_type="text/markdown",
    long_description=read_file("README.md"),
)
