from setuptools import setup

setup(
  name='devenney-accounts',
  version='0.1.0',
  author='Brendan Devenney',
  author_email='brendan@devenney.io',
  packages=['devenney.accounts'],
  package_dir = {
    'devenney.accounts': './accounts'
  },
  package_data={'devenney.accounts':['templates/*/*.html','templates/*/*/*.html']},
  url='https://github.com/devenney/django_accounts',
  license='LICENSE',
  install_requires=[
    "Django >= 2.0"
  ],
)
