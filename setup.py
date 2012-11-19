from distutils.core import setup
import os

packages = []
root_dir = os.path.dirname(__file__)
if root_dir:
    os.chdir(root_dir)

for dirpath, dirnames, filenames in os.walk('brightway2'):
    # Ignore dirnames that start with '.'
    if '__init__.py' in filenames:
        pkg = dirpath.replace(os.path.sep, '.')
        if os.path.altsep:
            pkg = pkg.replace(os.path.altsep, '.')
        packages.append(pkg)

setup(
  name='brightway2',
  version="0.9",
  packages=packages,
  author="Chris Mutel",
  author_email="cmutel@gmail.com",
  license=open('LICENSE.txt').read(),
  requires=["voluptuous", "nose", "progressbar", "numpy", "lxml", "fuzzywuzzy"],
  url="https://bitbucket.org/cmutel/brightway2",
  long_description=open('README').read(),
)
