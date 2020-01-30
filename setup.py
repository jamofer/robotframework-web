import sys

from setuptools import setup
from setuptools.command.test import test as TestCommand


PYTEST_ARGS = '--cov=robotframework_rest_listener --junitxml results.xml --color=yes test'


class PyTest(TestCommand):
    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = ''

    def run_tests(self):
        import pytest
        errno = pytest.main(PYTEST_ARGS.split())
        sys.exit(errno)


setup(
    name='robotframework-web',
    version='',
    packages=['robotframework_rest_listener'],
    url='',
    license='',
    author='jamoh',
    author_email='',
    description='',
    install_requires=['simple_websocket_server', 'mock'],
    tests_require=['pytest', 'pytest-cov', 'pytest-remove-stale-bytecode'],
    cmdclass={'test': PyTest}
)
