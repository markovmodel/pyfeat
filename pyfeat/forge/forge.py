r"""

==============
Data container
==============

.. moduleauthor:: Antonia Mey <antonia.mey@fu-berlin.de>, Christoph Wehmeyer <christoph.wehmeyer@fu-berlin.de>

"""

import pytram as pt
import numpy as np

class Forge( pt.TRAMData ):
    """I am the data forge
    
    """
    def __init__( self, trajs, b_K_i=None, kT_K=None, kT_target=None, verbose = False ):
        super( Forge, self ).__init__( trajs, b_K_i=b_K_i, kT_K=kT_K, kT_target=kT_target, verbose = verbose )
    
    
