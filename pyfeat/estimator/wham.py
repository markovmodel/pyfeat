r"""

=====================
WHAM estimator module
=====================

.. moduleauthor:: Antonia Mey <antonia.mey@fu-berlin.de>, Christoph Wehmeyer <christoph.wehmeyer@fu-berlin.de>

"""

import numpy as np
from pytram import NotConvergedWarning, ExpressionError


####################################################################################################
#                                                                                                  #
#   WHAM ESTIMATOR CLASS                                                                           #
#                                                                                                  #
####################################################################################################
class WHAM( object ):
    r"""
    I run the WHAM estimator
    """
    def __init__( self, N_K_i, b_K_i ):
        r"""
        Initialize the WHAM object
        
        Parameters
        ----------
        N_K_i : numpy.ndarray( shape=(T,M), dtype=numpy.intc )
            total number of counts from simulation at T in M discrete Markov state (bin)
        b_K_i : numpy.ndarray( shape=(T,M), dtype=numpy.float64 )
            bias energies in the T thermodynamic and M discrete Markov states
        """
        self._n_therm_states = N_K_i.shape[0]
        self._n_markov_states = N_K_i.shape[1]
        self.gamma_K_i = b_K_i
        self._N_K_i = N_K_i
        self._pi_i = np.zeros( shape=(self.n_markov_states,), dtype=np.float64 )
        self._f_K = None
        self._pi_K_i = None
        self.citation = [
                "The weighted histogram analysis method for free-energy calculations on biomolecules;", 
                "Shankar Kumar, John M. Rosenberg, Djamal Bouzida, Robert H. Swendsen and Peter A. Kollman",
                "J. Comput. Chem. 13, 1011-1021 (1992)"
            ]

    def cite( self, pre="" ):
        for line in self.citation:
            print "%s%s" % ( pre, line )

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
        # reset internal storage variables
        self._pi_K_i = None
        self._f_K = np.ones( shape=(self.n_therm_states,), dtype=np.float64 )
        finc = None
        if verbose:
            print "# %25s %25s" % ( "[iteration step]", "[relative increment]" )
        if np.all( self.pi_i == 0.0 ):
            self._pi_i[:] = self._p_step()
        for i in xrange( maxiter ):
            f_new = self._f_step()
            nonzero = self._f_K.nonzero()
            finc = np.max( np.abs( ( f_new[nonzero] - self._f_K[nonzero] ) / self._f_K[nonzero] ) )
            self._f_K[:] = f_new[:]
            self._pi_i = self._p_step()
            if verbose:
                print "%25d %25.12e" % ( i+1, finc )
            if finc <ftol:
                break
        if finc>=ftol:
            raise NotConvergedWarning( "WHAM", finc )
        self._pi_i /= self._pi_i.sum()

    def _f_step( self ):
        return 1.0 / np.dot( self.gamma_K_i, self.pi_i ) + np.log( self.pi_i.sum() )
    def _p_step( self ):
        return self._N_K_i.sum( axis=0 ) / np.dot( self._N_K_i.sum( axis=1 ) * self._f_K , self.gamma_K_i )

    @property
    def n_therm_states( self ):
        return self._n_therm_states

    @property
    def n_markov_states( self ):
        return self._n_markov_states

    @property
    def pi_i( self ):
        return self._pi_i

    @property
    def f_i( self ):
        return -np.log(self._pi_i)

    @property
    def f_K_i( self ):
        return -np.log(self.pi_K_i)

    @property
    def f_K( self ):
        if self._f_K is None:
            self._f_K = 1.0 / np.dot( self.gamma_K_i, self.pi_i )
        return np.log(self._f_K)

    @property
    def pi_K_i( self ):
        if self._pi_K_i is None:
            self._pi_K_i = self.f_K[:,np.newaxis] * self.pi_i[np.newaxis,:] * self.gamma_K_i
        return self._pi_K_i

    ############################################################################
    #                                                                          #
    #   _b_K_i sanity checks                                                   #
    #                                                                          #
    ############################################################################

    def _check_b_K_i( self, b_K_i ):
        if b_K_i is None:
            raise ExpressionError( "b_K_i", "is None" )
        if not isinstance( b_K_i, (np.ndarray,) ):
            raise ExpressionError( "b_K_i", "invalid type (%s)" % str( type( b_K_i ) ) )
        if 2 != b_K_i.ndim:
            raise ExpressionError( "b_K_i", "invalid number of dimensions (%d)" % b_K_i.ndim )
        if b_K_i.shape[0] != self.n_therm_states:
            raise ExpressionError( "b_K_i", "unmatching number of thermodynamic states (%d,%d)" % (b_K_i.shape[0], self.n_therm_states) )
        if b_K_i.shape[1] != self.n_markov_states:
            raise ExpressionError( "b_K_i", "unmatching number of markov states (%d,%d)" % (b_K_i.shape[1], self.n_markov_states) )
        if np.float64 != b_K_i.dtype:
            raise ExpressionError( "b_K_i", "invalid dtype (%s)" % str( b_K_i.dtype ) )
        return True

    ############################################################################
    #                                                                          #
    #   gamma_K_i getter and setter                                            #
    #                                                                          #
    ############################################################################

    @property
    def gamma_K_i( self ):
        return self._gamma_K_i

    @gamma_K_i.setter
    def gamma_K_i( self, b_K_i ):
        self._gamma_K_i = None
        if self._check_b_K_i( b_K_i ):
            self._gamma_K_i = np.exp( b_K_i.min() - b_K_i )

