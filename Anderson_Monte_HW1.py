import argparse
import csv
import math

#Because we were allowed to use pandas, I assumed we were also allowed to use numpy, as they do 
#almost the same things that we need.

import numpy as np

class DataSet:
    def __init__(self,location):
        with open (location, "rU") as csvfile:
            self.readData=csvfile.readlines();


def calculate( dataFile, ithAttr):

    with open(dataFile) as fin:

        headerLine = next(fin)

        '''-----------------------------------------------------
           total is the total sum of the column. 
           numObj is the total number of objects in the column.
           minValue is the minimum value. We set this to infinity first, because that allows any number to become
                  the next minimum value.
           maxValue is the maximum value. We set this to be negative infinity first, because any number can now
                  become the largest number.
       
           listOfNumbers is a dictionary that we use to append our values of the columns to. This will allow us to
                  find the statistical data that we need, like median, Q1, Q2, etc.

           Because these values are constantly changing, it is easier to declare them besides the for loop, for easier
                  reference later on.
        -----------------------------------------------------'''

        total = 0
        numObj = 0
        minValue = 100000
        maxValue = -100000

        listOfNumbers = []

        '''-----------------------------------------------------

           Here, we begin the for loop that will loop through, grab the ithAttr element of a row (we need ithAttr-1,
           because arrays start at 0, but we reference them starting at 1), and then append that item to our dictionary.
           We also find if we have a new minimum or maximum number.

        -----------------------------------------------------'''
        for row in csv.reader(fin):
            numObj+=1

            if (float(row[ithAttr-1]) < float(minValue)):
                minValue = row[ithAttr-1]

            if (float(row[ithAttr-1]) > float(maxValue)):
                maxValue = row[ithAttr-1]

            #print(row[ithAttr-1])
            listOfNumbers.append(row[ithAttr-1])

            total+=float(row[ithAttr-1])
            #statistics.median(fin)

    
    count = 0
    mean = total/numObj
    newListOfNumbers = []
    Q1Dict = []
    Q3Dict = []

    '''
        For some reason, it was casting some of the dictionary items as strings, but not all of them. To fix that,
            I decided to manually cast all elements as floats in the dictionary, then make a new dictionary from this.
    '''

    for item in listOfNumbers:
        float(item)
        newListOfNumbers.append(float(item))


    #print(newListOfNumbers)
    medianList = sorted(newListOfNumbers)
   # print(medianList)



    lenMedianList = int(len(medianList))/2
    #print(lenMedianList)

    '''
        These dictionaries contain the first half and second half of the original dictionary. This is because
            we need to find Q1 and Q3, which are the medians of the first and second half of the dictionary. To me,
            it made the most sense to just split them, then do the median of those new dictionaries.
    '''

    Q1Dict = medianList[:int(lenMedianList)]
    Q3Dict = medianList[int(lenMedianList)+1:]

    '''
        Here, we actually declare the median values for each half of the dictionary. 
    '''

    Q1 = np.median(Q1Dict)
    Q3 = np.median(Q3Dict)


    IQR = float(float(Q3) - float(Q1))
    median =  np.median(medianList)

    #Casting min/max values to floats, as they were still strings from the dictionary.
    minValue = float(minValue)
    maxValue = float(maxValue)
    stdev = np.std(medianList)

    '''
    print("\n--------------------------")
    print("Total: \t\t" + str(total))
    print("Number of Objects: \t" + str(numObj))
    print("Min Value: \t" + str(minValue))
    print("Max Value: \t" + str(maxValue))
    print("Mean: \t\t" + str(mean))
    print("Stand. Dev: " + str(stdev))
    print("Q1: " + Q1)
    print("Median: " + median)
    print("Q3: " + Q3)
    print("IQR: " + str(IQR))
    print("--------------------------\n")
    '''


    '''
    Input Parameters:
        dataFile: The dataset file.
        ithAttre: The ith attribute for which the various properties must be calculated.

    Default value of 0,infinity,-infinity are assigned to all the variables as required. 
    Objective of the function is to calculate:  N (number of objects), min, max, mean, standard deviation, Q1, median, Q3, IQR
    '''

    #numObj, minValue, maxValue, mean, stdev, Q1, median, Q3, IQR = [0,"inf","-inf",0,0,0,0,0,0]
    
    #YOUR TASK: Write code to assign the values to the respective variables.

    return numObj, minValue, maxValue, mean, stdev, Q1, median, Q3, IQR

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Data Mining HW1')
    parser.add_argument('--i', type=int,
                            help="ith attribute of the dataset (2 <= i <= 29)", 
                            default=5,
                            choices=range(2,30),
                            required=True)
    parser.add_argument("--data", type=str, 
                            help="Location of the dataset file",
                            default="energydata_complete.csv", 
                            required=True)
    args = parser.parse_args()
    data = DataSet(args.data)

    print ','.join(map(str,calculate(args.data,args.i)))
