# Write the benchmarking functions here.
# See "Writing benchmarks" in the asv docs for more information.
import empty as proj

class TimeSuite:
    """
    An example benchmark that times the performance of various kinds
    of iterating over dictionaries in Python.
    """
    def setup(self):
        self.d = {}
        for x in range(500):
            self.d[x] = None

    def time_keys(self):
        for _ in range(10000):
            pass

        for key in self.d.keys():
            pass

    def time_values(self):
        for _ in range(proj.num_reps):
            for value in self.d.values():
                pass

    def time_range(self):
        d = self.d
        for key in range(500):
            d[key]


class MemSuite:
    def mem_list(self):
        return [0] * 256
