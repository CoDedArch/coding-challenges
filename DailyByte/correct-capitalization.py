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

    def set_cap_conditions(self):
        pass