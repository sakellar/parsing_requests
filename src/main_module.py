import sys
import logging
from collections import Counter
from parser import Parser

"""Files needed for this module"""
file_name_nasa = "../data/NASA_access_log_Aug95"
output_file = "../data/report.txt"
test_file = "../data/test_file"

class Collector:

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
        self.options = self.parser.options
        self.error_lines = {}
        self.input_file = input_file
        self.output_file = output_file

    def parse_requested_pages(self, line):
        """
        Parses pages and counts the number for each one
        """
        try:
            self.top10cnt[line.split()[6]] += 1
        except Exception:
            self.error_lines[self.line_number] = "malformed request: cannot parse status"

    def parse_successful_requests(self, line):
        """
        Counts the number of successful requests
        """
        try:
            status = line.split()[8]
            if int(status):
                if int(status) >= 200 and int(status) < 400:
                        self.success_counter += 1
        except ValueError:
            self.error_lines[self.line_number] = "malformed request: status is not an integer"
            self.request_counter -= 1
        except Exception:
            self.error_lines[self.line_number] = "malformed request: cannot parse status"
            self.request_counter -= 1

    def parse_request_per_host(self, line):
        """
        Collects request, number of requests per host
        """
        try:
            host = line.split()[0]
            self.top10hosts[host] += 1
            if self.top10hosts_dict == {}:
                cnt = Counter()
                cnt[line.split()[6]] += 1
                self.top10hosts_dict[host] = cnt
            else:
                if self.top10hosts_dict.has_key(host): 
                    value_cnt = self.top10hosts_dict[host]
                    value_cnt[line.split()[6]] += 1
                    self.top10hosts_dict[host] = value_cnt
                else:
                    cnt = Counter()
                    cnt[line.split()[6]] += 1
                    self.top10hosts_dict[host] = cnt

        except Exception as e:
            self.error_lines[self.line_number] = "malformed request: cannot parse status"
            self.request_counter -= 1

    def parse_unsuccessful_page_requests(self, line):
        """
        Parses requests not in 300s 400s
        """
        try:
            status = line.split()[8]
            if int(status):
                if not (int(status) >= 200 and int(status) < 400):
                    self.top10uncnt[line.split()[6]] += 1
        except ValueError:
            self.error_lines[self.line_number] = "malformed request: status is not an integer"
            self.request_counter -= 1
        except Exception:
            self.error_lines[self.line_number] = "malformed request: cannot parse status"
            self.request_counter -= 1

    def produce_report_for_selected_option(self):
        """
        Returns report for selected option
        """
        if self.options.top10:
            top10requests =  "----Top 10 requests----\n"
            for item in self.top10cnt.most_common(10):
                top10requests += "request : {0}  number of requests : {1}\n".format(item[0], item[1])
            return top10requests 
        elif self.options.persuccess:
            return "Percentage of successful requests: {}".format(float(self.success_counter)/self.request_counter) + "\n"
        elif self.options.perfail:
            return "Percentage of unsuccessful requests: {}".format(float(self.request_counter -self.success_counter)/self.request_counter) + "\n"
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
        """
        Main function for producing report
        """
        with open(self.output_file, "w") as f:
            option_log = self.produce_report_for_selected_option()
            if option_log != "":
                f.write("----Optional Report----\n")
                f.write(option_log)
            f.write("----Main Report---\n")
            top10hosts =  "----Top 10 hosts----\n"
            for host in self.top10hosts.most_common(10):
                f.write("host : {0} , Number of requests :  {1}\n".format(host[0], host[1]))
                f.write("----Top 5 requests-----\n")
                for request in self.top10hosts_dict[host[0]].most_common(5):
                     f.write("request : {0} , Number of requests :  {1}\n".format(request[0], request[1]))
            f.write("----Error Log----\n")
            for key, value in self.error_lines.iteritems():
                error_log = "line number:" + str(key) + " error:" + str(value) +"\n"
                f.write(error_log)

    def collect_statistics(self):
        """
        Collects statistics and Produces Report
        """
        with open(self.input_file) as f:
            for line in f.readlines():
                self.request_counter +=1
                self.line_number += 1
                if len(line.split()) != 10:
                    self.request_counter -= 1
                    self.error_lines[self.line_number] = "malformed request, number of columns is not 10"
                    continue
                self.parse_request_per_host(line)
                if self.options.top10:
                    self.parse_requested_pages(line)
                if self.options.persuccess or self.options.perfail:
                    self.parse_successful_requests(line)
                if self.options.top10fail:
                    self.parse_unsuccessful_page_requests(line)
        self.produce_report() 

def main():
    try:
        collector = Collector(sys.argv[1:])
        collector.collect_statistics()
    except:
        pass

if __name__ == "__main__":
    main()
