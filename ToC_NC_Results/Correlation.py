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
    print("Completed Calculating Correlation. Filename: (YEAR)-correlation.csv")
    dateColumn = []
    temperatureSet = []
    crashSet = []
    newTemperatureSet = []
    newCrashSet = []

    with open('2017-information-ToC-NC.csv', 'rU') as fin:
        headerLine = next(fin)
        for row in csv.reader(fin):
            dateColumn.append(row[0])  
            temperatureSet.append(row[3])
            crashSet.append(row[6])
 

        for item in temperatureSet:
            newTemperatureSet.append(float(item))
            #if (item == 'Yes'):
                #newTemperatureSet.append(1)
            #else:
                #newTemperatureSet.append(0)

        for item in crashSet:
            newCrashSet.append(float(item))

        #medianListTemp = sorted(newTemperatureSet)
        #avgListCrash = np.mean(newCrashSet)

        #stdevTemp = np.std(medianListTemp)

        #print(stdevTemp)
        #print(avgListCrash)
        print(np.corrcoef(newTemperatureSet, newCrashSet)[0,1])

        """with open('2017-information-Denver.csv', 'wb') as fileOut:
            countedList = Counter(newListCrashes)
            od = collections.OrderedDict(sorted(countedList.items()))
            
            for key, value in od.items():
                myDict = (key, value)
                countedCrashes.append(str(value))

            while (len(countedCrashes) < 365):
                countedCrashes.append("NaN")
                #print(len(countedCrashes))

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
                        """
        #newListDate.sort()
        #print(Counter(newListDate))
        #plt.plot(newListDate,newListPrecip)
        #plt.show()
