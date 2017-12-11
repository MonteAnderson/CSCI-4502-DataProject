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
    print("Completed Creating Database. Filename: (YEAR)-information.csv")
    countedList = []
    newListDate = []
    newListTemp = []
    newListPrecip = []
    newListSnowFall = []
    newListAvgWindSpeed = []
    newListFog = []
    newListIce = []
    newListCrashes = []
    newListCrashesSliced = []
    countedCrashes = []
    index = 0

    with open('ToC-NC-crashes.csv', 'rU') as fin:
        headerLine = next(fin)
        for row in csv.reader(fin):
            if ('2016' in row[0]):
                item= str(row[0])
                newListCrashes.append(str(item[:10]))      
        newListCrashes.sort()
        #print(newListCrashes)
        
    with open('ToC-NC-weather.csv', 'rU') as fin:
        headerLine = next(fin)
        for row in csv.reader(fin):
            if ('2016' in row[0]):
                newListDate.append(str(row[0]))
	        newListTemp.append(row[1])
                newListPrecip.append(row[3])
                newListSnowFall.append(row[4])
                newListFog.append(row[11])
                newListIce.append(row[16])


        with open('2016-information.csv', 'wb') as fileOut:
            countedList = Counter(newListCrashes)
            od = collections.OrderedDict(sorted(countedList.items()))
            
            for key, value in od.items():
                myDict = (key, value)
                countedCrashes.append(str(value))

            fileOut.write("Date,Temp,Precipitation,Snowfall,Fog,Ice,Crashes\n")
            testZip = zip(newListDate, newListTemp, newListPrecip, newListSnowFall, newListFog, newListIce)

            testZip.sort(key = lambda t: t[0])

            for a,b,c,d,e,f in testZip:
                #print(a,b,c)
                fileOut.write(a)
                fileOut.write(",")
                fileOut.write(b)
                fileOut.write(",")
                fileOut.write(c)
                fileOut.write(",")
                fileOut.write(d)
                fileOut.write(",")
                fileOut.write(e)
                fileOut.write(",")
                fileOut.write(f)
                fileOut.write(",")
                fileOut.write(countedCrashes[index])
                fileOut.write("\n")
                index+=1
                
        newListDate.sort()
        #print(Counter(newListDate))
        #plt.plot(newListDate,newListPrecip)
        #plt.show()
