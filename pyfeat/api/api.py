r"""

==========================
API for the pyfeat package
==========================

.. moduleauthor:: Antonia Mey <antonia.mey@fu-berlin.de>
.. moduleauthor:: Christoph Wehmeyer <christoph.wehmeyer@fu-berlin.de>

"""

from ..wham import WHAM
from pytram import NotConvergedWarning, ExpressionError



########################################################################
#                                                                      #
#   WHAM API function using the mathematical expressions at input      #
#                                                                      #
########################################################################

def wham_me( N_K_i, b_K_i, maxiter=100, ftol=1.0E-5, verbose=False ):
    r"""
    The WHAM API function
    
    Parameters
    ----------
    N_K_i : numpy.ndarray( shape=(T,M), dtype=numpy.float64 )
        total number of counts from simulation at T in M discrete Markov state (bin)
    b_K_i : numpy.ndarray( shape=(T,M), dtype=numpy.float64 )
        reduced bias energies at the T thermodynamic and M discrete Markov states
    maxiter : int
        maximum number of self-consistant iteration steps during the optimisation of the stationary probabilities
    ftol : float (> 0.0)
        convergence criterion based on the max relative change in an self-consistent-iteration step
    verbose : boolean
        writes convergence information to stdout during the self-consistent-iteration cycle
    
    Returns
    -------
    wham_obj : object
        WHAM estimator object with optimised unbiased stationary probabilities
    """
    # try to create the WHAM object
    try:
        wham_obj = WHAM( N_K_i, b_K_i )
    except ExpressionError, e:
        print "# ERROR ############################################################################"
        print "# Your input was faulty!"
        print "# The < %s > object is malformed: %s" % ( e.expression, e.msg )
        print "# ABORTING #########################################################################"
        raise
    # try to converge the stationary probabilities
    try:
        wham_obj.sc_iteration( maxiter=maxiter, ftol=ftol, verbose=verbose )
    except NotConvergedWarning, e:
        print "# WARNING ##########################################################################"
        print "# WHAM did not converge within %d steps!" % maxiter
        print "# The last relative increment was %.6e." % e.relative_increment
        print "# You should run the < sc_iteration > method again."
        print "# USE RESULTS WITH CARE ############################################################"
    finally:
        return wham_obj

    
def wham( forge, maxiter=100, ftol=1.0E-5, verbose=False ):
    r"""
    The WHAM API function
    
    Parameters
    ----------
    forge : object
        data forge or container for pyfeat input data
    maxiter : int
        maximum number of SC iteration steps during the optimisation of the stationary probabilities
    ftol : float (> 0.0)
        convergence criterion based on the max relative change in an self-consistent-iteration step
    verbose : boolean
        writes convergence information to stdout during the self-consistent-iteration cycle
    
    Returns
    -------
    wham_obj : object
        wham estimator object with optimised unbiased stationary probabilities
    """
    return wham_me( forge.N_K_i, forge.b_K_i, maxiter=maxiter, ftol=ftol, verbose=verbose )
    
