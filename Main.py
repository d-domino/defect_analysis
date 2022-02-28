# Program Individual Project
# Description:
#   Correlation Analysis and Graphing in Python
#   Has random data generation component for demo purposes
# Author: Delaney Domino
# Date: December 4, 2021
# Revised:
#   December 6, 2021

# import library modules here
import pandas as pd
import random as rand
import numpy as np
import string
from datetime import date, datetime
import os
import matplotlib.pyplot as plt
import seaborn as sns
from project_func_library import *

# Define global constants (name in ALL_CAPS)
TEST_FILE_1 = './Test1.csv'
TEST_FILE_2 = './Test2.csv'
TEST_FILE_3 = './Test_merged.csv'
TEST_FILE_4 = './Test_merged_filter.csv'
TEST_FILE_5 = './Test_merged_outliers.csv'


def main():

# Declare Variable types (EVERY variable used in this main program)


# Including the below code to show how I tested this at work -
# This test is with a "real" CSV file - MetalHC_Data (which represents path1 in the graph_1 func test

# This function creates random test files 1 and 2, performs an inner join and saves to Test_File_3
#proj_csv_join(TEST_FILE_1, TEST_FILE_2, TEST_FILE_3, randomgen='both')

# This function graphs data from 'MetalHC_Data' and removes outliers.
#graph_1('VALUE', 'ITEM_VALUE', path1)

# This function takes the Metal HC CSV and a given date cutoff, y var, and limit to come up with a before and after failure rate.
#graph_failrate('./MetalHC_Data.csv', 'ITEM_VALUE', '2021-12-01', 5)

# This test is solely with random generators/random data

    # This function creates random test files 1 and 2, performs an inner join and saves to Test_File_3
    proj_csv_join( TEST_FILE_1, TEST_FILE_2, TEST_FILE_3, randomgen='both' )

    # This function takes random x var - Measurement 1 - and random y var - Measurement 2 - data from  randomly generated join file Test_File_3 and makes several graphs.
    graph_1( 'Measurement 1', 'Measurement 2', TEST_FILE_3 )

    # This function takes a date cutoff, y_var, merged/randomly generated join file, and an upper limit for the y var to calculate before and after failure rates.
    graph_failrate( './Test_merged.csv', 'Measurement 2', '2021-11-01', 5, randgen=True )

# End Program

main()
