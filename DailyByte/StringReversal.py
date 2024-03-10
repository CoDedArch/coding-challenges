import unittest

def stringReversal(input_string):
   if type(input_string) is not str:
      raise ValueError('function argument must be a string')
   return input_string[::-1]

print(stringReversal('Hear am i'))


# unittest 
class TestStringReversal(unittest.TestCase):
   def test_string_reversal(self):
      self.assertEqual(stringReversal('Cat'), 'taC')
      self.assertEqual(stringReversal('Dog'), 'goD')
      self.assertEqual(stringReversal(''), '')

   def test_string_reversal_error(self):
      with self.assertRaises(ValueError):
         stringReversal(123)

if __name__ == '__main__':
   unittest.main()