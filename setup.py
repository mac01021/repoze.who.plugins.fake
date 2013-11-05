from setuptools import setup, find_packages
import sys, os
 
version = '0.1'
 
README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()
 
setup(name='repoze.who.plugins.fake',
      version=version,
      description="A collection of repoze.who plugins meant to help with testing",
      long_description=README,
      classifiers=[],
      keywords='',
      author='',
      author_email='coolbeth@gmail.com',
      url='',
      license='',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      """,
      )
 
