from distutils.core import setup

setup(
  name='brightway2',
  version="0.8.1",
  packages=["brightway2"],
  author="Chris Mutel",
  author_email="cmutel@gmail.com",
  license=open('LICENSE.txt').read(),
  install_requires=["bw2data", "bw2calc", "bw2ui", "bw2analyzer"],
  url="https://bitbucket.org/cmutel/brightway2",
  long_description=open('README').read(),
)
