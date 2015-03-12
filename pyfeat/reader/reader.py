r"""
======
Reader
======

.. moduleauthor:: Antonia Mey <antonia.mey@fu-berlin.de>

"""

import pytram as pt
import numpy as np

class Reader( pt.Reader ):
    """I am the pyfeat reader and read all trajectory information
    """
    def __init__( self, files, b_K_i_file=None, kT_file=None, skiprows=0, maxlength=None, verbose=False ):
        super( Reader, self ).__init__( files, b_K_i_file=b_K_i_file, kT_file=kT_file, skiprows=skiprows, maxlength=maxlength, verbose=verbose )
