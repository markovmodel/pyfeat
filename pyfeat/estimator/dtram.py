r"""
=======================
dTRAM estimator wrapper
=======================

.. moduleauthor:: Antonia Mey <antonia.mey@fu-berlin.de>, Christoph Wehmeyer <christoph.wehmeyer@fu-berlin.de>

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
        self._dtram_obj = pt.DTRAM( C_K_ij, b_K_i )

    def sc_iteration( self, maxiter=100, ftol=1.0e-5, verbose=False ):
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
        return self._dtram_obj.f_K_i

    @property
    def f_i( self ):
        return self._dtram_obj.f_i

    @property
    def n_therm_states( self ):
        return self._dtram_obj.n_therm_states

    @property
    def n_markov_states( self ):
        return self._dtram_obj.n_markov_states

    @property
    def citation( self ):
        return self._dtram_obj.citation

    def cite( self, pre="" ):
        self._dtram_obj.cite( pre=pre )
