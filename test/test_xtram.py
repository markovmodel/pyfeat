################################################################################
#
#   test_xtram.py - testing the pyfeat xtram class
#
#   author: Christoph Wehmeyer <christoph.wehmeyer@fu-berlin.de>
#   author: Antonia Mey <antonia.mey@fu-berlin.de>
#
################################################################################

from nose.tools import assert_raises, assert_true
from pyfeat.estimator import XTRAM
from pytram import ExpressionError, NotConvergedWarning
import numpy as np

#XTRAM testing
def test_expression_error_None():
    assert_raises( ExpressionError, XTRAM, np.ones( shape =(2,3,3), dtype=np.intc), None, np.ones( shape =(10), dtype=np.intc), np.ones( shape =(10), dtype=np.intc),np.ones( shape =(2,3), dtype=np.intc) )
    assert_raises( ExpressionError, XTRAM, np.ones( shape =(2,3,3), dtype=np.intc), np.ones( shape =(2,10), dtype=np.float64 ),None, np.ones( shape =(10), dtype=np.intc), np.ones( shape =(2,3), dtype=np.intc) )
    assert_raises( ExpressionError, XTRAM, np.ones( shape =(2,3,3), dtype=np.intc), np.ones( shape =(2,10), dtype=np.float64), np.ones( shape =(10), dtype=np.intc),None, np.ones( shape =(2,3), dtype=np.intc) )
    assert_raises( ExpressionError, XTRAM, np.ones( shape =(2,3,3), dtype=np.intc), np.ones( shape =(2,10), dtype=np.float64), np.ones( shape =(10), dtype=np.intc),np.ones( shape =(10), dtype=np.intc), None )

def test_expression_error_dim():
    assert_raises( ExpressionError, XTRAM, np.ones( shape =(2,3), dtype=np.intc), np.ones( shape =(2,10), dtype=np.float64 ), np.ones( shape =(10), dtype=np.intc ),np.ones( shape =(10), dtype=np.intc), np.ones( shape =(2,3), dtype=np.intc) )
    assert_raises( ExpressionError, XTRAM, np.ones( shape =(2,3,3), dtype=np.intc), np.ones( shape =(10), dtype=np.float64 ), np.ones( shape =(10), dtype=np.intc ),np.ones( shape =(10), dtype=np.intc), np.ones( shape =(2,3), dtype=np.intc) )
    assert_raises( ExpressionError, XTRAM, np.ones( shape =(2,3,3), dtype=np.intc), np.ones( shape =(2,10), dtype=np.float64 ), np.ones( shape =(10), dtype=np.intc ),np.ones( shape =(10), dtype=np.intc), np.ones( shape =(3), dtype=np.intc) )

def test_expression_error_markov():
    assert_raises( ExpressionError, XTRAM, np.ones( shape =(2,3,3), dtype=np.intc), np.ones( shape =(2,10), dtype=np.float64), np.ones( shape =(10), dtype=np.intc),np.ones( shape =(10), dtype=np.intc), np.ones( shape =(2,4), dtype=np.intc) )
def test_expression_error_therm():
    assert_raises( ExpressionError, XTRAM, np.ones( shape =(2,3,3), dtype=np.intc), np.ones( shape =(3,10), dtype=np.float64), np.ones( shape =(10), dtype=np.intc),np.ones( shape =(10), dtype=np.intc), np.ones( shape =(2,3), dtype=np.intc) )
    assert_raises( ExpressionError, XTRAM, np.ones( shape =(2,3,3), dtype=np.intc), np.ones( shape =(2,10), dtype=np.float64), np.ones( shape =(10), dtype=np.intc),np.ones( shape =(10), dtype=np.intc), np.ones( shape =(3,4), dtype=np.intc) )
















