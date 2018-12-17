import unittest

def stampa_PROVA(self):
    return "PROVA"

class test_MetodiStringa(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print(">> Avvio i test ... ")

    @classmethod
    def tearDownClass(cls):
        print("... Test conclusi <<")

    def test_str_upper(self):
        self.assertEqual(stampa_PROVA(self), "PROVA")
        #self.assertEqual('prova'.upper(), "PIPPO")

    def test_str_isupper(self):
        self.assertTrue('PROVA'.isupper())
        self.assertFalse('prova'.isupper())

    def test_str_split_1(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])

    def test_str_split_2(self):
        # verifica che il metodo split() fallisca quando il separatore
        # non e' una stringa
        with self.assertRaises(TypeError):
            s = 'hello world'
            s.split(2)


# Avvio "pythonico" automatico di tutti i test
if __name__ == '__main__':
   unittest.main()

# Avvio manuale di tutti i test mediante suite
#suite = unittest.TestLoader().loadTestsFromTestCase(test_MetodiStringa)
#unittest.TextTestRunner(verbosity=2).run(suite)

# Composizione manuale di una suite di test
#suite = unittest.TestSuite()
#suite.addTest(test_MetodiStringa('test_str_upper'))
#suite.addTest(test_MetodiStringa('test_str_isupper'))
#suite.addTest(test_MetodiStringa('test_str_split_1'))
#suite.addTest(test_MetodiStringa('test_str_split_2'))
#unittest.TextTestRunner(verbosity=2).run(suite)

# Avvio da riga di comando
#python -m unittest -f unittest1









