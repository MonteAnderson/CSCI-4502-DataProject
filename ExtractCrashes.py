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
    newListTemp = []
    countedList = []
    count = 1
    with open('ToC-NC-crashes.csv', 'rU') as fin:
        #headerLine = next(fin)
        for row in csv.reader(fin):
            if ('2016' in row[0]):
                newListDate.append(str(row[0]))
            
        newListDate.sort()

        for item in newListDate:
            item = item[:10]
            #print(item)
            newListTemp.append(item[:10])

        newListTemp.sort()
        print(Counter(newListTemp))
        #print(newListTemp)
        #for item in newListDate:

        with open('test-c.csv', 'wb') as fileOut:
            fileOut.write("Date,#ofAccidents\n")

            for item in newListTemp:
                fileOut.write(item)
                #fileOut.write(countedList)
                fileOut.write(",")
                fileOut.write("\n")
                
        newListDate.sort()
        #print(Counter(newListDate))
        #plt.plot(newListDate,newListPrecip)
        #plt.show()
