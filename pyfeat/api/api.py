r"""

==========================
API for the pyfeat package
==========================

.. moduleauthor:: Antonia Mey <antonia.mey@fu-berlin.de>
.. moduleauthor:: Christoph Wehmeyer <christoph.wehmeyer@fu-berlin.de>

"""

from ..estimator import WHAM, XTRAM, DTRAM, TRAM #, MBAR
from pytram import NotConvergedWarning, ExpressionError
from ..reader import Reader
from ..forge import Forge



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
        convergence criterion based on the max change in an self-consistent-iteration step
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
        print "# The last increment was %.6e." % e.increment
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
        convergence criterion based on the max change in an self-consistent-iteration step
    verbose : boolean
        writes convergence information to stdout during the self-consistent-iteration cycle

    Returns
    -------
    wham_obj : object
        wham estimator object with optimised unbiased stationary probabilities
    """
    return wham_me( forge.N_K_i, forge.b_K_i, maxiter=maxiter, ftol=ftol, verbose=verbose )

########################################################################
#                                                                      #
#   dTRAM API function using the mathematical expressions at input     #
#                                                                      #
########################################################################

def dtram_me( C_K_ij, b_K_i, maxiter = 100, ftol = 1.0e-10, verbose = False ):
    r"""
    Parameters
    ----------
    C_K_ij : numpy.ndarray( shape=(T,M,M), dtype=numpy.intc )
        transition counts between the M discrete Markov states for each of the T thermodynamic ensembles
    b_K_i : numpy.ndarray( shape=(T,M), dtype=numpy.float64 )
        bias energies in the T thermodynamic and M discrete Markov states
    Returns:
    -------
    dtram_obj : obj
        dtram estimator object with optimised stationary properties

    """

    # try to create the DTRAM object
    try:
        dtram_obj = DTRAM( C_K_ij, b_K_i )
    except ExpressionError, e:
        print "# ERROR ############################################################################"
        print "# Your input was faulty!"
        print "# The < %s > object is malformed: %s" % ( e.expression, e.msg )
        print "# ABORTING #########################################################################"
        raise
    # try to converge the stationary probabilities
    try:
        dtram_obj.sc_iteration( maxiter=maxiter, ftol=ftol, verbose=verbose )
    except NotConvergedWarning, e:
        print "# WARNING ##########################################################################"
        print "# dTRAM did not converge within %d steps!" % maxiter
        print "# The last increment was %.6e." % e.increment
        print "# You should run the < sc_iteration > method again."
        print "# USE RESULTS WITH CARE ############################################################"
    return dtram_obj


########################################################################
#                                                                      #
#   dTRAM API function                                                 #
#                                                                      #
########################################################################

def dtram( forge, lag = 1,  maxiter=100, ftol=1.0e-10, verbose= False ):
    r"""
    Parameters
    ----------
    forge : object
        data forge or container for pyfeat input data
    lag : int
        lagtime at which the countmatrix is estimated
    maxiter : int
        maximum number of SC iteration steps during the optimisation of the stationary probabilities
    ftol : float (> 0.0)
        convergence criterion based on the max change in an self-consistent-iteration step
    verbose : boolean
        writes convergence information to stdout during the self-consistent-iteration cycle
    
    Returns
    -------
    dtram_obj : object
        dtram estimator object with optimised stationary properties
    """
    return dtram_me( forge.get_C_K_ij( lag), forge.b_K_i, maxiter = maxiter, ftol = ftol, verbose = verbose )
    
########################################################################
#                                                                      #
#   MBAR API function using the mathematical expressions at input      #
#                                                                      #
########################################################################
#def mbar_me( b_IK_x, M_I_x, N_K, maxiter=1000, ftol=1.0e-10, verbose=False ):
#    r"""
#    Parameters
#    ----------
#    b_IK_x : numpy.ndarray( shape=(T,M,M), dtype=numpy.intc )
#        transition counts between the M discrete Markov states for each of the T thermodynamic ensembles
#    M_I_x : numpy.ndarray( shape=(T,M), dtype=numpy.float64 )
#        bias energies in the T thermodynamic and M discrete Markov states
#    N_K : numpy.ndarray( shape=(T), dtype=numpy.float64 )
#        number of samples at each thermodynamic state T
#    maxiter : int
#        maximum number of SC iteration steps during the optimisation of the stationary probabilities
#    ftol : float (> 0.0)
#        convergence criterion based on the max relative change in an self-consistent-iteration step
#    verbose : boolean
#        writes convergence information to stdout during the self-consistent-iteration cycle
#    Returns:
#    -------
#    mbar_obj : obj
#        mbar estimator object with optimised stationary properties
#    """
#    # try to create the MBAR object
#    try:
#        mbar_obj = MBAR( b_IK_x, M_I_x, N_K )
#    except ExpressionError, e:
#        print "# ERROR ############################################################################"
#        print "# Your input was faulty!"
#        print "# The < %s > object is malformed: %s" % ( e.expression, e.msg )
#        print "# ABORTING #########################################################################"
#        raise
#    # try to converge the stationary probabilities
#    try:
#        mbar_obj.sc_iteration( maxiter=maxiter, ftol=ftol, verbose=verbose )
#    except NotConvergedWarning, e:
#        print "# WARNING ##########################################################################"
#        print "# WHAM did not converge within %d steps!" % maxiter
#        print "# The last relative increment was %.6e." % e.relative_increment
#        print "# You should run the < sc_iteration > method again."
#        print "# USE RESULTS WITH CARE ############################################################"
#    finally:
#        return mbar_obj


########################################################################
#                                                                      #
#   MBAR API function                                                  #
#                                                                      #
########################################################################
#def mbar( forge, maxiter = 1000, ftol = 1.0e-10, verbose = False ):
#    r"""
#    Parameters
#    ----------
#    forge : object
#        data forge or container for pyfeat input data
#    maxiter : int
#        maximum number of SC iteration steps during the optimisation of the stationary probabilities
#    ftol : float (> 0.0)
#        convergence criterion based on the max relative change in an self-consistent-iteration step
#    verbose : boolean
#        writes convergence information to stdout during the self-consistent-iteration cycle
#    Returns
#    -------
#    mbar_obj : object
#        mbar estimator object with optimised stationary properties
#    """
#    return mbar_me( forge.b_IK_x, forge.M_K_x, forge.N_K, maxiter=maxiter, ftol=ftol, verbose=verbose )

 
########################################################################
#                                                                      #
#   xTRAM API function using the mathematical expressions as input     #
#                                                                      #
########################################################################

def xtram_me( C_K_ij, b_K_x, T_x, M_x, N_K_i, maxiter = 100, ftol = 1.0e-10, verbose = False ):
    r"""
    C_K_ij : numpy.ndarray( shape=(T,M,M), dtype=numpy.intc )
        transition counts between the M discrete Markov states for each of the T thermodynamic ensembles
    b_K_x : numpy.ndarray( shape=(T,N), dtype=numpy.float64 )
        Biasing tensor
    T_x : numpy.ndarray( shape=(N), dtype=numpy.intc )
        Thermodynamic state trajectory
    M_x : numpy.ndarray( shape=(N), dtype=numpy.intc )
        Markov state trajectories
    N_K_i : numpy.ndarray( shape=(T,M), dtype=numpy.intc )
        Number of markov samples in each thermodynamic state
    """

    # try to create the XTRAM object
    try:
        xtram_obj = XTRAM( C_K_ij, b_K_x, T_x, M_x, N_K_i )
    except ExpressionError, e:
        print "# ERROR ############################################################################"
        print "# Your input was faulty!"
        print "# The < %s > object is malformed: %s" % ( e.expression, e.msg )
        print "# ABORTING #########################################################################"
        raise
    # try to converge the stationary probabilities
    try:
        xtram_obj.sc_iteration( maxiter=maxiter, ftol=ftol, verbose=verbose )
    except NotConvergedWarning, e:
        print "# WARNING ##########################################################################"
        print "# WHAM did not converge within %d steps!" % maxiter
        print "# The last increment was %.6e." % e.increment
        print "# You should run the < sc_iteration > method again."
        print "# USE RESULTS WITH CARE ############################################################"
    finally:
        return xtram_obj


########################################################################
#                                                                      #
#   xTRAM API function                                                 #
#                                                                      #
########################################################################

def xtram( forge, lag = 1, maxiter=100, ftol=1.0e-10, verbose= False ):
    r"""
    Parameters
    ----------
    forge : object
        data forge or container for pyfeat input data
    lag : int
        lagtime at which the countmatrix is estimated
    maxiter : int
        maximum number of SC iteration steps during the optimisation of the stationary probabilities
    ftol : float (> 0.0)
        convergence criterion based on the max change in an self-consistent-iteration step
    verbose : boolean
        writes convergence information to stdout during the self-consistent-iteration cycle

    Returns
    -------
    xtram_obj : object
        xtram estimator object with optimised stationary properties
    """
    return xtram_me( forge.get_C_K_ij( lag ), forge.b_K_x, forge.T_x, forge.M_x, forge.N_K_i, maxiter = maxiter, ftol = ftol, verbose = verbose )


########################################################################
#                                                                      #
#   TRAM API function using the mathematical expressions at input     #
#                                                                      #
########################################################################
def tram_me():
    raise NotImplementedError('tram_me function has not been implemented yet')

########################################################################
#                                                                      #
#   TRAM API function                                                 #
#                                                                      #
########################################################################
def tram():
    raise NotImplementedError('TRAM API function has not been implemented yet')


########################################################################
#                                                                      #
#   Forge API function                                                 #
#                                                                      #
########################################################################    
    
def convert_data( trajs, b_K_i=None, kT_K=None, kT_target=None ):
    r"""
    API function for creating the data forge object which will then be used for the estimators

    Parameters
    ----------
    trajs : list of dictionaries
        simulation trajectories
    b_K_i : numpy.ndarray( shape=(T,M), dtype=numpy.float64 )
        reduced bias energies at the T thermodynamic and M discrete Markov states
    kT_K : numpy.nparray( shape=(T), dtype=numpy.float64 )
        list of kT values of each thermodynamic state
    kT_target : int
        target thermodynamic state for which pi_i and f_i will be computed

    Returns
    -------
    forge : pyfeat.Forge object
        container holding all data
    """
    forge = Forge( trajs, b_K_i, kT_K, kT_target)
    return forge

########################################################################
#                                                                      #
#   Reader API function                                                #
#                                                                      #
########################################################################

def read_files (files, b_K_i_file=None, kT_file=None, skiprows=0, maxlength=None, verbose=False ):
    r"""
    API function for reading files 
    
    Parameters
    ----------
    files : list of strings
        file names to read
    b_K_i_file : string (optional)
        file name for discrete estimator data
    kT_file : string (optional)
        file name for kT value listing
    skiprows : int (optional)
        specify the number of skipped lines when reading the trajectory files
    maxlength : int (optional)
        maximum number of data points read from file
    verbose : boolean (optional)
        verbose output during the reading/building process

    Returns
    -------
    reader : pyfeat.Reader object
    	augmented trajectory information to be passed to the forge
    """
    reader = Reader(files, b_K_i_file, kT_file, skiprows, maxlength, verbose)
    return reader 
    
