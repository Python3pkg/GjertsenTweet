"""
long description
"""

from setuptools import setup

setup(name='GjertsenTweet',
      version='0.1',
      description='A simple twitter client for the terminal',
      long_description = __doc__,
      author='Fredrik Gjertsen',
      author_email='f.gjertsen@gmail.com',
      packages=['GjertsenTweet'],
      license='GNU General Public License',
      install_requires=['npyscreen==4.9.1',
                        'twitter==1.17.0'],
      entry_points={
          'console_scripts':
            ['gjertsentweet=Gjertsen.client:main'],
          },
      classifiers=['Development Status :: 4 - Beta',
                   'Environment :: Console',
                   'Intedned Audience :: End Users/Desktop',
                   'Natural Language :: English',
                   'Programming Language :: Python :: 2.7'
                   'Topic :: Utilities',
                   'License :: GNU General Public License'],
      keywords='twitter, command-line tools')


__author__ = 'Fredrik Gjertsen'

