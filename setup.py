from setuptools import setup

packages = [
    "lxml",
    "numpy",
    "scipy",
    "nose",
    "progressbar",
    "voluptuous",
    "fuzzywuzzy",
    "flask",
    "docopt",
    "bw2calc",
    "bw2ui",
    "bw2analyzer",
    "bw2data",
    "requests",
    "bw-stats-toolkit",
]

setup(
  name='brightway2',
  version="0.8.2",
  packages=["brightway2"],
  author="Chris Mutel",
  author_email="cmutel@gmail.com",
  license=open('LICENSE.txt').read(),
  install_requires=packages,
  url="https://bitbucket.org/cmutel/brightway2",
  long_description=open('README').read(),
)
