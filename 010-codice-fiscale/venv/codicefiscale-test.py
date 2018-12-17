import unittest
from codicefiscale import *


class CodiceFiscaleTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('>> Avvio i test ... ')

    @classmethod
    def tearDownClass(cls):
        print('... Test conclusi <<')

    def test_firstTest(self):
        argv = ['0', 'crosara', 'marco', '02/08/1996', 'thiene', 'm']
        self.assertEquals(main(argv), 'crsmrc96m02l157j')

    def test_ControFilippo(self):
        argv = ['0', 'contro', 'filippo', '12/10/1996', 'verona', 'm']
        self.assertEquals(main(argv), 'cntfpp96r12l781c')

    def test_SunyiXu(self):
        argv = ['0', 'xu', 'sunyi', '20/09/1996', 'cina', 'f']
        self.assertEquals(main(argv), 'snyxux96p60z210y')

    # se il nome è troppo lungo --> non funziona
    # se il cognome è troppo corto --> non funziona
    # se il nome contiene uno spazio --> non funziona


if __name__ == '__main__':
   unittest.main()








