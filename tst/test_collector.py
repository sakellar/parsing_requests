import unittest
from main_module import Collector

class TestCollector(unittest.TestCase):

     def test_read_success_percent(self):
          collector = Collector(["--persuccess"],input_file="../data/test_file", output_file="../data/report1.txt")
          options =  collector.parser.options
          collector.collect_statistics()

     def test_read_success_percent(self):
          collector = Collector(["--perfail"],input_file="../data/test_file", output_file="../data/report2.txt")
          options =  collector.parser.options
          collector.collect_statistics()
     """
     def test_read_success_percent(self):
          collector = Collector(["--top10"])
          options =  collector.parser.options
          collector.collect_statistics()

     def test_read_success_percent(self):
          collector = Collector(["--top10fail"])
          options =  collector.parser.options
          collector.collect_statistics()

     def test_read_success_percent(self):
          collector = Collector(["--top10hosts"])
          options =  collector.parser.options
          collector.collect_statistics()
     """
if __name__ == '__main__':
    unittest.main()
