def stringReversal(input_string:str):
   if type(input_string) is not str:
      raise ValueError('function argument must be a string')
   return input_string[::-1]

print(stringReversal('Hear am i'))