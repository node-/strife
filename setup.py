import os
from setuptools import setup, find_packages

setup(
    name = "strife",
    version = "0.0.0",
    author = "Jake Kosberg",
    author_email = "jakekosberg@gmail.com",
    description = ("Literally the dumbest bot."),
    license = "BSD",
    package_dir = {'strife' : 'src'},
    packages=['strife'],
    scripts = ['bin/strife']
)
