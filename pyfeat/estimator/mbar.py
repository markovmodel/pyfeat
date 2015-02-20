r"""

=======================
MBAR estimator wrapper
=======================

.. moduleauthor:: Antonia Mey <antonia.mey@fu-berlin.de>

"""

import pymbar as mb
import numpy as np


class MBAR( object ):
    r"""
    I am the mbar wrapper
    """
    def __init__( self, u_K_n, b_K_i, pymbar=True ):
        
        if pymbar:
            mbar_obj = None
        else:
            print "You want to use an mbar implementation that is not as safe as pymbar, think about this again!"
            m
        
    def sc_iteration( self, ftol=10e-04, maxiter=10000,verbose=False ):
        if mbar_obj is None:
            mbar_obj = mb.MBAR( self.u_I_x, self.N_k, maximum_iterations=maxiter, relative_tolerance=ftol, verbose=verbose )
        return mbar_obj
             
             
class MBAR_LEGACY( object ):
    r"""
    I am the mbar legacy class
    """
    def __init__( self, u_I_x, M_x, T_x ):
        raise NotImplementedError("WRITE MEEEEEEE!")
