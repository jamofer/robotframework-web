import sys

from setuptools import setup
from setuptools.command.test import test as TestCommand


PYTEST_ARGS = '--cov=robot_webserver --junitxml results.xml --color=yes test'


class PyTest(TestCommand):
    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = ''

    def run_tests(self):
        import pytest
        errno = pytest.main(PYTEST_ARGS.split())
        sys.exit(errno)


setup(
    name='robotframework-webserver-listener',
    version='',
    packages=['robot_webserver'],
    url='',
    license='',
    author='jamoh',
    author_email='',
    description='',
    install_requires=['requests', 'mock'],
    tests_require=['pytest', 'pytest-cov', 'pytest-remove-stale-bytecode'],
    cmdclass={'test': PyTest}
)
