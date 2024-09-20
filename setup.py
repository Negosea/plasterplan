# setup.py
from setuptools import setup, find_packages

setup(
    name='plasterplan',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'matplotlib',
    ],
    entry_points={
        'console_scripts': [
            'plasterplan=plasterplan.__main__:main',
        ],
    },
)
