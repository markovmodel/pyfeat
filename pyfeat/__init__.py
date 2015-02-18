__version__='0.3.0'
# raise the Reader class onto the pyfeat package level
from .reader import Reader

# raise the Forge class onto the pyfeat package level
from .forge import Forge

# raise WHAM class onto pyfeat package leve
from .estimator import WHAM

# raise WHAM class onto pyfeat package leve
from .estimator import XTRAM

# raise the API function onto the pyfeat package level
from .api import wham, wham_me
