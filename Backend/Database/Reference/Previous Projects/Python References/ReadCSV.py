# Lab 5 - Data Analysis class ChangePopulation
# Author: Dan Beck
# Date: April 18, 2020
# Class to read the PopChange.csv file

import csv
                
class ReadCSV:         
    def __init__(self, line):
        self.data = line
        
        self.c1 = self.data[0].strip()
        self.c2 = self.data[1].strip()
        self.c3 = self.data[2].strip()
        self.c4 = self.data[3].strip()
        self.c5 = self.data[4].strip()
        self.c6 = self.data[5].strip()
        self.c7 = self.data[6].strip()
        
    @property
    def c1(self):
        return self.c1
    
    @property
    def c2(self):
        return self.c2
    
    @property
    def c3(self):
        return self.c3
    
    @property
    def c4(self):
        return self.c4
    
    @property
    def c5(self):
        return self.c5
    
    @property
    def c6(self):
        return self.c6
    
    @property
    def c7(self):
        return self.c7