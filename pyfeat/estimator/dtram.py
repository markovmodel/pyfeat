r"""

=======================
dTRAM estimator wrapper
=======================

.. moduleauthor:: Antonia Mey <antonia.mey@fu-berlin.de>, Christoph Wehmeyer <christoph.wehmeyer@fu-berlin.de>

"""

import pytram as pt
import numpy as np
from pytram import NotConvergedWarning, ExpressionError


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

        self._dtram_obj = pt.DTRAM( C_K_ij, b_K_i )
        self.n_therm_states = np.shape(b_K_i)[0]
        self.n_markov_states = np.shape(b_K_i)[1]


    def sc_iteration( self , ftol=1.0e-15, maxiter=1000, verbose=False ):
         self._dtram_obj.sc_iteration( ftol=ftol, maxiter=maxiter, verbose=verbose )
         
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
        return -np.log( self.pi_K_i )
        
    @property
    def f_i( self ):
        return -np.log(self.pi_i)
    
    @property
    def n_therm_states( self ):
        return self._n_therm_states
    
    @n_therm_states.setter
    def n_therm_states( self, m ):
        self._n_therm_states = m

    @property
    def n_markov_states( self ):
        return self._n_markov_states
        
    @n_markov_states.setter
    def n_markov_states( self, n ):
        self._n_markov_states = n
        
