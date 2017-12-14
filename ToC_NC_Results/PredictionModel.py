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
    print("Prediction Model Created.")
    dateList = []
    file2013 = []
    file2014 = []
    file2015 = []
    file2016 = []
    file2017 = []
    yearPrediction = []
    average = 0
    i = 0
    predictionModel = []

    with open('2016-information-ToC-NC.csv', 'rU') as fin:
        headerLine = next(fin)
        for row in csv.reader(fin):
            dateList.append(row[0])

    with open('2013-information-ToC-NC.csv', 'rU') as fin:
        headerLine = next(fin)
        for row in csv.reader(fin):
            file2013.append(row[1])

    with open('2014-information-ToC-NC.csv', 'rU') as fin:
        headerLine = next(fin)
        for row in csv.reader(fin):
            file2014.append(row[1])

    with open('2015-information-ToC-NC.csv', 'rU') as fin:
        headerLine = next(fin)
        for row in csv.reader(fin):
            file2015.append(row[1])

    with open('2016-information-ToC-NC.csv', 'rU') as fin:
        headerLine = next(fin)
        for row in csv.reader(fin):
            file2016.append(row[1])

    with open('2017-information-ToC-NC.csv', 'rU') as fin:
        headerLine = next(fin)
        for row in csv.reader(fin):
            file2017.append(row[1])

    while(len(file2017) < 365):
        file2017.append(file2016[len(file2017)])

    numZip = zip(file2013, file2014, file2015, file2016, file2017)

    for year2013,year2014, year2015, year2016,year2017 in numZip:
        difference = (float(year2013) + float(year2014) + float(year2015) + float(year2016) + float(year2017))/5
        predictionModel.append(float(difference))

    while (i < 365):
        yearPrediction.append(predictionModel[i])
        i+=1

    #predictedZip = zip(dateList, file2013, file2014, yearPrediction)

    with open('PREDICTION_MODEL_OUTPUT_2018.csv', 'wb') as fileOut:
        fileOut.write("Date,2013, 2014, 2015, 2016, 2017, PREDICTED FOR 2018\n")
        i = 0
        while (i < 365):
            fileOut.write(dateList[i])
            fileOut.write(",")
            fileOut.write(file2013[i])
            fileOut.write(",")
            fileOut.write(file2014[i])
            fileOut.write(",")
            fileOut.write(file2015[i])
            fileOut.write(",")
            fileOut.write(file2016[i])
            fileOut.write(",")
            fileOut.write(file2017[i])
            fileOut.write(",")
            fileOut.write(str(yearPrediction[i]))
            fileOut.write("\n")
            i+=1









