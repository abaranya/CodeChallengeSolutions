# Solution class
import sys


class Solution:

    def __init__(self):
        self.filename = ""
        self.lines = 0
        self.test_data = []

    def open_input(self, filename):
        self.filename = filename
        if self.filename > "":
            sys.stdin = open(self.filename, 'r')

    def read_data(self):
        self.test_data=[]
        for line in map(str.rstrip, sys.stdin):
            self.test_data.append(line)
            print("line ", len(self.test_data), " : ", line)

    def print_lines(self):
        print(self.lines)



