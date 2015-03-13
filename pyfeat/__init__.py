__version__='0.3.0'
# raise the Reader class onto the pyfeat package level
from .reader import Reader

# raise the Forge class onto the pyfeat package level
from .forge import Forge

#raise API functions onto package level
from .api import xtram, xtram_me, dtram, dtram_me, wham, wham_me, read_files, convert_data
