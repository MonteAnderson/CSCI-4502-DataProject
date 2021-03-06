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

    with open('accidents_uk.csv', 'rU') as fin:
        headerLine = next(fin)
        for row in csv.reader(fin):
            if ('2015' in row[0]):
                item= str(row[0])
                print(item)
                newListCrashes.append(str(item[:10]))      
        newListCrashes.sort()
        #print(newListCrashes)
        
    with open('Denver-weather.csv', 'rU') as fin:
        headerLine = next(fin)
        for row in csv.reader(fin):
            if ('2017' in row[2]):
                newListDate.append(str(row[2]))
	        newListTemp.append(row[6])
                newListPrecip.append(row[4])
                newListSnowFall.append(row[5])
                newListFog.append(row[6])
                newListIce.append(row[6])


        with open('2017-information-UK.csv', 'wb') as fileOut:
            countedList = Counter(newListCrashes)
            od = collections.OrderedDict(sorted(countedList.items()))
            #print(countedList)
            for key, value in od.items():
                myDict = (key, value)
                countedCrashes.append(str(value))

            while (len(countedCrashes) <= 365):
                countedCrashes.append("NaN")
                #print(len(countedCrashes))

            fileOut.write("Date,Temp,Precipitation,Snowfall,Fog,Ice,Crashes\n")
            testZip = zip(newListDate, newListTemp, newListPrecip, newListSnowFall, newListFog, newListIce)

            testZip.sort(key = lambda t: t[0])
            print(len(countedCrashes))
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
                print(countedCrashes[index])
                fileOut.write("\n")
                if index < 365:
                    index+=1
                #print(index)     
        newListDate.sort()
        #print(Counter(newListDate))
        #plt.plot(newListDate,newListPrecip)
        #plt.show()
