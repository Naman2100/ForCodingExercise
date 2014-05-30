import csv
import sys

def findMaximum(columnNum, readerObj):
    if type(columnNum) != int:
        print "The column number should be an integer."
    elif int(columnNum) < 0:
        print "please provide a valid positive value of columnNum"
    elif (readerObj == None):
        print "The reader object provided is invalid."
    else:
        rowNum = 0
        maximum = 0
        year = 0
        month = 0
        for eachRow in readerObj:
            try:
                if maximum <= int(eachRow[columnNum]):
                    maximum = int(eachRow[columnNum])
                    year = int(eachRow[0])
                    month = int(eachRow[1])
            except ValueError:
                print "The data in the input file isn't in the expected format. Please update with valid values and re-initiate."
            except IndexError:
                print "We get some error while processing your request."
            rowNum += 1
        print "For the given company, share touched its maximum value in the year: " + str(year) + " and month of : " + str(month)
        print "The maximum value of share that reached is : " + str(maximum)
    

def readDataFromCSV(filepath, companyName):
    row = 0
    column = 0
    flag = False
    try:
        with open(filepath, "r") as f:
            reader = csv.reader(f)
            for eachRow in reader:
                if row == 0:
                    headerRow = eachRow
                    for col in headerRow:
                        if col == str(companyName):
                            flag = True
                            findMaximum(column, reader)
                        column += 1
                row += 1
            if not flag:
                print "We don't have the company listed with us. Please try with a different company name."
    except IOError:
        print "Can't find the specified file."



def testCase1():
    with open("b.csv", "r") as f:
        reader = csv.reader(f)
        findMaximum("2", reader)

def testCase2():
    with open("b.csv", "r") as f:
        reader = csv.reader(f)
        findMaximum("a", reader)

def testCase3():
    with open("b.csv", "r") as f:
        reader = csv.reader(f)
        findMaximum(-2, reader)    

##POSITIVE CASES
readDataFromCSV("b.csv", "Com4")
readDataFromCSV("b.csv", "Com3")

## Invalid File Name
readDataFromCSV("x.csv", "Com2")

## Company not listed in input CSV
readDataFromCSV("b.csv", "Com5")

## Invalid input (number passed as a string) to the findMaximum function
testCase1()

## Invalid input(Invalid column number) to the findMaximum function
testCase2()

## Invalid input (negative column number) to the findMaximum function
testCase3()

## Invalid reader object to the findMaximum function
findMaximum(2, None)
