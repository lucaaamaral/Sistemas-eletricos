import unittest
from math import sqrt
from lib.PhaseToComplex import PhaseToComplex
from lib.ComplexToPhase import ComplexToPhase
from lib.TensaoFase import TensaoFase
from lib.FaseLinha import FaseLinha
from lib.Correntes import Correntes
import lib.DeltaEstrela as DeltaEstrela
import lib.EstrelaDelta as EstrelaDelta
import lib.TensaoNeutro as TensaoNeutro

class TestBase(unittest.TestCase):

    def test_0_PhaseToComplex(self):
        ans:complex = PhaseToComplex(100, 0)
        ans = complex(
            round(ans.real, 11),
            round(ans.imag, 11)
            )
        self.assertEqual(ans, 100+0j)

        ans = PhaseToComplex(100, 120)
        ans = complex(
            round(ans.real, 11),
            round(ans.imag, 11)
            )
        self.assertEqual(ans, -50.0+86.60254037844j)

    def test_1_ComplexToPhase(self):

        ans = ComplexToPhase(PhaseToComplex(100, 0))
        ans = ( round(ans[0], 11), round(ans[1], 11) )
        self.assertEqual(ans, (100,0))

        ans = ComplexToPhase(PhaseToComplex(100, 120))
        ans = ( round(ans[0], 11), round(ans[1], 11) )
        self.assertEqual(ans, (100, 120))

        ans = ComplexToPhase(PhaseToComplex(100, 240))
        ans = ( round(ans[0], 11), round(ans[1], 11) )
        self.assertEqual(ans, (100, 240))

    def test_2_TensaoFase(self):

        ref = [PhaseToComplex(100, 0), PhaseToComplex(100, 120), PhaseToComplex(100, 240)]
        self.assertEqual(TensaoFase(ref[0], 3), ref)

        ref = [PhaseToComplex(100, 30), PhaseToComplex(100, 150), PhaseToComplex(100, 270)]
        self.assertEqual(TensaoFase(ref[0], 3), ref)

    def test_3_FaseLinha(self):

        mod = 100/sqrt(3)
        ref = []
        for i in range(0,3):
            tmp = PhaseToComplex(mod, -30 + i*120)
            tmp = complex(round(tmp.real, 10), round(tmp.imag, 10))
            ref.append(tmp)
        
        ans = FaseLinha(TensaoFase(PhaseToComplex(100,0)))

        for i in range(0,3):
            ans[i] = complex( round(ans[i].real, 10), round(ans[i].imag, 10) )

        self.assertEqual(ans, ref)

        #######

        ref = []
        for i in range(0,3):
            tmp = PhaseToComplex(mod, -30 + i*120 + 30)
            tmp = complex(round(tmp.real, 10), round(tmp.imag, 10))
            ref.append(tmp)
        
        ans = FaseLinha(TensaoFase(PhaseToComplex(100,30)))

        for i in range(0,3): # fail due to rounding
            ans[i] = complex( round(ans[i].real, 10), round(ans[i].imag, 10) )

        self.assertEqual(ans, ref)

    def test_4_Correntes(self):

        ref = [1 + 0j]
        self.assertEqual(Correntes([2+0j], [2+0j]), ref)
        self.assertEqual(Correntes([2+1j], [2+1j]), ref)
        self.assertEqual(Correntes([0+1j], [0+1j]), ref)

    def test_5_DeltaEstrela(self):

        self.assertEqual(DeltaEstrela.Impedancia([3 + 0j, 3 + 0j, 3 + 0j]), [1 + 0j, 1 + 0j, 1 + 0j])
        self.assertEqual(DeltaEstrela.Impedancia([3 + 3j, 3 + 3j, 3 + 3j]), [1 + 1j, 1 + 1j, 1 + 1j])
        self.assertEqual(DeltaEstrela.Impedancia([0 + 3j, 0 + 3j, 0 + 3j]), [0 + 1j, 0 + 1j, 0 + 1j])

    def test_6_EstrelaDelta(self):

        self.assertEqual(EstrelaDelta.Impedancia([1 + 0j, 1 + 0j, 1 + 0j]), [3 + 0j, 3 + 0j, 3 + 0j])
        self.assertEqual(EstrelaDelta.Impedancia([1 + 1j, 1 + 1j, 1 + 1j]), [3 + 3j, 3 + 3j, 3 + 3j])
        self.assertEqual(EstrelaDelta.Impedancia([0 + 1j, 0 + 1j, 0 + 1j]), [0 + 3j, 0 + 3j, 0 + 3j])

    def test_7_TensaoNeutro(self):
        pass

if __name__ == '__main__':
    unittest.main()
