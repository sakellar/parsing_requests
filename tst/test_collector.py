import unittest
from main_module import Collector

class TestCollector(unittest.TestCase):

     def test_collect_success_percent(self):
          collector = Collector(["--persuccess"],input_file="../data/test_file", output_file="../data/report1.txt")
          collector.collect_statistics()

     def test_collect_fail_percent(self):
          collector = Collector(["--perfail"],input_file="../data/test_file", output_file="../data/report2.txt")
          collector.collect_statistics()

     def test_collect_top10requests(self):
          collector = Collector(["--top10"],input_file="../data/test_file", output_file="../data/report3.txt")
          options =  collector.parser.options
          collector.collect_statistics()

     def test_top10fail(self):
          collector = Collector(["--top10fail"],input_file="../data/test_file", output_file="../data/report4.txt")
          collector.collect_statistics()

     def test_top10hosts(self):
          collector = Collector(["--top10hosts"],input_file="../data/test_file", output_file="../data/report5.txt")
          collector.collect_statistics()

if __name__ == '__main__':
    unittest.main()
