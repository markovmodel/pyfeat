#!/usr/bin/env python

####################################################################################################
#                                                                                                  #
#   RUN SCRIPT FOR THE ALL ESTIMATORS IN THE PYFEATPACKAGE                                         #
#                                                                                                  #
#    author: Antonia Mey <antonia.mey@fu-berlin.de>                                                #
#    author: Christoph Wehmeyer <christoph.wehmeyer@fu-berlin.de>                                  #
#                                                                                                  #
####################################################################################################



####################################################################################################
#
#   IMPORTS
#
####################################################################################################

from pyfeat import Reader, Forge
from pyfeat.estimator import WHAM, XTRAM, DTRAM
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
            help='pyfeat compatible files for evaluation (trajectory files)',
            nargs='*',
            metavar='FILE'
        )
    parser.add_argument(
            '--estimator',
            help='specify an available estimator choices are: XTRAM, DTRAM, WHAM',
            default='WHAM',
            metavar='STR'
        )
    parser.add_argument(
            "--b_K_i_file",
            help="specify a pytram compatible file containing kT information",
            default=None,
            metavar="FILE"
        )
    parser.add_argument(
            "--kT_file",
            help="specify a pytram compatible file containing kT information",
            default=None,
            metavar="FILE"
        )
    parser.add_argument(
            "--kT_target",
            help="The kT value for which the free energy and probabilities should be calculated",
            type=int,
            default=None,
            metavar='INT'
        )
    parser.add_argument(
            "--lag",
            help="specify a lag time for evaluation",
            type=int,
            default=1,
            metavar='INT'
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
            default=100,
            metavar='INT'
        )
    parser.add_argument(
            "--ftol",
            help="limit the requested convergence level",
            type=float,
            default=1.0E-5,
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
    #   check estimator consistancy
    #
    ############################################################################
    if args.estimator == 'DTRAM' or args.estimator == 'WHAM':
        if args.b_K_i_file is None:
            print "Error: you must set the --b_K_i_file option, with %s as your estimator choice!" %args.estimator
            exit( 1 )

    ############################################################################
    #
    #   write header
    #
    ############################################################################
    print "\n\n###################################### PYFEAT ######################################"
    print "#\n#                          Invoking the %s estimator" %args.estimator
    print "#\n### PARAMETERS\n#"
    print "# %25s %24d" % ( "[--lag]", args.lag )
    print "# %25s %24d" % ( "[--maxiter]", args.maxiter )
    print "# %25s %24.5e" % ( "[--ftol]", args.ftol )



    ############################################################################
    #
    #   import the data and initialize the estimator
    #
    ############################################################################
    print "#\n################################## IMPORTING DATA ##################################\n#"
    reader = None
    forge = None
    estimator = None
    if args.estimator == 'DTRAM' or args.estimator == 'WHAM':
        reader = Reader(
            args.files,
            b_K_i_file=args.b_K_i_file,
            maxlength=args.maxlength,
            skiprows=args.skiprows,
            verbose=True
            )
        forge = Forge( reader.trajs, b_K_i = reader.b_K_i)
        if args.estimator == 'WHAM':
            print "#\n### WARNING\n#"
            print "# You chose an estimator that your input data samples from a global equilibrium and is uncorrelated!"
            print "# Have you subsampled your data appropriately to account for this?"
            print "# Maybe consider using one of the TRAM estimator instead!"
            try:
                estimator = WHAM( forge.N_K_i, forge.b_K_i )
            except ExpressionError, e:
                print "#\n### ERROR\n#"
                print "# Your input was faulty!"
                print "# The < %s > object is malformed: %s" % ( e.expression, e.msg )
                print "#\n### ABORTING\n\n"
                exit( 1 )
        else:
            try:
                estimator = DTRAM( forge.get_C_K_ij(args.lag), forge.b_K_i )
            except ExpressionError, e:
                print "#\n### ERROR\n#"
                print "# Your input was faulty!"
                print "# The < %s > object is malformed: %s" % ( e.expression, e.msg )
                print "#\n### ABORTING\n\n"
                exit( 1 )
    else:
        reader = Reader(
            args.files,
            kT_file=args.kT_file,
            maxlength=args.maxlength,
            skiprows=args.skiprows,
            verbose=True
            )
        forge = Forge( reader.trajs, kT_K=reader.kT_K, kT_target=args.kT_target )
        if args.estimator == 'XTRAM':
            try:
                estimator = XTRAM( forge.get_C_K_ij(args.lag), forge.b_K_x, forge.T_x, forge.M_x, forge.N_K_i, target = forge.kT_target )
            except ExpressionError, e:
                print "#\n### ERROR\n#"
                print "# Your input was faulty!"
                print "# The < %s > object is malformed: %s" % ( e.expression, e.msg )
                print "#\n### ABORTING\n\n"
                exit( 1 )
        elif args.estimator == 'TRAM':
            print "#\n### ERROR\n#"
            print 'TRAM cannot be used yet!'
            exit(1)
        
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
        estimator.sc_iteration( maxiter=args.maxiter, ftol=args.ftol, verbose=args.verbose )
        print "# ... converged!"
    except NotConvergedWarning, e:
        print "#\n### WARNING\n#\n# %s is not converged - use these results carefuly!" %args.estimator
        print "#\n### RECOMMENDATION\n#\n# Run run_pyfeat.py again and increase --maxiter"



    ############################################################################
    #
    #   print out the results
    #
    ############################################################################
    print "#\n##################################### RESULTS ######################################"
    print "#\n### UNBIASED STATIONARY VECTOR\n#"
    print "# %25s %25s" % ( "[markov state]", "[stationary probability]" )
    for i in xrange( estimator.pi_i.shape[0] ):
        print " %25d %25.12e" % ( i, estimator.pi_i[i] )
    print "#\n### UNBIASED FREE ENERGY\n#"
    print "# %25s %25s" % ( "[markov state]", "[reduced free energy]" )
    for i in xrange( estimator.f_i.shape[0] ):
        print " %25d %25.12e" % ( i, estimator.f_i[i] )
    print "#\n### THERMODYNAMIC FREE ENERGY\n#"
    print "# %25s %25s" % ( "[thermodynamic state]", "[reduced free energy]" )
    for i in xrange( estimator.f_K.shape[0] ):
        print " %25d %25.12e" % ( i, estimator.f_K[i] )



    ############################################################################
    #
    #   say good bye
    #
    ############################################################################
    print "#\n###################That's it, now it is time to put the kettle on ##############################\n#"
    print "#\n#                  Thank you for using %s in the pyfeat package!\n#\n#" %args.estimator
    print "### CITATION\n#"
    estimator.cite( pre="#    " )
    print "#\n################################################################################################\n\n"











