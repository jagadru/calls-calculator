from setuptools import find_packages, setup

from calls_calculator.version import __version__

setup(
    name='fee_call_calculator',
    version=__version__,
    author='Julian A. Garcia de Rubertis',
    packages=find_packages(exclude=['tests', 'tests.*']),
    setup_requires=['pytest-runner'],
)
