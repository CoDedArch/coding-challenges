import unittest

name = 'keL'
print (name.isupper())


class CorrectCapitalization:
    """This Class Answers Google Questions
        on testing whether a string uses correct capitalization
        or not.
        1. All letters are capitalized
        2. no letters are capitalized
        3. only the first letter is capitalized
    """
    def __init__(self,input_string:str):
        """initializes states

        Args:
            input_string (str): user input 
        """
        self.string_input = input_string
        self.cap_conditions = []
        self.is_correctly_capitalized = None

    def check_all_caps(self, string_to_check:str):
        return string_to_check.isupper()
    
    def check_for_no_caps(self, string_to_check:str):
        return string_to_check.islower()
    
    def only_first_is_cap(self, string_to_check:str):
        first_letter_cap = True
        remaining_letters_not_cap = True
        first_letter= string_to_check[0]
        remaining_letters = string_to_check[1:]

        if not first_letter.isupper():
            first_letter_cap = False
        
        if not self.check_for_no_caps(remaining_letters):
            remaining_letters_not_cap = False
        return all([first_letter_cap, remaining_letters_not_cap])
    
    def set_cap_conditions(self, string_to_check):
        self.cap_conditions.append(self.check_all_caps(string_to_check))
        self.cap_conditions.append(self.check_for_no_caps(string_to_check))
        self.cap_conditions.append(self.only_first_is_cap(string_to_check))
        print(self.cap_conditions)
        return 

    def check_is_correctly_cap(self):
        self.set_cap_conditions(self.string_input)
        self.is_correctly_capitalized = any(self.cap_conditions)
        return self.is_correctly_capitalized


class TestCapitalization(unittest.TestCase):
    def test_is_correctly_capitalized(self):
        usa = CorrectCapitalization('USA')
        calvin = CorrectCapitalization('Calvin')
        computer = CorrectCapitalization('CompUter')
        coding = CorrectCapitalization('coding')
        self.assertEqual(usa.check_is_correctly_cap(), True)
        self.assertEqual(calvin.check_is_correctly_cap(), True)
        self.assertEqual(computer.check_is_correctly_cap(), False)
        self.assertEqual(coding.check_is_correctly_cap(), True)



if __name__ == '__main__':
    unittest.main()