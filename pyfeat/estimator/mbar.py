#r"""

#=======================
#MBAR estimator wrapper
#=======================

#..moduleauthor::Christoph Wehmeyer <christoph.wehmeyer@fu-berlin.de>, Antonia Mey <antonia.mey@fu-berlin.de>,

#"""

#import pymbar as mb
#import numpy as np
#from pytram import ExpressionError

#class MBAR( object ):
#    r"""
#    I am the mbar wrapper
#    """
#    def __init__( self, b_IK_x, b_K_x, M_I_x, N_K ):
#        self._n_therm_states = None
#        self._n_markov_states = None
#        self.N_K = N_K
#        self.M_I_x = M_I_x
#        self.b_IK_x = b_IK_x
#        self.b_K_x = b_K_x
#        self._mbar_obj = mb.MBAR( b_IK_x, N_K, maximum_iterations=0, verbose=False )
#        self.citation = [
#                "Statistically optimal analysis of samples from multiple equilibrium states;",
#                "Michael R Shirts and John D Chodera ",
#                "J. Chem. Phys. 129:124105 (2008)"
#            ]

#    def sc_iteration( self, maxiter=1000, ftol=1.0e-6, verbose=False ):
#        self._mbar_obj._selfConsistentIteration( maximum_iterations=maxiter, relative_tolerance=ftol, verbose=verbose )

#    def cite( self, pre="" ):
#        for line in self.citation:
#            print "%s%s" % ( pre, line )

#    @property
#    def n_therm_states( self ):
#        if self._n_therm_states is None:
#            self._n_therm_states = self.N_K.shape[0]
#        return self._n_therm_states

#    @property
#    def n_markov_states( self ):
#        if self._n_markov_states is None:
#            self._n_markov_states = self.M_I_x.max() + 1
#        return self._n_markov_states

#    @property
#    def f_K( self ):
#        return self._mbar_obj.f_k

#    @property
#    def f_K_i( self ):
#        raise NotImplementedError('Property not available yet')

#    @property
#    def pi_i( self ):
#        raise NotImplementedError('Property not available yet')

#    @property 
#    def pi_K_i( self ):
#       raise NotImplementedError('Property not available yet')


#######################################################################
#    MBAR Legacy class                                                #
#######################################################################

# class MBAR_LEGACY( object ):
#     r"""
#     I am the mbar legacy class
#     """
#     def __init__( self, b_IK_x, M_I_x, N_K ):
#         raise NotImplementedError('I need to be implemented')
        
#     def _check_N_K( self, N_K ):
#         if None is N_K:
#             raise ExpressionError( "N_K", "is None" )
#         if not isinstance( N_K, (np.ndarray,) ):
#             raise ExpressionError( "N_K", "invalid type (%s)" % str( type( N_K ) ) )
#         if 1 != N_K.ndim:
#             raise ExpressionError( "N_K", "invalid number of dimensions (%d)" % N_K.ndim )
#         if np.intc != N_K.dtype:
#             raise ExpressionError( "N_K", "invalid dtype (%s)" % str( N_K.dtype ) )
#         if not np.all( N_K > 0 ):
#             raise ExpressionError( "N_K", "contains non-positive length entries" )
#         return True

#     @property
#     def N_K( self ):
#         return self._N_K

#     @N_K.setter
#     def N_K( self, N_K ):
#         self._N_K = None
#         if self._check_N_K( N_K ):
#             self._N_K = N_K

#     def _check_M_I_x( self, M_I_x ):
#         if None is M_I_x:
#             raise ExpressionError( "M_I_x", "is None" )
#         if not isinstance( M_I_x, (np.ndarray,) ):
#             raise ExpressionError( "M_I_x", "invalid type (%s)" % str( type( M_I_x ) ) )
#         if 1 != M_I_x.ndim:
#             raise ExpressionError( "M_I_x", "invalid number of dimensions (%d)" % M_I_x.ndim )
#         if M_I_x.shape[0] != self.N_K.max():
#             raise ExpressionError( "M_I_x", "unmatching number of samples (%d,%d)" % (M_I_x.shape[0], self.N_K.max()) )
#         if np.intc != M_I_x.dtype:
#             raise ExpressionError( "M_I_x", "invalid dtype (%s)" % str( M_I_x.dtype ) )
#         if not np.all( M_I_x >= 0 ):
#             raise ExpressionError( "M_I_x", "contains negative state indices" )
#         if not np.all( M_I_x < self.n_markov_states ):
#             raise ExpressionError( "M_I_x", "contains too large state indices" )
#         return True

#     @property
#     def M_I_x( self ):
#         return self._M_I_x

#     @M_I_x.setter
#     def M_I_x( self, M_I_x ):
#         self._M_I_x = None
#         if self._check_M_I_x( M_I_x ):
#             self._M_I_x = M_I_x

#     def _check_b_IK_x( self, b_IK_x ):
#         if None is b_IK_x:
#             raise ExpressionError( "b_IK_x", "is None" )
#         if not isinstance( b_IK_x, (np.ndarray,) ):
#             raise ExpressionError( "b_IK_x", "invalid type (%s)" % str( type( b_IK_x ) ) )
#         if 3 != b_IK_x.ndim:
#             raise ExpressionError( "b_IK_x", "invalid number of dimensions (%d)" % b_IK_x.ndim )
#         if b_IK_x.shape[0] != self.n_therm_states:
#             raise ExpressionError( "b_IK_x", "unmatching number of thermodynamic states (%d,%d)" % (b_IK_x.shape[0], self.n_therm_states) )
#         if b_IK_x.shape[1] != self.n_therm_states:
#             raise ExpressionError( "b_IK_x", "unmatching number of thermodynamic states (%d,%d)" % (b_IK_x.shape[1], self.n_therm_states) )
#         if b_IK_x.shape[2] != self.M_I_x.shape[1]:
#             raise ExpressionError( "b_IK_x_x", "unmatching sample dimension (%d,%d)" % (b_IK_x.shape[2], self.M_I_x.shape[1]) )
#         if np.float64 != b_IK_x.dtype:
#             raise ExpressionError( "b_IK_x", "invalid dtype (%s)" % str( b_IK_x.dtype ) )
#         return True

#     @property
#     def b_IK_x( self ):
#         return self._b_IK_x

#     @u_I_x.setter
#     def b_IK_x( self, b_IK_x ):
#         self._b_IK_x = None
#         if self._check_b_IK_x( b_IK_x ):
#             self._b_IK_x = b_IK_x








