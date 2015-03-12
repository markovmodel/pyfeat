r"""

=======================
XTRAM estimator wrapper
=======================

.. moduleauthor:: Antonia Mey <antonia.mey@fu-berlin.de>

"""

import pytram as pt
import numpy as np
from pytram import NotConvergedWarning, ExpressionError


class XTRAM( object ):
    r"""
    I am the xTRAM wrapper
    """
    def __init__( self, C_K_ij, b_K_x, T_x, M_x, N_K_i, target=0 ):

        r"""
        Initialize the XTRAM object
        
        Parameters
        ----------
        C_K_ij : 3-D numpy array
            Countmatrix for each thermodynamic state K
        b_K_x : 2-D numpy array
            Biasing tensor
        T_x : 1-D numpy array
            Thermodynamic state trajectory
        M_x : 1-D numpy array
            Markov state trajectories
        N_K_i : 2-D numpy array
            Number of markov samples in each thermodynamic state
        """

        self._xtram_obj = pt.XTRAM( C_K_ij, b_K_x, T_x, M_x, N_K_i, target = 0 )
        self.n_therm_states = np.shape(N_K_i)[0]
        self.n_markov_states = np.shape(N_K_i)[1]


    def sc_iteration( self, maxiter=100, ftol=1.0E-5, verbose=False ):
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
        self._xtram_obj.sc_iteration( maxiter, ftol, verbose)

    @property
    def pi_i( self ):
        return self._xtram_obj.pi_i

    @property
    def pi_K_i( self ):
        return self._xtram_obj.pi_K_i

    @property
    def f_K( self ):
        return self._xtram_obj.f_K

    @property
    def f_K_i( self ):
        return -np.log(self.pi_K_i)

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

    @property
    def citation( self ):
        return self._xtram_obj.citation

    def cite( self, pre="" ):
        self._xtram_obj.cite( pre=pre )

