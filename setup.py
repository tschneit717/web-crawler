from setuptools import setup

setup(
    name='foo',
    version='1.0',
    description='A useful module',
    author='Tom Schneider',
    author_email='tschneit717@gmail.com',
    packages=[''],  #same as name
    install_requires=['beautifulsoup4'], #external packages as dependencies
)