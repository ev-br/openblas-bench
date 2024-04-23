import numpy as np
from openblas_bench import dgemm

class BlasL3:

    params = [10, 100]

    def setup(self, n):
        print(f"setup {n = }")
        rndm = np.random.RandomState(1234)
        self.a = np.asarray(rndm.uniform(size=(n, n)), dtype=float, order='F')
        self.b = np.asarray(rndm.uniform(size=(n, n)), dtype=float, order='F')
        self.c = np.empty((n, n), dtype=float, order='F')
    
    def time_gemm(self, n):
        a, b, c = self.a, self.b, self.c
        result = dgemm(1.0, a, b, c=c, overwrite_c=True)
        assert result is c
