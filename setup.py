from setuptools import setup, find_packages
import os

version = '0.2'

long_description = (
    open('README.txt').read()
    + '\n' +
    'Contributors\n'
    '============\n'
    + '\n' +
    open('CONTRIBUTORS.txt').read()
    + '\n' +
    open('CHANGES.txt').read()
    + '\n')

setup(name='collective.ie8nomore',
      version=version,
      description="Plone viewlet to prompt users to upgrade to a better web browser.",
      long_description=long_description,
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='plone internet explorer',
      author='Noe Nieto',
      author_email='nnieto@noenieto.com',
      url='http://github.com/collective/',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'Products.CMFPlone',
          'plonetheme.sunburst'
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
