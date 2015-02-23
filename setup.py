from setuptools import setup
from os.path import join, dirname
import numpy as np

def read( filename ):
    return open( join( dirname( __file__ ), filename ) ).read()

setup(
    name='pyfeat',
    version='0.3.0',
    description='The python free energy analysis toolkit',
    long_description=read( 'README.rst' ),
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
    keywords=[ 'MBAR', 'WHAM', 'TRAM', 'free energy' ],
    url='http://github.com/markovmodel/pyfeat',
    author='The pyfeat team',
    author_email='pyfeat@lists.fu-berlin.de',
    license='Simplified BSD License',
    setup_requires=[ 'numpy>=1.7.1', 'cython>=0.15', 'setuptools>=0.6', 'pytram>=0.1' ],
    tests_require=[ 'numpy>=1.7.1', 'pymbar==2.0' ],
    install_requires=[ 'numpy>=1.7.1', 'pymbar==2.0' ],
    packages=[
            'pyfeat',
            'pyfeat.reader',
            'pyfeat.forge',
            'pyfeat.estimator',
            'pyfeat.estimator.wham',
            'pyfeat.estimator.mbar',
            'pyfeat.estimator.tram',
            'pyfeat.estimator.dtram',
            'pyfeat.estimator.xtram'
        ]
)
