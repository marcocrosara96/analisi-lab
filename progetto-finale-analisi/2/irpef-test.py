import unittest
import irpef as c


class test_Irpef(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('>> Avvio i test ... ')

    @classmethod
    def tearDownClass(cls):
        print('... Test conclusi <<')

    def test_aliquota_23u(self):
        argv = ['test-istance', 15000.49]
        self.assertEqual(c.main(argv), 3450)

    def test_aliquota_27l(self):
        argv = ['test-istance', 15000.50]
        self.assertEqual(c.main(argv), 3450.27)

    def test_aliquota_27u(self):
        argv = ['test-istance', 28000.49]
        self.assertEqual(c.main(argv), 6960)

    def test_aliquota_38l(self):
        argv = ['test-istance', 28000.50]
        self.assertEqual(c.main(argv), 6960.38)
    
    def test_aliquota_38u(self):
        argv = ['test-istance', 55000.49]
        self.assertEqual(c.main(argv), 17220)

    def test_aliquota_41l(self):
        argv = ['test-istance', 55000.50]
        self.assertEqual(c.main(argv), 17220.41)

    def test_aliquota_41u(self):
        argv = ['test-istance', 75000.49]
        self.assertEqual(c.main(argv), 25420)

    def test_aliquota_43l(self):
        argv = ['test-istance', 75000.50]
        self.assertEqual(c.main(argv), 25420.43)

#avvio di tutti i test
if __name__ == '__main__':
    unittest.main()
