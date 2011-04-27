#!/usr/bin/python
# -*- coding:Utf-8 -*-

from setuptools import setup

setup(name='PipeTK',
      version='0.1',
      description='Collection of small scripts that modify input received via shell pipe',
      long_description = open('README').read(),
      author='Laurent Peuch',
      author_email='cortex@worlddomination.be',
      url='http://blog.worlddomination.be/pipetk',
      install_requires=['mechanize'],
      packages=[],
      scripts=['puniq', 'pipetk', 'pdetinyfy', 'pmerge', 'purls', 'purltitle'],
      license = "GPLv3+",
      keywords="sh bash shell pipe stream cli",
      classifiers=['Development Status :: 4 - Beta',
                   'Environment :: Console',
                   'Intended Audience :: End Users/Desktop',
                   'License :: OSI Approved :: GNU General Public License (GPL)',
                   'Programming Language :: Python',
                  ],

     )

# vim:set shiftwidth=4 tabstop=4 expandtab:
