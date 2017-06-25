#!/usr/bin/env python3

from setuptools import setup

setup(name='linode_api3',
      version='0.1.5',
      description='Linode APIv3 client for Python3',
      author='Phil Eaton',
      url='https://github.com/eatonphil/python3-linode_api3',
      install_requires=['requests'],
      packages=['linode_api3'],
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Environment :: Console',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: BSD License',
          'Operating System :: MacOS :: MacOS X',
          'Operating System :: Unix',
          'Operating System :: POSIX',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3',
          'Topic :: Software Development',
          'Topic :: Software Development :: Libraries',
          'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
