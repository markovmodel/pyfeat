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
    def __init__( self, C_K_ij, b_K_x, M_x, N_K_i ):
        r"""
        Initialize the TRAM object

        Parameters
        ----------
        C_K_ij : numpy.ndarray( shape=(T,M,M), dtype=numpy.intc )
            transition counts between the M discrete Markov states for each of the T thermodynamic ensembles
        b_K_x : numpy.ndarray( shape=(T,samples), dtype=numpy.float )
            all samples for biases at thermodynamic state K
        M_x : numpy.ndarray( shape=(samples), dtype=numpy.intc )
            trajectory of Markov states sampled
        N_K_i : numpy.ndarray( shape=(T,M), dtype=numpy.intc )
           total number of counts from simulation at T in M discrete Markov state (bin)
        """
        try:
            self._tram_obj = pt.TRAM( C_K_ij, b_K_x, M_x, N_K_i )
        except AttributeError, e:
            raise NotImplementedError( "The TRAM estimator is not yet implemented in the pytram package" )

    def sc_iteration( self , maxiter=100, ftol=1.0E-5, verbose=False ):
        r"""
        sc_iteration function

        Parameters
        ----------
        maxiter : int
            maximum number of self-consistent-iteration steps
        ftol : float (> 0.0)
            convergence criterion based on the max relative change in an self-consistent-iteration step
        verbose : boolean
            Be loud and noisy
        """
        self._tram_obj.sc_iteration( maxiter=maxiter, ftol=ftol, verbose=verbose )
         
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

    @property
    def citation( self ):
        return self._tram_obj.citation

    def cite( self, pre="" ):
        self._tram_obj.cite( pre=pre )
