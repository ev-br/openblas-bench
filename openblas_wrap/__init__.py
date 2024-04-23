"""
Empty dummy proj
"""

__version__ = "0.1"  


num_reps = 8


from scipy.linalg.blas import (
    # level 1
    dnrm2,
    ddot,
    daxpy,
    # level 3
    dgemm, dsyrk,
)

from scipy.linalg.lapack import (
    # linalg.solve
    dgesv
)
