import unittest
from mock import Mock, patch, call
from parser import Parser, OptionParser

class TestParser(unittest.TestCase):

    def test_parse_options(self):
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

    #@patch("parser.OptionParser.error")
    #def test_wrongoption(self, mock_error1):
    #    parser1 = Parser(["--ltop10"])
    #    mock_error1.assert_has_calls([call('error: no such option: --ltop10')])

    @patch("parser.OptionParser.error")
    def test_parse_wrong_options(self, mock_error):
           parser = Parser(["--top10", "--top10hosts"])
           #mock_error.assert_has_calls([call('You need to give only one option')])
           parser = Parser(["--ltop10"])
           parser = Parser(["--top10", "hello"])
           mock_error.assert_has_calls([call('error: no such option: --ltop10')])

    def test_pare2args(self):
        try:
           parser = Parser(["--top10", "hello"])
        except:
            print "exception 3"
        
if __name__ == '__main__':
    unittest.main()
