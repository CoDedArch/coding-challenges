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
    def check_all_caps(self, string_to_check:str):
        letters_all_caps = True
        while letters_all_caps:
            for letter in string_to_check:
                if letter is not letter.isupper():
                    letters_all_caps = False
                    break
        return letters_all_caps                
    def set_cap_conditions(self):
        self.cap_conditions.append(self.check_all_caps(self.string_input))      