from os import path
from setuptools import setup, find_packages

with open(path.join(path.abspath(path.dirname(__file__)), 'README'), encoding='utf-8') as f:
    long_description = f.read()
with open(path.join(path.abspath(path.dirname(__file__)), 'VERSION'), encoding='utf-8') as f:
    version = f.read()

setup(name="blotch",
      description="Publication Quality Plotting Utilities for Machine Learning",
      long_description=long_description,
      version=version,
      url="https://github.com/geyang/blotch",
      author="Ge Yang",
      author_email="ge.ike.yang@gmail.com",
      license=None,
      keywords=["blotch", "visualization", "publication", "plot"],
      classifiers=[
          "Development Status :: 4 - Beta",
          "Intended Audience :: Science/Research",
          "Programming Language :: Python :: 3"
      ],
      packages=find_packages(),
      install_requires=[],
      )
