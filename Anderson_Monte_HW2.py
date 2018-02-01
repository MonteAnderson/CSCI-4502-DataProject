# Monte Anderson
# Fall 2017, CSCI 4502/5502, Homework 2 
# 
# Based on historical quotes from http://www.nasdaq.com/quotes/
# Be sure to follow the exact instruction for the output format 
#

import argparse
import csv
import math
import numpy as np
import scipy as stats

def normalization (fname, attr, normType):

    #Here, we assign the values to the given input. This was done to make it easier 
    # later on to refer to the attribute by column number.

    ithAttr = 0

    if attr == 'close':
        ithAttr = 2

    elif attr == 'volume':
        ithAttr = 3

    elif attr == 'open':
        ithAttr = 4

    elif attr == 'high':
        ithAttr = 5

    elif attr == 'low':
        ithAttr = 6

    #Here we declare all the variables, and set out min/max values.

    total = 0
    numObj = 0
    listOfNumbers = []
    minValue = math.inf
    maxValue = -math.inf


    #Opening the file, we need to get the list of values from the column, in order to observe them.

    with open(fname) as fin:
        headerLine = next(fin)

     
        for row in csv.reader(fin):
            numObj+=1
            print(row[ithAttr-1])
            if (float(row[ithAttr-1]) < float(minValue)):
                minValue = float(row[ithAttr-1])

            if (float(row[ithAttr-1]) > float(maxValue)):
                maxValue = float(row[ithAttr-1])
            
            total+=float(row[ithAttr-1])
            listOfNumbers.append(row[ithAttr-1])


    newListOfNumbers = []
    normalizedList = []
    normalizedMinMaxList = []

    for item in listOfNumbers:
        float(item)
        newListOfNumbers.append(float(item))
    

    medianList = sorted(newListOfNumbers)

    stdev = np.std(medianList)
    median =  np.median(medianList)
    mean = total/numObj

    #Here, we calculate the z-score for the new list of numbers (all floats). 
    for x in newListOfNumbers:
        z = float((x - mean)/stdev)
        normalizedList.append(z)
 
    #We do the same for minmax here, using the formula for every value in our list.
    for y in newListOfNumbers:
        minmaxNum = ((y - minValue)/(maxValue - minValue))
        normalizedMinMaxList.append(minmaxNum) 

    printX = 0

    if normType == 'z_score' :
        while printX < len(newListOfNumbers):
            #print(normalizedMinMaxList[printX])
            print("Original = ", listOfNumbers[printX], "\t| ZScore = ", normalizedList[printX])
            printX += 1


    if normType == 'min_max' :
        while printX < len(newListOfNumbers):
            #print(normalizedMinMaxList[printX])
            print("Original = ", listOfNumbers[printX], "\t| Min_max = ", normalizedMinMaxList[printX])
            printX += 1

    #print(newListOfNumbers)

    '''
    Input Parameters:
        fname: Name of the csv file contiaining historical quotes
        attr: The attribute to be normalized 
        normType: The type of normalization 
    Output:
        For each line of quotes in the input file, print the original value and normalized value of the specific attribute, separated by <TAB>  
    '''


def correlation (fname1, attr1, fname2, attr2):

    #Same thing in the other function, but now doing it twice.

    ithAttr1 = 0
    listOfNumbers1 = []

    ithAttr2 = 0
    listOfNumbers2 = []

    if attr1 == 'close':
        ithAttr1 = 2
    if attr2 == 'close':
        ithAttr2 = 2

    if attr1 == 'volume':
        ithAttr1 = 3
    if attr2 == 'volume':
        ithAttr2 = 3

    if attr1 == 'open':
        ithAttr1 = 4
    if attr2 == 'open':
        ithAttr2 = 4

    if attr1 == 'high':
        ithAttr1 = 5
    if attr2 == 'high':
        ithAttr2 = 5

    if attr1 == 'low':
        ithAttr1 = 6
    if attr2 == 'low':
        ithAttr2 = 6


    with open(fname1) as fin:
        headerLine = next(fin)
        for row in csv.reader(fin):
            listOfNumbers1.append(row[ithAttr1-1])


    with open(fname2) as fin2:
        headerLine = next(fin2)
        for row in csv.reader(fin2):
            listOfNumbers2.append(row[ithAttr2-1])


    newListOfNumbers1 = []
    newListOfNumbers2 = []

    #Having to make a new list from just the float numbers (instead of strings) from the lists.
    for item in listOfNumbers1:
        float(item)
        newListOfNumbers1.append(float(item))

    for item in listOfNumbers2:
        float(item)
        newListOfNumbers2.append(float(item))


    #Fortunantly, python/numpy has a built in function to compute the correlation coefficient, so I just used that.
    print("\nCoeff: ", np.corrcoef(newListOfNumbers1, newListOfNumbers2)[0,1], "\n")


    '''
    Input Parameters:
        fname1: name of the first csv file containing historical quotes
        attr1: The attribute to consider in the first csv file (fname1)
        fname2: name of the second csv file containing historical quotes
        attr2: The attribute to consider in the second csv file (fname2)
        
    Output:
        correlation coefficient between attr1 in fname1 and attr2 in fname2
    '''

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Data Mining HW2')
    parser.add_argument('-f1', type=str,
                            help="First csv file. Use only f1 for Q1.", 
                            required=True)
    parser.add_argument("-f2", type=str, 
                            help="Second csv file. Used for Q2.", 
                            required=False)
    parser.add_argument("-n", type=str, 
                            help="Type of Normalization. Select either min_max or z_score",
                            choices=['min_max','z_score'],
                            required=False)
    parser.add_argument("-a1", type=str, 
                            help="Type of Attribute for fname1. Select either open or high or low or close or volume",
                            choices=['open','high','low','close','volume'],
                            required=False)
    parser.add_argument("-a2", type=str, 
                            help="Type of Attribute for fname2. Select either open or high or low or close or volume",
                            choices=['open','high','low','close','volume'],
                            required=False)


    args = parser.parse_args()

    if ( args.n and args.a1 ):
        normalization(args.f1, args.a1, args.n)
    elif ( args.f2 and args.a1 and args.a2):
        correlation(args.f1, args.a1, args.f2, args.a2)
    else:
        print ("Need input in the following form:\nHW2_PythonTemplate.py -f1 <filename1> -a1 <attribute> -n <normalizationType> or \nHW2_PythonTemplate.py -f1 <filename1> -a1 <attribute> -f2 <filename2> -a2 <attribute>")
