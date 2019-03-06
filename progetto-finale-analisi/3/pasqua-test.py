"""
    Test sui giorni di pasqua
"""

import unittest
import pasqua as c

class test_Pasqua(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('>> Avvio i test ... ')

    @classmethod
    def tearDownClass(cls):
        print('... Test conclusi <<')

    def test_2018(self):
        argv = ['', '2018']
        self.assertEqual(c.main(argv), '1 Aprile 2018')

    def test_2016(self):
        argv = ['', '2016']
        self.assertEqual(c.main(argv), '27 Marzo 2016')

    def test_1609(self): # anno che presenta una eccezione sull'algoritmo di gauss
        argv = ['', '1609']
        self.assertEqual(c.main(argv), '19 Aprile 1609')

    def test_1582(self): # anno non gestito dal programma -> il risultato atteso è None
        argv = ['', '1582']
        self.assertEqual(c.main(argv), None)

    def test_2600(self): # anno non gestito dal programma -> il risultato atteso è None
        argv = ['', '2600']
        self.assertEqual(c.main(argv), None)

#avvio di tutti i test
if __name__ == '__main__':
    unittest.main()
