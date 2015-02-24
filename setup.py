from setuptools import setup
from os.path import join, dirname
import numpy as np


setup(
    name='pyfeat',
    version='0.3.0',
    description='The python free energy analysis toolkit',
    long_description='Commandline toolkit that allows the use of different free energy estimators using a single format',
    classifiers=[
            'Development Status :: 2 - Pre-alpha',
            'Environment :: Console',
            'Intended Audience :: Science/Research',
            'License :: OSI Approved :: BSD License',
            'Natural Language :: English',
            'Operating System :: MacOS :: MacOS X',
            'Operating System :: POSIX :: Linux',
            'Programming Language :: C',
            'Programming Language :: Cython',
            'Programming Language :: Python :: 2.7',
            'Topic :: Scientific/Engineering :: Bio-Informatics',
            'Topic :: Scientific/Engineering :: Chemistry',
            'Topic :: Scientific/Engineering :: Mathematics',
            'Topic :: Scientific/Engineering :: Physics'
        ],
    keywords=[ 'TRAM', 'WHAM', 'MBAR', 'free energy' ],
    url='http://github.com/markovmodel/pyfeat',
    author='The pyfeat team',
    author_email='pyfeat@lists.fu-berlin.de',
    license='Simplified BSD License',
    setup_requires=[ 'numpy>=1.7.1', 'cython>=0.15', 'setuptools>=0.6', 'pytram>=0.1.6' ],
    tests_require=[ 'numpy>=1.7.1', 'pymbar==2.0.0-beta', 'nose>=1.3' ],
    install_requires=[ 'numpy>=1.7.1', 'pymbar==2.0.0-beta' ],
    packages=[
            'pyfeat',
            'pyfeat.reader',
            'pyfeat.forge',
            'pyfeat.estimator',
            'pyfeat.api'
        ],
    test_suite='nose.collector',
    scripts=[
            'bin/dtram.py',
            'bin/wham.py',
            'bin/xtram.py'
        ]
)
