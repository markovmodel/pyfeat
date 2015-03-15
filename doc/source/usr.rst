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
   # and [b_K] denotes the reduced bias energies b_K/kT
   # [M]  [T]  [b_0]  [b_1]  ... 
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

In this case, you need the ``[M]`` and ``[T]`` columns, and one reduced potential energy column ``[u_K]``. In this case the third column only contains reduced potential energies: u_K = u(x)/kT_K. The energy is reduced according to the generating thermodynamic state. For example, the entry ``2  5  20.5`` denotes that the actual sample corresponds to the Markov state ``2``, was generated at temperature ``kT_5``, and the corresponding energy was reduced with ``kT_5``.

**Important note**: for temperature-dependent simulations, you need an additional single column ``kT`` file wich indicates all generating temperatures times the Boltzmann constant (consistent with your energy units). Note that the order of ``kT`` values must be constistent with the numbering of the thermodynamic states. Additionally the ``kT.dat`` file will need to contain all tempeartures multiplied by the Botzmann constant. (Make sure that you are suing the correct units here when reducing your potential energies.) The ``kT.dat`` file is just a single column file. ::

   #This is a kT file
   #[kT]
   1.2
   1.4
   1.7
   1.9
   .
   .
   .

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

Assume that we have two files ``file_1.dat`` and ``file_2.dat`` with e.g. umbrella sampling simulation data. In addition to that, the discrete estimator methods require the user to specify the reduced bias energies of all Markov states in each of the thermodynamic states. The corresponding file format is given by ::

   # we store the reduced bias energies b_K(x)/kT
   # at the discrete states x_i
   # [b_0]  [b_1]  ... 
      0.0    4.0
      0.0    0.0
      0.0    8.0

In this example, we have three Markov states which are evaluated at two different thermodynamic states.

Using the API, we can run WHAM via the following code (DTRAM works in the same way, just replace wham with dtram):

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
   data_forge = Forge( reader.trajs, b_K_i=reader.b_K_i )

   # run WHAM using the API function
   wham_obj = wham( data_forge, maxiter=1000, ftol=1.0E-10, verbose=True )

   # show unbiased stationary distribution
   print wham_obj.pi_i

   # show thermodynamic free energies
   print wham_obj.f_K

If the data is generated from a multiple temperature simulation,  the user can still follow the above usage of the WHAM or DTRAM estiamtor, but this time give an additional kT file using the appropritate flag in the Reader and the Forge. Additionaly, now the estimator object ``est.pi_i`` returns by default the probability of all states at the lowest temperatures, if this is not the tempearture of interest, the forge can be given an extra arguemnt, ``target_kT``, to estiamte the stationary probabilties at a different tempearture. 

from file using the runscript
-----------------------------   

Or we can run WHAM with the runscript in the following way from the commandline (DTRAM would will work in the same way using DTRAM as the commanline parameter for the ``--estimator`` flag):

``run_pyfeat file*.dat --estimator WHAM --b_K_i_file b_K_i.dat --maxiter=1000 --ftol 1.0E-5``

For all options given in the runscript, use:

``run_pyfeat --help``



Continuous Estimators (xTRAM)
===================================

Currently, it is only safe to use multiple temperature ensemble simulations with this estimator. In a future rease the fuctionality of this will be enhanced. 

An example usage from file with a ST simulation can be found in the examples directory in the ipython notebook double-well.ipynb.


