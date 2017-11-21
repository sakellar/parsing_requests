from optparse import OptionParser
import logging

class Parser:
    """Parser Class which initializes parser with provided options"""
    def __init__(self, args):
        """Parser class __init__ """
        self.parser = self._initialize_parser()
        (self.options, self.args) = self.parser.parse_args(args)
        self._check_options()
        self._check_args()

    def _initialize_parser(self):
        """Initializes Parser"""
        parser = OptionParser("exec [--top10] [--persucess] [--perfail] [--top10fail] [--top10hosts]")
        parser.add_option("--top10", action="store_true", dest="top10",
                      help="1.  Top 10 requested pages and requests for each")
        parser.add_option("--persuccess", action="store_true", dest="persuccess",
                      help="2.  Percentage of successful requests")
        parser.add_option("--perfail", action="store_true", dest="perfail",
                      help="3.  Percentage of unsuccessful requests")
        parser.add_option("--top10fail", action="store_true", dest="top10fail",
                      help="4.  Top 10 unsuccessful page requests")
        parser.add_option("--top10hosts", action="store_true", dest="top10hosts",
                      help="5.  The top 10 hosts making the most requests")
        return parser

    def _check_options(self):
        """
        Counts the number of options against 1
        """
        option_counter = 0

        if self.options.top10:
            option_counter +=1
        if self.options.persuccess:
            option_counter +=1
        if self.options.perfail:
            option_counter +=1
        if self.options.top10fail:
            option_counter +=1
        if self.options.top10hosts:
            option_counter +=1

        if option_counter == 0:
            self.parser.error("You need to give an option")
            return
        elif option_counter == 1:
            return
        else:
            self.parser.error("You need to give only one option")
            return

    def _check_args(self):
        """Checks number of args"""
        if len(self.args) != 0:
            self.parser.error("no arguments needed")

