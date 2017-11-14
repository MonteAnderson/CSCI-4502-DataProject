# Monte Anderson
# Fall 2017, Data Mining Project

import argparse
import csv
import math
import numpy as np
#import scipy as stats
import matplotlib.pyplot as plt
import collections
from collections import Counter

if __name__ == "__main__":
    print("TestNorm")
    newListDate = []
    newListPrecip = []
    count = 0
    myDict = {}
    i = 0
    countedList = []
    od = {}
    with open('Crash_Data.csv', 'rU') as fin:
        #headerLine = next(fin)
        for row in csv.reader(fin):
            #print(row[1])
            if ('2016' in row[3]):
                item = str(row[3])
                #print(item[0:10])
                newListDate.append(item[0:10])

                #newListPrecip.append(row[3])
                #print(row[2] + "  |  " + str(row[3]))

        newListDate.sort()
        #print(Counter(newListDate))
    with open('test.csv', 'wb') as fileOut:

        countedList = Counter(newListDate)
        od = collections.OrderedDict(sorted(countedList.items())) 
        for key, value in od.items():
            myDict = (key, value)
    
            fileOut.write(key) 
            fileOut.write('\t' + str(value))
            fileOut.write('\n')
            #print(myDict)

        """while (i < len(newListDate)):
            fileOut.write(newListDate[i])
            fileOut.write('\n')
            i += 1"""


        #plt.plot(newListDate,newListPrecip)
        #plt.show()
