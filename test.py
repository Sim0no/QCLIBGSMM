import unittest,complejo,math as m
class TestStringMethods(unittest.TestCase):
    def test_deveriaFallar(self):
        m2,m3=[[(7,0),(6,5)],[(6,-5),(0,-3)]],[[(7,0),(6,5)],[(6,-5),(-3,0)]]
        self.assertFalse(complejo.esHermitiana(m2))
        self.assertFalse(complejo.esUnitaria(m3))
    def test_deveriaServir(self):
        m3,m4=[[(7,0),(6,5)],[(6,-5),(-3,0)]],[[(m.cos(30),0),(-1*m.sin(30),0),(0,0)],[(m.sin(30),0),(m.cos(30),0),(0,0)],[(0,0),(0,0),(1,0)]]
        m5,m6 = [[(3,2),(5,-1),(0,2)],[(0,0),(12,0),(6,-3)],[(2,0),(4,4),(9,3)]],[[(1,0),(3,4),(5,-7)],[(10,2),(6,0),(2,5)],[(0,0),(1,0),(2,9)]]
        self.assertEquals(m5,complejo.matrizAdjunta(complejo.matrizAdjunta(m5)))
        self.assertTrue(complejo.esHermitiana(m3))
        self.assertTrue(complejo.esUnitaria(m4))
        self.assertTrue(len(m5)*len(m6) == len(complejo.productoTensor(m5,m6)))
        x = complejo.marbels([[(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)],[(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)],[(0,0),(1,0),(0,0),(0,0),(0,0),(1,0)],[(0,0),(0,0),(0,0),(1,0),(0,0),(0,0)],[(0,0),(0,0),(1,0),(0,0),(0,0),(0,0)],[(1,0),(0,0),(0,0),(0,0),(1,0),(0,0)]],[(6,0),(2,0),(1,0),(5,0),(3,0),(10,0)],1)
        self.assertEquals(x,[(0.0, 0.0), (0.0, 0.0), (12.0, 0.0), (5.0, 0.0), (1.0, 0.0), (9.0, 0.0)])
if __name__ == '__main__':
    unittest.main()

