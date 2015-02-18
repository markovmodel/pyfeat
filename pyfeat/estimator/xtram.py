r"""

=======================
XTRAM estimator wrapper
=======================

.. moduleauthor:: Antonia Mey <antonia.mey@fu-berlin.de>

"""

import pytram as pt
import numpy as np


class XTRAM( pt.XTRAM ):
    r"""
    I am the xTRAM estimator
    """
    def __init__( self, C_K_ij, u_I_x, T_x, M_x, N_K_i, target = 0, verbose = False ):

        r"""
        Initialize the XTRAM object
        
        Parameters
        ----------
        C_K_ij : 3-D numpy array
            Countmatrix for each thermodynamic state K
        u_I_x : 2-D numpy array
            Biasing tensor
        T_x : 1-D numpy array
            Thermodynamic state trajectory
        M_x : 1-D numpy array
            Markov state trajectories
        N_K_i : 2-D numpy array
            Number of markov samples in each thermodynamic state
        N_K : 1-D numpy array
            Numer of thermodynamic samples array
        target : Integer 
            target state for which pi_i should be computed
            default : 0
        verbose : Boolean
            Be loud and noisy
        """
        N_K = np.sum(N_K_i, axis=1)
        self._xtram_obj = pt.XTRAM( C_K_ij = C_K_ij, u_I_x = u_I_x, T_x = T_x, M_x = M_x, N_K_i = N_K_i, N_K = N_K target = 0, verbose = False )


     def sc_iteration( self , ftol=10e-4, maxiter = 10, verbose = False):
         self._xtram_obj.sc_iteration( ftol, maxiter, verbose)
         
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
        
        
         
         
