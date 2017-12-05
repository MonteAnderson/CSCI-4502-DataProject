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
    newListTemp = []
    myDict = {}
    newDict = {}
    count = 0
    with open('ToC-NC-weather.csv', 'rU') as fin:
        headerLine = next(fin)
        for row in csv.reader(fin):
            if ('2016' in row[0]):
                newListDate.append(str(row[0]))
	        newListTemp.append(row[1])
                newListPrecip.append(row[3])

        with open('test.csv', 'wb') as fileOut:
            fileOut.write("Date,Temp,\n")
            myDict = dict(zip(newListDate, newListTemp))
            testZip = zip(newListDate, newListTemp, newListPrecip)
            testZip.sort(key = lambda t: t[0])

            for a,b,c in testZip:
                print(a,b,c)
                fileOut.write(a)
                fileOut.write(",")
                fileOut.write(b)
                fileOut.write(",")
                fileOut.write(c)
                fileOut.write("\n")

            #print(myDict)
            #orderedMyDict = collections.OrderedDict(sorted(myDict.items())) 

            """for key, value in orderedMyDict.items():
                fileOut.write(key)
                fileOut.write(",")
                fileOut.write(value)

                fileOut.write("\n")"""
                
        newListDate.sort()
        #print(Counter(newListDate))
        #plt.plot(newListDate,newListPrecip)
        #plt.show()
