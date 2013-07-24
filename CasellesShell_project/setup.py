#!/usr/bin/env python

"""
Setup script for myshell project.

"""

from setuptools import find_packages, setup

setup (
        name = "CasellesShell",
        version = "1.0.0.a1",
        long_description = "Sample script using cmd2 and requests modules",
        platforms = ["Linux"],
        author = "Arnau Orriols (Josep.Caselles)",
        author_email = "josepcaselles@gmail.com",
        url = "myshel://github.com/JCaselles/SummerTrainingAssignments/tree/"
                "master/CasellesShell_project",
        scripts = ["myshell/CasellesShell"],
        install_requires = ["cmd2", "requests"],
        packages = find_packages()
        )
