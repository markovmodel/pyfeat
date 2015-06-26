r"""
======
Reader
======

.. moduleauthor:: Antonia Mey <antonia.mey@fu-berlin.de>

"""

import pytram as pt


class Reader(pt.Reader):
    """I am the pyfeat reader and read all trajectory information
    """
    def __init__(self,
                 files,
                 b_K_i_file=None,
                 kT_file=None, skiprows=0,
                 maxlength=None,
                 verbose=False):
        r"""Reader, reads file provided in pyfeat format
        Parameters
        ----------

        files : list of strings
             list of strings with filenames compatible with pyfeat
        b_K_i_file : string
             sting for the filename of the bias matrix file
        kT_file : string
             string for the filename of the reduced tempeature file
        maxlength : int
             maximum number of files that should be read
        verbose : boolean
            Prints useful output of what the reader is doing
        """
        super(Reader, self).__init__(files,
                                     b_K_i_file=b_K_i_file,
                                     kT_file=kT_file,
                                     skiprows=skiprows,
                                     maxlength=maxlength,
                                     verbose=verbose)
