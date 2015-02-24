#!/usr/bin/env python

####################################################################################################
#                                                                                                  #
#   RUN SCRIPT FOR THE WHAM METHOD WITHIN THE PYTRAM package                                      #
#                                                                                                  #
#    author: Christoph Wehmeyer <christoph.wehmeyer@fu-berlin.de>                                  #
#    author: Antonia Mey <antonia.mey@fu-berlin.de>                                                #
#                                                                                                  #
####################################################################################################



####################################################################################################
#
#   IMPORTS
#
####################################################################################################

from pyfeat import Reader, Forge
from pyfeat.estimator import WHAM
from pytram import ExpressionError, NotConvergedWarning
from argparse import ArgumentParser, FileType
from sys import exit
import numpy as np



####################################################################################################
#
#   MAIN PART
#
####################################################################################################

if '__main__' == __name__:

    ############################################################################
    #
    #   capture the command line arguments
    #
    ############################################################################
    parser = ArgumentParser()
    parser.add_argument(
            'files',
            help='pytram compatible files for evaluation (trajectory files)',
            nargs='*',
            metavar='FILE'
        )
    parser.add_argument(
            "--b_K_i_file",
            help="specify a pytram compatible file containing kT information",
            metavar="FILE"
        )
    parser.add_argument(
            "--maxlength",
            help="limit the number of trajectory frames",
            type=int,
            default=None,
            metavar='INT'
        )
    parser.add_argument(
            "--skiprows",
            help="Number of initial frames skipped",
            type=int,
            default=0,
            metavar='INT'
        )
    parser.add_argument(
            "--maxiter",
            help="limit the number of fixed point iterations",
            type=int,
            default=1000,
            metavar='INT'
        )
    parser.add_argument(
            "--ftol",
            help="limit the requested convergence level",
            type=float,
            default=1.0E-10,
            metavar='FLOAT'
        )
    parser.add_argument(
            "--verbose",
            help="show the progress during the self-consistent-iteration",
            action='store_true'
        )
    args = parser.parse_args()



    ############################################################################
    #
    #   check mandatory command line arguments
    #
    ############################################################################
    if 1 > len( args.files ):
        print "ERROR: you must give at least one pytram compatible trajectory file!"
        exit( 1 )


    ############################################################################
    #
    #   write header
    #
    ############################################################################
    print "\n\n###################################### PYFEAT ######################################"
    print "#\n#                          Invoking the wham estimator"
    print "#\n### PARAMETERS\n#"
    print "# %25s %24d" % ( "[--maxiter]", args.maxiter )
    print "# %25s %24.5e" % ( "[--ftol]", args.ftol )



    ############################################################################
    #
    #   import the data
    #
    ############################################################################
    print "#\n################################## IMPORTING DATA ##################################\n#"
    reader = Reader(
            args.files,
            b_K_i_file=args.b_K_i_file,
            maxlength=args.maxlength,
            skiprows=args.skiprows,
            verbose=True
        )
    forge = Forge( reader.trajs, b_K_i = reader.b_K_i)
    try:
        wham_obj = WHAM( forge.N_K_i, forge.b_K_i )
    except ExpressionError, e:
        print "#\n### ERROR\n#"
        print "# Your input was faulty!"
        print "# The < %s > object is malformed: %s" % ( e.expression, e.msg )
        print "#\n### ABORTING\n\n"
        exit( 1 )
    print "#\n### SYSTEM INFORMATION\n#"
    print "# %25s %24d" % ( "[markov states]", forge.n_markov_states )
    print "# %25s %24d" % ( "[thermodynamic states]", forge.n_therm_states )



    ############################################################################
    #
    #   run the self-consistent-iteration
    #
    ############################################################################
    print "#\n#################################### RUN WHAM #####################################\n#"
    try:
        print "# Run self-consistent-iteration"
        wham_obj.sc_iteration( maxiter=args.maxiter, ftol=args.ftol, verbose=args.verbose )
        print "# ... converged!"
    except NotConvergedWarning, e:
        print "#\n### WARNING\n#\n# wham is not converged - use these results carefuly!"
        print "#\n### RECOMMENDATION\n#\n# Run wham.py again and increase --maxiter"



    ############################################################################
    #
    #   print out the results
    #
    ############################################################################
    print "#\n##################################### RESULTS ######################################"
    print "#\n### UNBIASED STATIONARY VECTOR\n#"
    print "# %25s %25s" % ( "[markov state]", "[stationary probability]" )
    for i in xrange( wham_obj.pi_i.shape[0] ):
        print " %25d %25.12e" % ( i, wham_obj.pi_i[i] )
    print "#\n### UNBIASED FREE ENERGY\n#"
    print "# %25s %25s" % ( "[markov state]", "[reduced free energy]" )
    for i in xrange( wham_obj.f_i.shape[0] ):
        print " %25d %25.12e" % ( i, wham_obj.f_i[i] )
    print "#\n### THERMODYNAMIC FREE ENERGY\n#"
    print "# %25s %25s" % ( "[thermodynamic state]", "[reduced free energy]" )
    for i in xrange( wham_obj.f_K.shape[0] ):
        print " %25d %25.12e" % ( i, wham_obj.f_K[i] )



    ############################################################################
    #
    #   say good bye
    #
    ############################################################################
    print "#\n###################That's it, now it is time to put the kettle on ##############################\n#"
    print "#\n#                  Thank you for using wham in the pyfeat package!\n#\n#"
    print "#\n################################################################################################\n\n"











