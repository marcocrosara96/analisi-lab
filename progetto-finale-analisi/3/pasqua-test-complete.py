"""
    Confronto i risultati ottenuti dalla funzione con quelli di un database trovato online
    per verificare la correttezza di ogni singolo anno in input al programma
"""

import unittest
import pasqua as c

class test_Pasqua(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('>> Avvio i test sul database di confronto ... ')

    @classmethod
    def tearDownClass(cls):
        print('... i test sono stati conclusi <<')

    @staticmethod
    def readDB(year): # non un test: funzione di supporto
        with open('DB_pasqua_confronto.txt', 'r') as db:
            for line in db:
                if year in line:
                    return line[: len(line)-1]
        # Il return nullo è un caso di errore "giorno non trovato nel database" di questa 
        # funzione di test pertanto non serve controllarne la copertura
        return None  # pragma: no cover

    def test_valid_years(self):
        n_tests = 0
        for y in range(1583, 2600):
            argv = ['', str(y)]
            self.assertEqual(c.main(argv), test_Pasqua.readDB(str(y)))
            n_tests+=1
        print('Effettuati ' + str(n_tests) + ' test (con anni validi)')

    def test_invalid_years_1(self):
        argv = ['', '1582']
        self.assertEqual(c.main(argv), None)

    def test_invalid_years_2(self):
        argv = ['', '2600']
        self.assertEqual(c.main(argv), None)

#avvio di tutti i test
if __name__ == '__main__':
    unittest.main()
