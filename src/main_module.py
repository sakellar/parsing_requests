import sys
import logging
from collections import Counter
from parser import Parser

file_name_nasa = "../data/NASA_access_log_Aug95"
output_file = "../data/report.tx"


class Collector:
    file_name="../data/NASA_access_log_Aug95"

    def __init__(self, args, input_file=file_name_nasa, output_file=output_file):
        self.parser = Parser(args)
        self.request_counter = 0
        self.success_counter = 0
        self.top10cnt = Counter()
        self.top10uncnt = Counter()
        self.top10hosts = Counter()
        self.top10hosts_dict = dict()
        self.top10hosts_cnt = Counter()
        self.line_number = 0
        self.fail_counter = 0
        self.options = self.parser.options
        self.error_lines = {}
        self.get_method()
        self.input_file = input_file
        self.output_file = output_file

    def get_method(self):
        method_name = ""
        if self.options.top10:
            method_name = "parse_top10"
        elif self.options.persuccess:
            method_name = "parse_successful_requests"
        elif self.options.perfail:
            method_name = "parse_unsuccessful_requests"
        elif self.options.top10fail:
            method_name = "parse_top10unsuccessful"
        elif self.options.top10hosts:
            method_name = "parse_top10hosts"

    def parse_top10(self, line):
        try:
            self.top10cnt[line.split()[6]] += 1
        except Exception:
            self.error_lines[self.request_counter] = "mal formed request: cannot parse status"

    def parse_successful_requests(self, line):
        try:
            status = line.split()[8]
            if int(status):
                if int(status) >= 200 and int(status) < 400:
                        self.success_counter += 1
        except ValueError:
            self.error_lines[self.request_counter] = "mal formed request: status is not an integer"
        except Exception:
            self.error_lines[self.request_counter] = "mal formed request: cannot parse status"

    def parse_unsuccessful_requests(self, line):
        try:
            status = line.split()[8]
            if int(status):
                if not (int(status) >= 200 and int(status) < 400):
                        self.fail_counter += 1
        except ValueError:
            self.error_lines[self.request_counter] = "mal formed request: status is not an integer"
        except Exception:
            self.error_lines[self.request_counter] = "mal formed request: cannot parse status"

    def parse_top10general(self, line):
        try:
            self.top10hosts[line.split()[0]] += 1
        except Exception:
            self.error_lines[self.request_counter] = "mal formed request: cannot parse status"

    def parse_top10unsuccessful(self, line):
        try:
            status = line.split()[8]
            if int(status):
                if not (int(status) >= 200 and int(status) < 400):
                    self.top10uncnt[line.split()[6]] += 1
        except ValueError:
            self.error_lines[self.request_counter] = "mal formed request: status is not an integer"
        except Exception:
            self.error_lines[self.request_counter] = "mal formed request: cannot parse status"

    def parse_top10hosts(self, line):
        try:
            self.top10hosts[line.split()[0]] += 1
        except Exception:
            self.error_lines[self.request_counter] = "mal formed request: cannot parse status"

    def produce_report_for_selected_option(self):
        if self.options.top10:
            top10requests =  "----Top 10 requests----\n"
            for item in self.top10cnt.most_common(10):
                top10requests += "request : {0}  number of requests : {1}\n".format(item[0], item[1])
            return top10requests 
        elif self.options.persuccess:
            return "Percentage of successful requests: {}".format(float(self.success_counter)/self.request_counter) + "\n"
        elif self.options.perfail:
            return "Percentage of unsuccessful requests: {}".format(float(self.fail_counter)/self.request_counter) + "\n"
        elif self.options.top10fail:
            top10requests =  "----Top 10 unsuccessful requests----\n"
            for item in self.top10uncnt.most_common(10):
                top10requests += "request : {0} \n".format(item[0])
            return top10requests 
        elif self.options.top10hosts:
            top10requests =  "----Top 10 hosts----\n"
            for item in self.top10hosts.most_common(10):
                top10requests += "host : {0} , Number of requests :  {1}\n".format(item[0], item[1])
            return top10requests 
        else:
            return ""

    def produce_report(self):
        with open(self.output_file, "w") as f:
            option_log = self.produce_report_for_selected_option()
            if option_log != "":
                f.write(option_log)
            f.write("----Error Log----\n")
            for key, value in self.error_lines.iteritems():
                error_log = "line number:" + str(key) + " error:" + str(value) +"\n"
                f.write(error_log)

    def collect_statistics(self):
        with open(self.input_file) as f:
            for line in f.readlines():
                print line.split()
                self.request_counter +=1
                self.line_number += 1
                if len(line.split()) != 10:
                    print self.request_counter
                    self.error_lines[self.request_counter] = "malformed request, number of columns is not 10"
                    continue
                self.parse_top10general(line)
                self.parse_top10(line)
                self.parse_successful_requests(line)
                self.parse_unsuccessful_requests(line)
                self.parse_top10unsuccessful(line)
                self.parse_top10hosts(line)
        self.produce_report() 

def main():
    try:
        Collector(sys.argv[1:])
        Collector.collect_data()
    except:
        pass

if __name__ == "__main__":
    main()
