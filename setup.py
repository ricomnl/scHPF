#!/usr/bin/env python

from setuptools import find_packages, setup

__version__ = '0.2.0'

requires = ['scikit-learn',
            'numba',
            'scipy >= 1.1',
            'numpy']

setup(
    name='scHPF',
    version=__version__,
    packages=find_packages(),
    scripts=['bin/scHPF'],
    python_requires='>=3.6',
    install_requires=requires,
    extras_require={},
    author = 'Hanna Mendes Levitin',
    author_email = 'hml2134@columbia.edu',
    description='Single-cell Hierarchical Poisson Factorization',
    license='GPLv3',
    url='https://www.github.com/simslab/scHPF',
)
