from setuptools import setup
from os.path import join, dirname
import versioneer

setup(
    cmdclass=versioneer.get_cmdclass(),
    name='pyfeat',
    version=versioneer.get_version(),
    description='The python free energy analysis toolkit',
    long_description='Commandline toolkit that allows the use of different free energy estimators using a single format',
    classifiers=[
            'Development Status :: 3 - Alpha',
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
    keywords=[ 'TRAM', 'WHAM', 'free energy' ],
    url='http://github.com/markovmodel/pyfeat',
    author='The pyfeat team',
    author_email='pyfeat@lists.fu-berlin.de',
    license='Simplified BSD License',
    setup_requires=[ 'numpy>=1.7.1', 'setuptools>=0.6', 'pytram>=0.2.0' ],
    tests_require=[ 'numpy>=1.7.1', 'nose>=1.3' ],
    install_requires=[ 'numpy>=1.7.1' ],
    packages=[
            'pyfeat',
            'pyfeat.reader',
            'pyfeat.forge',
            'pyfeat.estimator',
            'pyfeat.api'
        ],
    test_suite='nose.collector',    
    scripts=[
            'bin/run_pyfeat.py'
        ]
)
