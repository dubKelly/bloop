from setuptools import setup, find_packages

setup(
    name='bloop',
    version='0.0.0',
    author='Jordan Neeb',
    url='https://github.com/dubKelly/bloop.git',
    description='Auto populate spreadsheet from .txtrpt data',
    license='MIT',
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': ['bloop = bloop.app:run'],
    }
)
