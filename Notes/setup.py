# -*- coding: utf-8 -*-
# Copyright (C) 2018-2026 Connet Information Technology Company, Shanghai.

from setuptools import find_packages, setup

setup(
    name='xSide-Tutorial-Notes',
    version='0.1.0a0',
    packages=find_packages(),
    include_package_data=True,
    package_data={},
    author="Connet Information Technology Company Ltd, Shanghai.",
    author_email="tech_support@shconnet.com.cn",
    description="X Qt framework.",
    long_description="",
    long_description_content_type="text/markdown",
    keywords="Qt Python",
    url="",
    project_urls={
    },
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Software Development :: Interpreters",
    ],
    install_requires=[],
    entry_points={
        "xSide": [
            f"xSide-Tutorial-Notes = x_notes.plugin:Notes",
        ]
    }
)