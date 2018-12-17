import unittest
from coverage3 import *


class Coverage3Tests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('>> Avvio i test ... ')

    @classmethod
    def tearDownClass(cls):
        print('... Test conclusi <<')

    def test_0(self):
        argv = [0]
        main(argv)

    def test_1(self):
        argv = [0, 1]
        main(argv)

    def test_2(self):
        argv = [0, 2]
        main(argv)

    def test_3(self):
        argv = [0, 3]
        main(argv)

    def test_4(self):
        argv = [0, 4]
        main(argv)

    def test_6(self):
        argv = [0, 6]
        main(argv)

    def test_a(self):
        argv = [0, 'a']
        main(argv)


if __name__ == '__main__':
    unittest.main()
