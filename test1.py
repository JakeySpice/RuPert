import unittest
from RuPertGUI import generate_response


class TestRuPert(unittest.TestCase):

    def test_generate_response(self):
        prompt = "What are some examples of restrictive practices?"
        response = generate_response(prompt)
        self.assertIsNotNone(response)
        self.assertIsInstance(response, str)

    def test_generate_response_empty(self):
        prompt = ""
        response = generate_response(prompt)
        self.assertIsNotNone(response)
        self.assertIsInstance(response, str)

    def test_generate_response_whitespace(self):
        prompt = "    "
        response = generate_response(prompt)
        self.assertIsNotNone(response)
        self.assertIsInstance(response, str)


if __name__ == '__main__':
    unittest.main()
