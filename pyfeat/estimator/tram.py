r"""

======================
TRAM estimator wrapper
======================

.. moduleauthor:: Christoph Wehmeyer <christoph.wehmeyer@fu-berlin.de>

"""

import pytram as pt
import numpy as np

class TRAM( object ):
    r"""
    I am the TRAM wrapper
    """
    def __init__( self, C_K_ij, u_I_x, M_x, N_K_i ):
        r"""
        Initialize the TRAM object
        
        Parameters
        ----------
        C_K_ij : numpy.ndarray( shape=(T,M,M), dtype=numpy.intc )
            transition counts between the M discrete Markov states for each of the T thermodynamic ensembles
        """
        try:
            self._tram_obj = pt.TRAM( C_K_ij, u_I_x, M_x, N_K_i )
        except AttributeError, e:
            raise NotImplementedError( "The TRAM estimator is not yet implemented in the pytram package" )

    def sc_iteration( self , ftol=1.0e-15, maxiter=1000, verbose=False ):
         self._tram_obj.sc_iteration( ftol=ftol, maxiter=maxiter, verbose=verbose )
         
    @property
    def pi_i( self ):
        return self._tram_obj.pi_i
     
    @property
    def pi_K_i( self ):
        return self._tram_obj.pi_K_i
    
    @property
    def f_K( self ):
        return self._tram_obj.f_K
        
    @property
    def f_K_i( self ):
        return -np.log( self.pi_K_i )
        
    @property
    def f_i( self ):
        return -np.log( self.pi_i )
