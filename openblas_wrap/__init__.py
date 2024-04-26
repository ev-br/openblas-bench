"""
Empty dummy proj
"""

__version__ = "0.1"  


num_reps = 8


#from scipy.linalg.blas import (
from ._flapack import (
    # level 1
    scipy_dnrm2 as dnrm2,
    scipy_ddot as ddot,
    scipy_daxpy as daxpy,
    # level 3
    scipy_dgemm as dgemm,
    scipy_dsyrk as dsyrk,
)

#from scipy.linalg.lapack import (
from ._flapack import (
    # linalg.solve
    scipy_dgesv as dgesv
)
