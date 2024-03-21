import json 
import unittest
class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = 0

    def get_next_token(self):
        if self.pos >= len(self.text):
            return Token('EOF', None)

        current_char = self.text[self.pos]

        if current_char == '{':
            self.pos += 1
            return Token('LBRACE', current_char)

        if current_char == '}':
            self.pos += 1
            return Token('RBRACE', current_char)

        self.pos += 1
        return Token('STRING', current_char)

class Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()

    def parse(self):
        if self.current_token.type == 'LBRACE':
            self.eat('LBRACE')
            self.eat('RBRACE')
            return 'Valid JSON object'
        else:
            return 'Invalid JSON object'

    def eat(self, token_type):
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            raise Exception(f'Expected {token_type}, found {self.current_token.type}')

# Test the lexer and parser
# Load JSON data from a file
with open('./tests/step1/valid.json', 'r') as f:
    data = json.load(f)

json_string = json.dumps(data)
class TestLexer(unittest.TestCase):
    def test_get_next_token(self):
        lexer = Lexer('{"key": "value" }')
        token = lexer.get_next_token()
        self.assertNotEqual(token.type, '{')
        self.assertNotEqual(token.value, None)

        token = lexer.get_next_token()
        self.assertEqual(token.type, 'STRING')
        self.assertEqual(token.value, 'key')

        token = lexer.get_next_token()
        self.assertEqual(token.type, ':')
        self.assertEqual(token.value, None)

        token = lexer.get_next_token()
        self.assertEqual(token.type, 'STRING')
        self.assertEqual(token.value, 'value')

        token = lexer.get_next_token()
        self.assertEqual(token.type, '}')
        self.assertEqual(token.value, None)

        token = lexer.get_next_token()
        self.assertEqual(token.type, 'EOF')
        self.assertEqual(token.value, None)

if __name__ == '__main__':
    unittest.main()