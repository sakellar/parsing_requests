import unittest
from mock import Mock, patch, call
from parser import Parser

class ClientTest(unittest.TestCase):

    def test_parse(self):
        parser = Parser(["--top10"])
        expected_dict = {'top10': True, 'perfail': None, 'persuccess': None, 'top10fail': None, 'top10hosts': None}
        self.assertEqual(parser.options, expected_dict)

        parser2 = Parser(["--persuccess"])
        expected_dict = {'top10': None, 'perfail': None, 'persuccess': True, 'top10fail': None, 'top10hosts': None}
        self.assertEqual(parser2.options, expected_dict)

        parser3 = Parser(["--perfail"])
        expected_dict = {'top10': None, 'perfail': True, 'persuccess': None, 'top10fail': None, 'top10hosts': None}
        self.assertEqual(parser3.options, expected_dict)

        parser4= Parser(["--top10fail"])
        expected_dict = {'top10': None, 'perfail': None, 'persuccess': None, 'top10fail': True, 'top10hosts': None}
        self.assertEqual(parser4.options, expected_dict)

        parser5= Parser(["--top10hosts"])
        expected_dict = {'top10': None, 'perfail': None, 'persuccess': None, 'top10fail': None, 'top10hosts': True}
        self.assertEqual(parser5.options, expected_dict)

    def test_wrongoption(self):
        try:
           parser = Parser(["--ltop10"])
        except:
           print "exception 1"

    def test_parse2options(self):
        try:
           parser = Parser(["--top10", "--top10hosts"])
        except:
           print "exception 2"

    def test_pare2args(self):
        try:
           parser = Parser(["--top10", "hello"])
        except:
            print "exception 3"
        
if __name__ == '__main__':
    unittest.main()
