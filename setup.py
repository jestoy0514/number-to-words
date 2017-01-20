try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Number To Words',
    'author': 'Jesus Vedasto Olazo',
    'url': 'https://github.com/jestoy0514/number-to-words',
    'download_url': 'https://github.com/jestoy0514/number-to-words',
    'author_email': 'jessie@jestoy.frihost.net',
    'version': '1.0.0',
    'install_requires': ['nose'],
    'packages': ['number_to_words'],
    'scripts': [],
    'name': 'numbertowords'
}

setup(**config)

