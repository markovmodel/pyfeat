r"""

=======================
dTRAM estimator wrapper
=======================

.. moduleauthor:: Antonia Mey <antonia.mey@fu-berlin.de>

"""

import pytram as pt
import numpy as np


class DTRAM( object ):
    r"""
    I am the dTRAM wrapper
    """
    def __init__( self, C_K_ij, b_K_i ):
        r"""
        Initialize the DTRAM object
        
        Parameters
        ----------
        C_K_ij : numpy.ndarray( shape=(T,M,M), dtype=numpy.intc )
            transition counts between the M discrete Markov states for each of the T thermodynamic ensembles
        b_K_i : numpy.ndarray( shape=(T,M), dtype=numpy.float64 )
            bias energies in the T thermodynamic and M discrete Markov states
        """
        self._dtram_obj = pt.DTRAM( C_K_ij = C_K_ij, b_K_i = b_K_i )


    def sc_iteration( self , ftol=10e-4, maxiter = 10, verbose = False):
         self._dtram_obj.sc_iteration( ftol, maxiter, verbose)
         
    @property
    def pi_i( self ):
        return self._dtram_obj.pi_i
     
    @property
    def pi_K_i( self ):
        return self._dtram_obj.pi_K_i
    
    @property
    def f_K( self ):
        return self._dtram_obj.f_K
        
    @property
    def f_K_i( self ):
        return -np.log(self.pi_K_i)
        
    @property
    def f_i( self ):
        return -np.log(self.pi_i)
        
