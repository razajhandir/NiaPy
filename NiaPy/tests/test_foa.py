# pylint: disable=old-style-class, line-too-long
from NiaPy.tests.test_algorithm import AlgorithmTestCase, MyBenchmark
from NiaPy.algorithms.basic import ForestOptimizationAlgorithm

class FOATestCase(AlgorithmTestCase):

    def test_type_parameters(self):
        tp = ForestOptimizationAlgorithm.typeParameters()
        self.assertTrue(tp['NP'](1))
        self.assertFalse(tp['NP'](0))
        self.assertFalse(tp['NP'](-1))
        self.assertFalse(tp['NP'](1.0))
        self.assertTrue(tp['lt'](1))
        self.assertFalse(tp['lt'](0))
        self.assertFalse(tp['lt'](-1))
        self.assertFalse(tp['lt'](1.0))
        self.assertTrue(tp['al'](1))
        self.assertFalse(tp['al'](0))
        self.assertFalse(tp['al'](-1))
        self.assertFalse(tp['al'](1.0))
        self.assertTrue(tp['lsc'](1))
        self.assertFalse(tp['lsc'](0))
        self.assertFalse(tp['lsc'](-1))
        self.assertFalse(tp['lsc'](1.0))
        self.assertTrue(tp['gsc'](1))
        self.assertFalse(tp['gsc'](0))
        self.assertFalse(tp['gsc'](-1))
        self.assertFalse(tp['gsc'](1.0))
        self.assertTrue(tp['tr'](1))
        self.assertTrue(tp['tr'](0.5))
        self.assertTrue(tp['tr'](0))
        self.assertFalse(tp['tr'](-1))
        self.assertFalse(tp['tr'](1.1))

    def test_works_fine(self):
        foa = ForestOptimizationAlgorithm(D=self.D, NP=20, nFES=self.nFES, nGEN=self.nGEN, lt=5, lsc=1, gsc=1, al=20, tr=0.35, benchmark=MyBenchmark(), seed=self.seed)
        foac = ForestOptimizationAlgorithm(D=self.D, NP=20, nFES=self.nFES, nGEN=self.nGEN, lt=5, lsc=1, gsc=1, al=20, tr=0.35, benchmark=MyBenchmark(), seed=self.seed)
        AlgorithmTestCase.algorithm_run_test(self, foa, foac)

    def test_griewank_works_fine(self):
        foa_griewank = ForestOptimizationAlgorithm(D=self.D, NP=20, nFES=self.nFES, nGEN=self.nGEN, lt=5, lsc=1, gsc=1, al=20, tr=0.35, benchmark='griewank', seed=self.seed)
        foa_griewankc = ForestOptimizationAlgorithm(D=self.D, NP=20, nFES=self.nFES, nGEN=self.nGEN, lt=5, lsc=1, gsc=1, al=20, tr=0.35, benchmark='griewank', seed=self.seed)
        AlgorithmTestCase.algorithm_run_test(self, foa_griewank, foa_griewankc)
