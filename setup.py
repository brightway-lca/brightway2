from setuptools import setup

packages = [
    "appdirs",
    "asteval",
    "bw2analyzer>=0.9",
    "bw2calc>=1.2.1",
    "bw2data>=2.0.1",
    "bw2io>=0.4.1",
    "bw2parameters>=0.5.1",
    "docopt",
    "eight",
    "flask",
    "future",
    "lxml",
    "numpy",
    "peewee>=2.8",
    "psutil",
    "pyprind",
    "requests",
    "scipy",
    "stats_arrays>=0.4.1",
    "unicodecsv",
    "voluptuous",
    "whoosh>=2.7.4",
    "xlrd",
    "xlsxwriter",
]

setup(
    name='brightway2',
    version="2.0.3",
    packages=["brightway2"],
    author="Chris Mutel",
    author_email="cmutel@gmail.com",
    license=open('LICENSE.txt').read(),
    install_requires=packages,
    url="https://bitbucket.org/cmutel/brightway2",
    long_description=open('README.rst').read(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 2 :: Only',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Topic :: Scientific/Engineering :: Visualization',
    ],
)
