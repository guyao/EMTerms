from setuptools import setup, find_packages


DESCRIPTION = "EMTerms parser"
LONG_DESCRIPTION = open('README.md').read()
NAME = "EMTerms"
AUTHOR = "Yao Gu"
AUTHOR_EMAIL = "yaogu@usc.edu"
MAINTAINER = "Yao Gu"
MAINTAINER_EMAIL = "yaogu@usc.edu"
VERSION = "0.1"

setup(name=NAME,
      version=VERSION,
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      author=AUTHOR,
      author_email=AUTHOR_EMAIL,
      maintainer=MAINTAINER,
      maintainer_email=MAINTAINER_EMAIL,
      packages=find_packages(
        exclude=["tests.*", "tests"]
        ),

      package_data = {
        # If any package contains *.txt or *.rst files, include them:
        '': ['data/*.csv', 'data/README.txt'],
        },

      classifiers=[
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6'],
      )