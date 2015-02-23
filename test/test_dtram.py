################################################################################
#
#   test_dtram.py - testing the pyfeat dtram class
#
#   author: Christoph Wehmeyer <christoph.wehmeyer@fu-berlin.de>
#
################################################################################

from nose.tools import assert_raises, assert_true
from pyfeat.estimator import DTRAM
from pytram import ExpressionError, NotConvergedWarning
import numpy as np

#DTRAM testing
def test_expression_error_None():
    assert_raises( ExpressionError, DTRAM, np.ones( shape=(2,3,3), dtype=np.intc ), None )
def test_expression_error_int():
    assert_raises( ExpressionError, DTRAM, np.ones( shape=(2,3,3), dtype=np.intc ), 5 )
def test_expression_error_list():
    assert_raises( ExpressionError, DTRAM, np.ones( shape=(2,3,3), dtype=np.intc ), [1,2] )
def test_expression_error_dim():
    assert_raises( ExpressionError, DTRAM, np.ones( shape=(2,3,3), dtype=np.intc ), np.ones( shape=(2,2,2), dtype=np.float64 ) )
def test_expression_error_markov():
    assert_raises( ExpressionError, DTRAM, np.ones( shape=(2,3,3), dtype=np.intc ), np.ones( shape=(2,2), dtype=np.float64 ) )
def test_expression_error_therm():
    assert_raises( ExpressionError, DTRAM, np.ones( shape=(2,3,3), dtype=np.intc ), np.ones( shape=(1,3), dtype=np.float64 ) )
def test_expression_error_int16():
    assert_raises( ExpressionError, DTRAM, np.ones( shape=(2,3,3), dtype=np.intc ), np.ones( shape=(2,3), dtype=np.int16 ) )
def test_expression_error_float32():
    assert_raises( ExpressionError, DTRAM, np.ones( shape=(2,3,3), dtype=np.intc ), np.ones( shape=(2,3), dtype=np.float32 ) )

















