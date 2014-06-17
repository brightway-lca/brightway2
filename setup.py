from setuptools import setup

packages = [
    "bw2analyzer>=0.5",
    "bw2calc>=0.14",
    "bw2data>=0.16",
    "bw2ui>=0.12.1",
    "docopt",
    "flask",
    "lxml",
    "nose",
    "numpy",
    "progressbar-ipython",
    "requests>=1.1.0",
    "scipy",
    "stats_arrays>=0.2.4",
    "voluptuous",
]

setup(
    name='brightway2',
    version="0.14",
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
