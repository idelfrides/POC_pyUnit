""" POC: unittest """


import unittest


class TestStringMethods(unittest.TestCase):
    """ Simple pyUnit test """
    
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO', msg="Error on assertEqual. The strings do not match.")
    
    def test_isupper(self):
        self.assertTrue('FOO'.isupper(), msg="Error in the assertTrue. String is not uppercase")
        self.assertFalse('Foo'.isupper(), msg="Error in assertFalse. String is uppercase")
    
    def test_split(self):
        s = 'Hello World'
        self.assertEqual(s.split(), ['Hello', 'World'])
        with self.assertRaises(TypeError):
            s.split(7)
    
    print('\n\n')


if __name__ == '__main__':
    unittest.main()

