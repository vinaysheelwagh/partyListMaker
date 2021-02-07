import pytest
import os
from app import *

# constants

WRITEFILE = "res/testWrite.txt"
OFFICE = ( 53.339428, -6.257664)
TCD = (53.34373252828094, -6.254788673748609)
ATHLONE = (53.431853050358264, -8.05028429212073)
DISTANCE = 100
FileRows = 32
NOLIST = [{"latitude": "51.8856167", "user_id": 2, "name": "Ian McArdle", "longitude": "-10.4240951"},
            {"latitude": "51.92893", "user_id": 1, "name": "Alice Cahill", "longitude": "-10.27699"}]
ALLLIST = [{"latitude": "51.8856167", "user_id": 2, "name": "Ian McArdle", "longitude": "-10.4240951"},
            {"latitude": "51.92893", "user_id": 1, "name": "Alice Cahill", "longitude": "-10.27699"},
           {"latitude": "53.1302756", "user_id": 5, "name": "Nora Dempsey", "longitude": "-6.2397222"},
           {"latitude": "53.2451022", "user_id": 4, "name": "Ian Kehoe", "longitude": "-6.238335"}]
TUPLES = [(5, 'Nora Dempsey'), (4, 'Ian Kehoe')]


# Helpers


def verify_answer(answer, expected):
    assert answer == expected

# Test Cases


def test_readFile():
    """test that readFile correctly reads and parses file"""
    test_file = "res/customers.txt"
    result = readFile(test_file)
    totalRows = len(result)
    verify_answer(totalRows, FileRows)

test_readFile()

def test_withinDistance_Yes():
    """test that withinDistance correctly filters within distance customers"""
    tcdInvite = withinDistance(TCD, OFFICE, DISTANCE)
    verify_answer(tcdInvite, True)


def test_withinDistance_No():
    """test that withinDistance correctly filters out customers who are too far away"""
    athloneNoInvite = withinDistance(ATHLONE, OFFICE, DISTANCE)
    verify_answer(athloneNoInvite, False)


def test_filterCustomers_Yes():
    """test that filterCustomers correctly compiles filtered list of customers"""
    allCustomers = filterCustomers(ALLLIST, OFFICE, DISTANCE)
    verify_answer(allCustomers, [(5, 'Nora Dempsey'), (4, 'Ian Kehoe')])


def test_filterCustomers_No():
    """test that filterCustomers correctly filters out all customers too far away"""
    noCustomers = filterCustomers(NOLIST, OFFICE, DISTANCE)
    verify_answer(noCustomers, [])


def test_sortFilteredCustomers():
    """test that sortFilteredCustomers correctly sorts customers by id"""
    sortedTuples = sortFilteredCustomers(TUPLES)
    verify_answer(sortedTuples, [(4, 'Ian Kehoe'), (5, 'Nora Dempsey')])


def test_writeOutput():
    """test that writeOutput correctly clears and writes new output text file"""
    writeFile = os.path.join(WRITEFILE)
    with open(writeFile, 'w') as f:
        f.truncate(0)
        f.write("gibberish\n")
    writeOutput(writeFile, TUPLES)
    f = open(writeFile, 'r')
    verify_answer(f.read(), '5 Nora Dempsey\n4 Ian Kehoe\n')