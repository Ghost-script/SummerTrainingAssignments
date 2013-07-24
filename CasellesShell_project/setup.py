#!/usr/bin/env python

"""
Setup script for myshell project.

"""

from setuptools import find_packages, setup

setup (
        name = "CasellesShell",
        version = "1.0.0.a9",
        long_description = "Sample script using cmd2 and requests modules",
        platforms = ["Linux"],
        author = "Arnau Orriols (Josep.Caselles)",
        author_email = "josepcaselles@gmail.com",
        url = "https://github.com/JCaselles/SummerTrainingAssignments/tree/"
                "master/CasellesShell_project",
        scripts = ["scripts/CasellesShell"],
        install_requires = ["cmd2 >= 0.6.5.1", "requests >= 1.2.3"],
        dependency_links = [
            "https://pypi.python.org/pypi/cmd2",
            "https://pypi.python.org/pypi/pyparsing/1.5.7",
            "https://pypi.python.org/pypi/requests"
            ],
        )
