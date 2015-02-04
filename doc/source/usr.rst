.. _ref_user:

==========
User guide
==========

.. toctree::
   :maxdepth: 2


File format
===========

The standard file format assumes text files with the following layout. ::

   # This is a comment line, you can several of those.
   # The next lines indicates the meaning of the columns,
   # [M] denotes Markov state indices (starting from zero),
   # [T] denotes thermodynamic state indices (starting from zero),
   # and [u_I] denotes the reduced bias energies u_I/kT
   # [M]  [T]  [u_0]  [u_1]  ... 
      0    0    3.1   18.2
      1    0    3.2   18.3
      2    0    4.8   19.9
      3    0    7.4   22.5
      .    .      .      .
      .    .      .      .
      .    .      .      .

The minimal layout only requires the ``[M]`` and ``[T]`` columns and can only be used for discrete estimators (dTRAM or WHAM). These two columns contain the sequences of the Markov and generating thermodynamic states. For example, the entry ``3  0`` denotes that the actual sample corresponds to the Markov state ``3`` and was generated at thermodynamic state ``0``.

**Important note**: in order to run dTRAM/WHAM successfully, you need an additional ``b_K_i`` file as explained in the discrete estimators section.

The other TRAM estimators require at least one energy column. For this, we distinguish two different cases:
temperature as the only thermodynamic variable, and all other thermodynamic conditions, i.e., different Hamiltonians, umbrella potentials, ...


Temperature as only thermodynamic variable
------------------------------------------

In this case, you need the ``[M]`` and ``[T]`` columns, and one energy column ``[u_K]``; this column contains the reduced energy sequence. The energy is reduced according to the generating thermodynamic state. For example, the entry ``2  5  20.5`` denotes that the actual sample corresponds to the Markov state ``2``, was generated at temperature ``kT_5``, and the corresponding energy was reduced with ``kT_5``.

**Important note**: for temperature-dependent simulations, you need an additional single column ``kT`` file wich indicates all generating temperatures times the Boltzmann constant (consistent with your energy units). Note that the order of ``kT`` values must be constistent with the numbering of the thermodynamic states.


Hamiltonian replica exchange, umbrella sampling, etc
----------------------------------------------------

This is the most general application. Here, each sample must be evaluated at all thermodynamic states which means that you need as many energy columns as you have thermodynamic states. For example, the line ``2  1  3.0  2.9  1.0  0.3`` indicates that the actual sample corresponds to the Markov state ``2``, has been generated at thermodynamic state ``1``, the reduced energy is

  * ``3.0 kT`` at thermodynamic state ``0``,
  * ``2.9 kT`` at thermodynamic state ``1``,
  * ``1.0 kT`` at thermodynamic state ``2``, and
  * ``0.3 kT`` at thermodynamic state ``3``.

This example also requires you to have exactly four thermodynamic states.


Discrete Estimators (WHAM, dTRAM)
=================================

from files
----------

Assume that we have two files ``file_1.dat`` and ``file_2.dat`` with simulation data. In addition to that, the discrete estimator methods require the user to specify the reduced bias energies of all Markov states in each of the thermodynamic states. The corresponding file format is given by ::

   # we store the reduced bias energies b_K(x)/kT
   # at the discrete states x_i
   # [b_0]  [b_1]  ... 
      0.0    4.0
      0.0    0.0
      0.0    8.0

In this example, we have three Markov states which are evaluated at two different thermodynamic states.

Using the API, we can run WHAM via the following code:

.. code-block:: python

   # import the Reader, Forge and the wham API function
   from pyfeat import Reader, Forge, wham

   # specify your input data files
   files = [ 
         'path/to/file_1.dat',
         'path/to/file_2.dat'
      ]
   b_K_i_file = 'path/to/b_K_i_file.dat'

   # import the files using the Reader
   reader = Reader( files, b_K_i_file=b_K_i_file, verbose=True )

   # convert the input data using TRAMData
   forge = Forge( reader.trajs, b_K_i=reader.b_K_i )

   # run WHAM using the API function
   wham_obj = wham( data, maxiter=1000, ftol=1.0E-10, verbose=True )

   # show unbiased stationary distribution
   print wham.pi_i

   # show thermodynamic free energies
   print wham_obj.f_K
   
Or we can run dTRAM with the API in the following way:

TODO: plese give dTRAM example here


from seqential data
-------------------

The data preparation and the API usage is shown in the ipython example.

Continuous Estimators (MBAR, xTRAM)
===================================
TODO: please fill in the neccessry info here



