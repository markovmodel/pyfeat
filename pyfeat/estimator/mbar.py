r"""

=======================
MBAR estimator wrapper
=======================

..moduleauthor::Christoph Wehmeyer <christoph.wehmeyer@fu-berlin.de>, Antonia Mey <antonia.mey@fu-berlin.de>,

"""

import pymbar as mb
import numpy as np
from pytram import ExpressionError

class MBAR( object ):
    r"""
    I am the mbar wrapper
    """
    def __init__( self, u_IJ_t, M_J_t, N_J, _legacy=False ):
        self._n_therm_states = None
        self._n_markov_states = None
        self.N_J = N_J
        self.M_J_t = M_J_t
        self.u_IJ_t = u_IJ_t
        if _legacy:
            self._mbar_obj = MBAR_LEGACY( u_IJ_t, M_J_t, N_J )
        else:
            self._mbar_obj = mb.mbar()
        
    def sc_iteration( self, ftol=10e-04, maxiter=10000,verbose=False ):
        if mbar_obj is None:
            mbar_obj = mb.MBAR( self.u_I_x, self.N_k, maximum_iterations=maxiter, relative_tolerance=ftol, verbose=verbose )
        return mbar_obj



    @property
    def n_therm_states( self ):
        if self._n_therm_states is None:
            self._n_therm_states = self.N_J.shape[0]
        return self._n_therm_states

    @property
    def n_markov_states( self ):
        if self._n_markov_states is None:
            self._n_markov_states = self.M_J_t.max() + 1
        return self._n_markov_states



    def _check_N_J( self, N_J ):
        if None is N_J:
            raise ExpressionError( "N_J", "is None" )
        if not isinstance( N_J, (np.ndarray,) ):
            raise ExpressionError( "N_J", "invalid type (%s)" % str( type( N_J ) ) )
        if 1 != N_J.ndim:
            raise ExpressionError( "N_J", "invalid number of dimensions (%d)" % N_J.ndim )
        if np.intc != N_J.dtype:
            raise ExpressionError( "N_J", "invalid dtype (%s)" % str( N_J.dtype ) )
        if not np.all( N_J > 0 ):
            raise ExpressionError( "N_J", "contains non-positive length entries" )
        return True

    @property
    def N_J( self ):
        return self._N_J

    @N_J.setter
    def N_J( self, N_J ):
        self._N_J = None
        if self._check_N_J( N_J ):
            self._N_J = N_J

    def _check_M_J_t( self, M_J_t ):
        if None is M_J_t:
            raise ExpressionError( "M_J_t", "is None" )
        if not isinstance( M_J_t, (np.ndarray,) ):
            raise ExpressionError( "M_J_t", "invalid type (%s)" % str( type( M_J_t ) ) )
        if 1 != M_J_t.ndim:
            raise ExpressionError( "M_J_t", "invalid number of dimensions (%d)" % M_J_t.ndim )
        if M_J_t.shape[0] != self.N_J.max():
            raise ExpressionError( "M_J_t", "unmatching number of samples (%d,%d)" % (M_J_t.shape[0], self.N_J.max()) )
        if np.intc != M_J_t.dtype:
            raise ExpressionError( "M_J_t", "invalid dtype (%s)" % str( M_J_t.dtype ) )
        if not np.all( M_J_t >= 0 ):
            raise ExpressionError( "M_J_t", "contains negative state indices" )
        if not np.all( M_J_t < self.n_markov_states ):
            raise ExpressionError( "M_J_t", "contains too large state indices" )
        return True

    @property
    def M_J_t( self ):
        return self._M_J_t

    @M_J_t.setter
    def M_J_t( self, M_J_t ):
        self._M_J_t = None
        if self._check_M_J_t( M_J_t ):
            self._M_J_t = M_J_t

    def _check_u_IJ_t( self, u_IJ_t ):
        if None is u_IJ_t:
            raise ExpressionError( "u_IJ_t", "is None" )
        if not isinstance( u_IJ_t, (np.ndarray,) ):
            raise ExpressionError( "u_IJ_t", "invalid type (%s)" % str( type( u_IJ_t ) ) )
        if 3 != u_IJ_t.ndim:
            raise ExpressionError( "u_IJ_t", "invalid number of dimensions (%d)" % u_IJ_t.ndim )
        if u_IJ_t.shape[0] != self.n_therm_states:
            raise ExpressionError( "u_IJ_t", "unmatching number of thermodynamic states (%d,%d)" % (u_IJ_t.shape[0], self.n_therm_states) )
        if u_IJ_t.shape[1] != self.n_therm_states:
            raise ExpressionError( "u_IJ_t", "unmatching number of thermodynamic states (%d,%d)" % (u_IJ_t.shape[1], self.n_therm_states) )
        if u_IJ_t.shape[2] != self.M_J_t.shape[1]:
            raise ExpressionError( "u_IJ_t_x", "unmatching sample dimension (%d,%d)" % (u_IJ_t.shape[2], self.M_J_t.shape[1]) )
        if np.float64 != u_IJ_t.dtype:
            raise ExpressionError( "u_IJ_t", "invalid dtype (%s)" % str( u_IJ_t.dtype ) )
        return True

    @property
    def u_IJ_t( self ):
        return self._u_IJ_t

    @u_I_x.setter
    def u_IJ_t( self, u_IJ_t ):
        self._u_IJ_t = None
        if self._check_u_IJ_t( u_IJ_t ):
            self._u_IJ_t = u_IJ_t


class MBAR_LEGACY( object ):
    r"""
    I am the mbar legacy class
    """
    def __init__( self, u_IJ_t, M_J_t, N_J ):
        raise NotImplementedError('I need to be implemented')








