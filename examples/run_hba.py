# This is temporary fix to import module from parent folder
# It will be removed when package is published on PyPI
import sys
sys.path.append('../')
# End of fix

import random
import logging
from NiaPy.algorithms.modified import HybridBatAlgorithm

logging.basicConfig()
logger = logging.getLogger('examples')
logger.setLevel('INFO')

# For reproducive results
random.seed(1234)


class MyBenchmark(object):
    def __init__(self):
        self.Lower = -11
        self.Upper = 11

    def function(self):
        def evaluate(D, sol):
            val = 0.0
            for i in range(D):
                val = val + sol[i] * sol[i]
            return val
        return evaluate

for i in range(10):
    Algorithm = HybridBatAlgorithm(
        D=10, NP=40, nFES=10000, A=0.9, r=0.1, F=0.001, CR=0.9, Qmin=0.0, Qmax=2.0, benchmark=MyBenchmark())
    Best = Algorithm.run()
    logger.info(Best)
