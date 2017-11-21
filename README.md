# parsing_requests

Parses the sample HTTP sample log file available in NASA-HTTP, or another file with well formed requests and produces a plain text report containing the following information:

1.	Top 10 requested pages and the number of requests made for each
2.	Percentage of successful requests (anything in the 200s and 300s range)
3.	Percentage of unsuccessful requests (anything that is not in the 200s or 300s range)
4.	Top 10 unsuccessful page requests
5.	The top 10 hosts making the most requests, displaying the IP address and number of requests made.
6.	Option parsing to produce only the report for one of the previous points (e.g. only the top 10 URLs, only the percentage of successful requests and so on)
7.	For each of the top 10 hosts, show the top 5 pages requested and the number of requests for each
8.	The log file contains malformed entries; for each malformed line, display an error message and the line number.


## REQUIREMENTS
Install python mock
```
$ sudo pip install mock
```
Unzip NASA HTTP log inside data/ directory.

## INSTALL
Alternatevely if you have donwloaded source code:
```
python setup.py install
```

## Documentation
To collect statistics and use this tool. Assuming you have dowloaded/cloned source code.
Go inside src code. Then run python main_module.py
To get the report.txt for NASA file unzip NASA file inside data/ directory.
When you run python main_module inside src/ directory then the default input/output files for this script 
is to read from:
```
file_name_nasa = "../data/NASA_access_log_Aug95"
```
and write to:
```
output_file = "../data/report.txt"
```

### Example 1:
```
$ python main_module.py --top10hostsadadsd
Usage: exec [--top10] [--persucess] [--perfail] [--top10fail] [--top10hosts] [--all]

main_module.py: error: no such option: --top10hostsadadsd
```
### Example 2:
```
$ python main_module.py --help
Usage: exec [--top10] [--persucess] [--perfail] [--top10fail] [--top10hosts]

Options:
  -h, --help    show this help message and exit
  --top10       1.  Top 10 requested pages and requests for each
  --persuccess  2.  Percentage of successful requests
  --perfail     3.  Percentage of unsuccessful requests
  --top10fail   4.  Top 10 unsuccessful page requests
  --top10hosts  5.  The top 10 hosts making the most requests
```
### Example 3 (Does not check if request status code is wrong i.e. 211):
```
python main_module.py  --persuccess
```
Then result report will be the following:
```
$ cat report.txt 
Percentage of successful requests: 0.954545454545
```
### Example 4:
```
----Optional Report----
python main_module.py  --perfail
```
Then result report will be the following:
```
$ cat report.txt 
----Optional Report----
Percentage of unsuccessful requests: 0.0454545454545
```
### Example 5:
```
python main_module.py  --top10
```
Then result report will be the following:
```
$ cat report.txt 
----Optional Report----
----Top 10 requests----
request : /history/apollo/apollo-13/apollo-13-patch-small.gif  number of requests : 3
request : /shuttle/countdown/  number of requests : 3
request : /images/ksclogosmall.gif  number of requests : 3
request : /history/apollo/images/footprint-small.gif  number of requests : 2
request : /images/ksclogo-medium.gif  number of requests : 2
request : /images/KSC-logosmall.gif  number of requests : 2
request : /history/apollo/images/footprint-logo.gif  number of requests : 2
request : /shuttle/resources/orbiters/discovery.html  number of requests : 1
request : /images/NASA-logosmall.gif  number of requests : 1
request : /shuttle/resources/orbiters/discovery-logo.gif  number of requests : 1
```
### Example 6:
```
python main_module.py --top10hosts
```
Then result report will be the following:
```
$ cat report.txt 
----Optional Report----
----Top 10 hosts----
host : pm9.j51.com , Number of requests :  6
host : uplherc.upl.com , Number of requests :  6
host : ad11-061.compuserve.com , Number of requests :  5
host : piweba3y.prodigy.com , Number of requests :  5
host : slip-4-12.ots.utexas.edu , Number of requests :  4
host : js002.cc.utsunomiya-u.ac.jp , Number of requests :  3
host : ad06-061.compuserve.com , Number of requests :  3
host : ip-pdx6-54.teleport.com , Number of requests :  3
host : piweba1y.prodigy.com , Number of requests :  2
host : piweba4y.prodigy.com , Number of requests :  2
```
### Example 7:
```
python main_module.py --top10fail
```
Then result report will be the following:
```
$ cat report.txt
----Optional Report----
----Top 10 unsuccessful requests----
request : /shuttle/resources/orbiters/discovery.gif 
request : /images/ksclogosmall.gif 
```
### Example 8:
For each Optional report a main report is aslo produced displaying for each of the top 10 hosts, show the top 5 pages requested and the number of requests for each
```
$ cat report.txt | less
----Main Report---
host : pm9.j51.com , Number of requests :  6
----Top 5 requests-----
request : /facilities/mlp.html , Number of requests :  1
request : /images/NASA-logosmall.gif , Number of requests :  1
request : /images/USA-logosmall.gif , Number of requests :  1
request : /images/mlp-logo.gif , Number of requests :  1
request : /images/ksclogo-medium.gif , Number of requests :  1
```
### Example 9: 
The log file contains malformed entries; for each malformed line, display an error message and the line number.
```
$ cat report.txt | less
----Error Log----
line number:270336 error:malformed request, number of columns is not 10
line number:622595 error:malformed request, number of columns is not 10
line number:606222 error:malformed request, number of columns is not 10
```
### Reports
Individual reports for each option can be found in data folder:
```
/data/report_top10.txt
/data/report_top10fail.tct
/data/report_top10hosts
/data/report_per_sucess.txt
/data/report_per_fail.txt
```

## Testing

To test  code you can run inside tst directory
```
bash run_tests.sh
```

Alternatively you can run explicitily tests:
```
python -m unittest test_parser
```
```
python -m unittest test_collector_unit
```
```
python -m unittest test_collector
```

test_parser unit test is the unit test for src/parser.py
test_collector_unit  unit test is the unit test for Collector class which is imported from main_module.py
test_collector is an automated test which has input data/test_file and produces different reports for different options
