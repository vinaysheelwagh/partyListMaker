import sys
import os
import demjson
from geopy.distance import great_circle

def readFile( dataFile):
    """reads file and parses data to the customer list"""
    customerList = []
    with open(dataFile, 'r') as f:
        for line in f:
            data = demjson.decode(line)
            customerList.append(data)
    return customerList

def withinDistance( a, b, distance):
    """returns true if customer is within the specifed distance of the office
    using great-circle distance"""
    return great_circle(a, b).km < distance

def filterCustomers( customerList, office, distance):
    """filters customer list by distance and appends party goers to final party list"""
    finalList = []
    for customer in customerList:
        home = (float(customer["latitude"]), float(customer["longitude"]))
        if withinDistance(office, home, distance):
            finalList.append((customer["user_id"], customer["name"]))
    return finalList

def sortFilteredCustomers( finalList):
    """sorts party goers by id"""
    finalList = sorted(finalList, key=lambda x: x[0])
    return finalList

def writeOutput( writeFile, finalList):
    """writes sorted list of party goers to output.txt file"""
    with open(writeFile, 'w') as f:
        f.truncate(0)
        for entry in finalList:
            f.write(str(entry[0]) + " " + str(entry[1]) + "\n")


def evaluate(OFFICE, MAXDISTANCE, DATAFILE, WRITEFILE):
    """evaluate party list with default values"""

    customerList = readFile(DATAFILE)
    finalList = filterCustomers(customerList, OFFICE, MAXDISTANCE)
    finalList = sortFilteredCustomers(finalList)
    writeOutput(WRITEFILE, finalList)


def main():
    OFFICE = ( 53.339428, -6.257664)
    MAXDISTANCE = 100
    DATAFILE = "res/customers.txt"
    WRITEFILE = "./output.txt"
    evaluate(OFFICE, MAXDISTANCE, DATAFILE, WRITEFILE)


if __name__ == "__main__":
    main()