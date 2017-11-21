import unittest
from main_module import Collector
from mock import patch, mock_open, call, MagicMock, Mock
from collections import Counter

data = "in24.inetnebr.com - - [01/Aug/1995:00:00:01 -0400] \"GET /shuttle/missions/sts-68/news/sts-68-mcc-05.txt HTTP/1.0\" 200 1839\n\
in24.inetnebr.com - - [01/Aug/1995:00:00:01 -0400] \"GET /shuttle/missions/sts-68/news/sts-68-mcc-05.txt \
        HTTP/1.0\" 200 1839\n\
in24.inetnebr.com - - [01/Aug/1995:00:00:01 -0400] \"GET /shuttle/missions/sts-68/news/sts-68-mcc-05.txt HTTP/1.0\" 500 1839\n"

data2 = "in24.inetnebr.com - - [01/Aug/1995:00:00:01 -0400] \"GET /shuttle/missions/sts-68/news/sts-68-mcc-05.txt HTTP/1.0\" 200 1839\n\
in24.inetnebr.com - - [01/Aug/1995:00:00:01 -0400] \"GET /shuttle/missions/sts-68/news/sts-68-mcc-05.txt \
        HTTP/1.0\" 200 1839\n\
in24.inetnebr.com - - [01/Aug/1995:00:00:01 -0400] \"GET /shuttle/missions/sts-68/news/another.txt HTTP/1.0\" 500 1839\n"


class TestCollector(unittest.TestCase):

     @patch('__builtin__.open', new_callable=mock_open, read_data=data)
     def test_read_success_percent(self, mo):
          collector = Collector(["--persuccess"])
          options = collector.parser.options
          self.assertEquals(options.persuccess, True)
          collector.collect_statistics()
          self.assertEquals(collector.success_counter, 2)
          self.assertEquals(collector.request_counter, 3)

     @patch('__builtin__.open', new_callable=mock_open, read_data=data2+data)
     def test_10topdict_general(self, mo):
          collector = Collector(["--persuccess"])
          options =  collector.parser.options
          self.assertEquals(options.persuccess, True)
          collector.collect_statistics()
          self.assertEquals(collector.success_counter, 4)
          self.assertEquals(collector.request_counter, 6)
          expected_dict = {'in24.inetnebr.com': Counter({'/shuttle/missions/sts-68/news/another.txt':1, '/shuttle/missions/sts-68/news/sts-68-mcc-05.txt': 5})}
          self.assertEquals(collector.top10hosts_dict, expected_dict)

if __name__ == '__main__':
    unittest.main()
