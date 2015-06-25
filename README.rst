******
pyfeat
******

.. image:: https://travis-ci.org/markovmodel/pyfeat.svg?branch=devel
    :target: https://travis-ci.org/markovmodel/pyfeat
.. image:: https://coveralls.io/repos/markovmodel/pyfeat/badge.svg?branch=devel
   :target: https://coveralls.io/r/markovmodel/pyfeat?branch=devel
.. image:: https://badge.fury.io/py/pyfeat.svg
   :target: https://pypi.python.org/pypi/pyfeat

The python free energy analysis toolkit.

**This code is under very heavy development!**

**Note**:

Currently the following algorithms are featured:

- WHAM
- DTRAM
- XTRAM

In future releases the list of available free energy algorithms will be extended. Watch this space!  


Installation
============
With pip from PyPI::

   # you might have to install these dependencies manually
   pip install cython
   pip install numpy
   pip install pytram

   # install pyfeat
   pip install pyfeat
   
With using conda::

   #Conda should automoatically take care of all dependencies
   conda install -c https://conda.binstar.org/omnia pytram

Authors
=======

- Antonia Mey\ :superscript:`*` <antonia.mey@fu-berlin.de>
- Christoph Wehmeyer\ :superscript:`*` <christoph.wehmeyer@fu-berlin.de>
- Fabian Paul
- Hao Wu
- Frank Noé

``*``) equal contribution

References
==========

* **dTRAM**: *Statistically optimal analysis of state-discretized trajectory data from multiple thermodynamic states*, Hao Wu, Antonia S.J.S. Mey, Edina Rosta, and Frank Noé, **J. Chem. Phys.** 141, 214106 (2014). 

    Download: <http://scitation.aip.org/content/aip/journal/jcp/141/21/10.1063/1.4902240>

* **xTRAM**: *Estimating Equilibrium Expectations from Time-Correlated Simulation Data at Multiple Thermodynamic States*, Antonia S.J.S. Mey, Hao Wu, and Frank Noé, **Phys. Rev. X** 4, 041018 (2014). 

    Download: <http://journals.aps.org/prx/pdf/10.1103/PhysRevX.4.041018>

* **WHAM**:  *The weighted histogram analysis method for free-energy calculations on biomolecules. I. The method*, Shankar Kumar, John M. Rosenberg, Djamal Bouzida, Robert H. Swendsen and Peter A. Kollman, **J. Comput. Chem.** 13, 1011–1021 (1992)

    Download: <http://onlinelibrary.wiley.com/doi/10.1002/jcc.540130812/abstract;jsessionid=096E6ED4241821B755F9424DCE203430.f03t02>

Copyright notice
================

Copyright (c) 2014, Computational Molecular Biology Group, FU Berlin, 14195 Berlin, Germany.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions
are met:

1. Redistributions of source code must retain the above copyright notice,
this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright
notice, this list of conditions and the following disclaimer in the
documentation and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
"AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED
TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.


