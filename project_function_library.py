# Library project_function_library
# Functions Included in Library:
#   proj_csv_join()
#   graph_1()
#   graph_failrate()
# Author: Delaney Domino
# Date: December 4, 2021
# Revised:
#   December 7, 2021

# import library modules here
import pandas as pd
import random as rand
import string
from datetime import date, datetime
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import scipy.stats as sps

# Define global constants (name in ALL_CAPS)
TEST_FILE_1 = './Test1.csv'
TEST_FILE_2 = './Test2.csv'
TEST_FILE_3 = './Test_merged.csv'
TEST_FILE_4 = './Test_merged_filter.csv'
TEST_FILE_5 = './Test_merged_outliers.csv'


# Function proj_csv_join()
# Description:
#   Function to join 2 csv files based on a given list of joining parameters.
#   Function also includes random generator for project demo purposes to create
#   a random version of the csv1 and csv2 files as a way to model the actual data
#   that will be used in a semiconductor work environment.
# Calls:
#   none
# Parameters:
#   path1 - string
#   path2 - string
#   paramlist - list of strings, default is 'Lot_ID' and 'Date'
#   randomgen - optional string with accepted value 'both'
#   default value of randomgen is 0
#   fileDefault - optional bool, set to True to use test file names as CSV paths
# Returns:
#   merged_data

def proj_csv_join(path1, path2, path3, paramlist=['Lot_ID', 'Date'], randomgen="0", fileDefault=True):
    # Declare Local Variable types (NOT parameters)
    df_1 = pd.DataFrame()
    df_2 = pd.DataFrame()
    merged_data = pd.DataFrame()
    df_random = pd.DataFrame()
    letters_and_num = str()
    year = int()
    month = int()
    month2 = int()
    day = int()
    lot_id = str()
    lot_id_list = list()
    date1 = str()
    date_str = str()
    date_list = list()
    measurement_1 = float()
    measurement_1_list = list()
    measurement_2 = float()
    measurement_2_list = list()
    counter = int()
    month_30 = list()
    month_31 = list()
    file_1 = str()
    file_2 = str()
    file_3 = str()

    # Set random seed for 1st round of generation
    rand.seed(50)

    # Initialize values
    year = 2021
    month_30 = [ 9, 4, 6, 7, 11 ]
    month_31 = [ 1, 3, 5, 8, 9, 12 ]

    # Define class for custom error
    class CustomError( Exception ):
        pass

    # Assess if fileDefault is False
    # if fileDefault is False and randomgen == 1, use input values for csv paths
    # Else, use default values for csv paths
    if fileDefault == False and randomgen == "both":
        file_1 = str( input('Please input a path for random file 1 ending in .csv: ') )
        file_2 = str( input('Please input a path for random file 2 ending in .csv: ') )
        file_3 = str( input('Please input a path for the random join file ending in .csv: ') )
    else:
        file_1 = path1
        file_2 = path2
        file_3 = path3
    # end if

    # Loop to assess if randomgen is needed
    if randomgen != "0":

        if randomgen == 'both':
            # generate a random dataframe for the first file
            # dataframe will have lot_id (5 letter/num string to represent a manufacturing entity),
            # date, and measurement 1

            for counter in range(50):

                # Create a string of possible letter and number choices
                letters_and_num = string.ascii_uppercase + string.digits

                # Initialize lot id
                lot_id = ""

                # For loop to generate random 5 character lot ids
                for lot_id_2 in range(5):
                    lot_id_2 = rand.choice( letters_and_num )
                    lot_id = lot_id + lot_id_2
                # end for

                # Generate random dates
                month = rand.randint( 1, 12 )
                day = rand.randint( 1, 31 )

                # Test if month is 30 day month
                for month2 in month_30:
                    if month == month2:
                        # Adjust day if needed
                        if day > 30:
                            day = day - 1
                        # end if
                    # end if

                # Test if month is February
                if month == 2:
                    # Adjust day if needed
                    if day > 28:
                        day = 28
                    # end if
                # end if

                date1 = date( year, month, day )
                date_str = date1.strftime( "%m/%d/%Y" )

                # Generate random measurement values
                measurement_1 = rand.uniform( 0, 100 )

                # Append values to list
                lot_id_list.append( lot_id )
                date_list.append( date_str )
                measurement_1_list.append( measurement_1 )
            # end for

            # create 1st dataframe with values
            df_1[1] = lot_id_list
            df_1[2] = date_list
            df_1[3] = measurement_1_list

            # create 2nd dataframe with values that are the same as 1st dataframe
            # date and lot_id will be the same as 1st dataframe
            # These values are the same to facilitate join for the randomgen case.
            df_2[1] = lot_id_list
            df_2[2] = date_list

            # Add column labels for dataframe 1
            df_1.columns = ['Lot_ID', 'Date', 'Measurement 1']

            # write dataframe to csv, remove index columns
            df_1.to_csv( file_1, index=False )

            # Change seed to get new values for measurement_2
            rand.seed(49)

            for counter in range(50):
                # Generate random measurement values
                measurement_2 = rand.uniform( 0, 100 )

                # Append value to measurement_2 list
                measurement_2_list.append( measurement_2 )
            # end for

            # Add measurement 2 values to 2nd dataframe
            df_2[3] = measurement_2_list

            # Rename columns for dataframe 2
            df_2.columns = ['Lot_ID', 'Date', 'Measurement 2']

            # write dataframe 2 to csv
            df_2.to_csv( file_2, index=False )


        else:
            raise CustomError("The only accepted values of randomgen are 'both' and '0'")
        # End if
    # End if

    df_1 = pd.read_csv( path1 )
    df_2 = pd.read_csv( path2 )
    merged_data = pd.merge( df_1, df_2, how='inner', on=paramlist )
    merged_data.to_csv( file_3, index=False )

    # End if

    # Return the return variable, if any
    return merged_data


# } Function proj_csv_join()


# Function graph_1()
# Description:
#   Function to create graphs based on a given x parameter, y parameter, and CSV file.
#   Function creates a histogram, boxplot, identifies and filters out outliers.
#   Function also performs a least squares regression and calculates correlation coefficient (r)
#   and coefficient of variability (r^2) to assess the strength of a linear correlation.
#   It displays r and r^2 on the resulting scatterplot.
#   Function also saves both filtered data (no outliers) and outliers to two
#   new CSV files.
# Calls:
#   none
# Parameters:
#   x_var - string
#   y_var - string
#   CSV_file - string
#   item_id - optional string to filter to a specific measurement type
#             which is used in real application when multiple types of measurements
#             are in CSV file
#   fileDefault - optional bool, set to True to use test file names as CSV paths
# Returns:
#


def graph_1( x_var, y_var, CSV_file, item_id="", fileDefault=True ):
    # Declare Local Variable types (NOT parameters)
    df_new = pd.DataFrame()
    df_outlier = pd.DataFrame()
    quartile_1 = float()
    quartile_3 = float()
    interquartile_range = float()
    upper_bound = float()
    lower_bound = float()
    x_var_max = int()
    y_var_max = float()
    current_axis = object()
    linreg_obj = object()
    line_eqn = str()
    line_eqn_eval = str()
    r_str = str()
    rsq_str = str()
    file_4 = str()
    file_5 = str()
    file_filtered = str()

    # Create dataframe from CSV
    df_new = pd.read_csv( CSV_file )

    # Assess if filedefault is False
    # if filedefault is False and randomgen == 1, use input values for csv paths
    # Else, use default values for csv paths
    if fileDefault == False:
        file_4 = str( input('Please input a path that the filtered file will save to ending in .csv: ') )
        file_5 = str( input('Please input a path that the outlier file will save to ending in .csv: ') )
    else:
        file_4 = TEST_FILE_4
        file_5 = TEST_FILE_5
    # end if

    # X_var is going to be a counter variable, and y_var is a measurement of defectivity
    # create histogram
    plt.hist( df_new[y_var] )
    plt.pause(5)
    plt.close()

    # create boxplot
    sns.boxplot( df_new[y_var] )
    plt.show()
    plt.pause(2)
    plt.close()

    # Identify and filter out outliers by calculating IQR (interquartile range)
    quartile_1 = np.percentile( df_new[y_var], 25, interpolation='midpoint' )
    quartile_3 = np.percentile( df_new[y_var], 75, interpolation='midpoint' )
    interquartile_range = quartile_3 - quartile_1

    # Filter out outliers with upper and lower bound
    upper = quartile_3 + 1.5 * interquartile_range
    lower = quartile_1 - 1.5 * interquartile_range

    # Create new dataframe with just outliers
    df_outlier = df_new[ df_new[y_var] > upper ]
    df_outlier = df_outlier.append( df_new[df_new[y_var] < lower] )

    # Remove outliers from previous dataframe
    df_new = df_new[ lower < df_new[y_var] ]
    df_new = df_new[ df_new[y_var] < upper ]

    # Filter out item ID, which represents measurement type
    if item_id != "":
        df_new = df_new[ df_new['ITEM_ID'] == item_id ]
    # end if

    # Find x and y var maxes and mins
    x_var_min = df_new[x_var].min()
    x_var_max = df_new[x_var].max()
    y_var_max = df_new[y_var].max()
    y_var_min = df_new[y_var].min()

    # Creates a scatter plot with outliers filtered out
    plt.scatter( df_new[x_var], df_new[y_var] )

    # Get current axis, set axis limits, and add axis labels
    current_axis = plt.gca()
    current_axis.set_xlim( [x_var_min, x_var_max] )
    current_axis.set_ylim( [y_var_min, y_var_max] )
    current_axis.set_ylabel(y_var)
    current_axis.set_xlabel(x_var)

    # Calculate linear least squares regression using scipy linregress
    # Will return the following:
    # slope, intercept, r_value, p_value, std_err
    linreg_obj = sps.linregress( df_new[x_var], df_new[y_var], alternative='greater' )

    # Format array values as equation string for later plotting
    line_eqn = str(linreg_obj[0]) + '*df_new[x_var]+' + str(linreg_obj[1])

    # Evaluate equation
    line_eqn_eval = eval( line_eqn )

    # Slice r and use to calculate r-sq with 5 decimal places
    # Convert to string
    rsq = round( float(linreg_obj[2]) ** 2, 5 )
    rsq_str = str(rsq)
    r_str = str( round(linreg_obj[2], 5) )

    # Plot line on existing scatter plot and adjust top to have room
    # for multi-line title with r and r-sq values
    plt.plot( df_new[x_var], line_eqn_eval, color='red' )
    plt.tight_layout()
    plt.subplots_adjust(top=0.84)
    plt.title('Scatter with outliers filtered out' + '\n' + 'R is ' + r_str + '\n' + 'R^2 is ' + rsq_str)

    # Show scatter plot
    plt.show()

    # Pause and hold
    plt.pause(5)
    plt.close()

    # Write filtered data file to csv
    df_new.to_csv( file_4, index=False )

    # Write outlier data file to csv
    df_outlier.to_csv( file_5, index=False )

    # Return the return variable, if any


# } Function graph_1()


# Function graph_failrate()
# Description:
#   Function to analyze the before and after failure rate for a dataset.
#   Data contains dates and a y variable that represents defect data.
#   Function calculates before and after failure rate based on given date cutoff
#   and upper control limit for y variable.
#   It produces a scatter plot of defect data vs. date with date cutoff and
#   upper control limit plotted.
#   It also produces 2 tables of before and after summary statistics with
#   count, median, mean, and failure rate for the two datasets.
# Calls:
#   none
# Parameters:
#   CSV_file - string
#   y_var - string
#   date_cutoff - string, assumes valid date formatted year-month-day
#   upper_control - int
#   randgen - optional bool, indicates if randgen was used for the CSV_file
# Returns:
#

def graph_failrate( CSV_file, y_var, date_cutoff, upper_control, randgen=False ):
    # Declare Local Variable types (NOT parameters)
    df_new = pd.DataFrame()
    df_before = pd.DataFrame()
    df_after = pd.DataFrame()
    date_piece = str()
    date_stripped = str()
    year = int()
    year_str = str()
    month_str = str()
    day_str = str()
    date1 = str()  # supposed to be date
    date_count = int()
    date_str = str()
    len_before = int()
    len_after = int()
    fail_before = int()
    fail_after = int()
    fail_rate_before = int()
    fail_rate_after = int()
    fail_rate_before_str = str()
    fail_rate_after_str = str()
    mean_before_str = str()
    mean_after_str = str()
    med_before_str = str()
    med_after_str = str()
    count_before_str = str()
    count_after_str = str()
    index_new = int()
    date_key = str()

    # Declare Local Variable types (NOT parameters)
    df_new = pd.DataFrame()
    df_before = pd.DataFrame()
    df_after = pd.DataFrame()

    # Create dataframe from CSV
    df_new = pd.read_csv( CSV_file )

    # Test to see if date in proper format with year
    date_piece = date_cutoff[0:4]
    while date_piece != '2021':
        date_cutoff = str( input('Please enter a date in the format YYYY-MM-DD with 2021 being the accepted year: ') )
        date_piece = date_cutoff[0: 4]
    # end while

    # Test to see if date in the proper format with special characters
    date_piece = date_cutoff[4]
    while date_piece != "-":
        date_cutoff = str( input('Please enter a date with hyphens in the format YYYY-MM-DD with 2021 being the accepted year: '))
        date_piece = date_cutoff[4]
    # end while

    # Initialize year, month, day strings
    year_str = ""
    month_str = ""
    day_str = ""

    # Format date
    # Strip '-' from date
    date_stripped = date_cutoff.replace("-", "")

    # get year from date
    for date_count in range(4):
        year_str += date_stripped[date_count]
    # end for

    # get month from date
    for date_count in range(4, 6):
        month_str += date_stripped[date_count]
    # end for

    # get day from date
    for date_count in range(6, 8):
        day_str += date_stripped[date_count]
    # end for

    # Convert year, month, day to int
    year = int( year_str )
    month = int( month_str )
    day = int( day_str )

    # Convert date into date objects
    date1 = date( year, month, day )
    date_str = date1.strftime("%m/%d/%Y")

    # Perform the following if randgen == True:
    if randgen == True:

        # Convert date column in df_new to datetime
        df_new['Date'] = pd.to_datetime( df_new['Date'] )

        # Create before and after dataframes using date1
        df_before = df_new[df_new['Date'] < date_str]
        df_after = df_new[df_new['Date'] > date_str]

    # Assume using my example file
    else:
        for index_new in range(df_new.shape[0]):
            df_new['TRACKSUB'][index_new] = df_new['TRACKSUB'][index_new][0:10]

        # end for

        # Convert date column in df_new to datetime
        df_new['Date'] = pd.to_datetime(df_new['TRACKSUB'])

        # Create before and after dataframes using date1
        df_before = df_new[df_new['Date'] < date_str]
        df_after = df_new[df_new['Date'] > date_str]

        # End for
    # End if

    # # Calculate before and after failure rates # #

    # Get length of each data frame
    len_before = df_before.shape[0]
    len_after = df_after.shape[0]

    # Create a fail column in each DataFrame
    df_before['Fail'] = df_before[y_var] > upper_control
    df_after['Fail'] = df_after[y_var] > upper_control

    # Calculate number of fail rows
    fail_before = df_before[df_before['Fail'] == True].shape[0]
    fail_after = df_after[df_after['Fail'] == True].shape[0]

    # Calculate fail rate before and after
    fail_rate_before = int(fail_before / len_before * 100)
    fail_rate_after = int(fail_after / len_after * 100)

    # Display strings of failure rates
    fail_rate_before_str = str(fail_rate_before)
    fail_rate_after_str = str(fail_rate_after)
    print('The before fail rate is: ' + fail_rate_before_str + ' %')
    print('The after fail rate is: ' + fail_rate_after_str + ' %')

    # #Produce a scatter plot of defect data versus date ##
    plt.figure(4)
    plt.scatter(df_new['Date'], df_new[y_var])
    plt.title('Scatter plot of defect data vs. date')
    plt.xticks( rotation=90 )
    plt.axvline( date1, color='green' )  # add vertical line with date_cutoff
    plt.axhline( upper_control, color='red' )  # add horizontal line with upper_control
    plt.show()

    # Calculate summary statistics
    mean_before_str = str( round(df_before[y_var].mean(), 3) )
    mean_after_str = str( round(df_after[y_var].mean(), 3) )
    med_before_str = str( round(df_before[y_var].median(), 3) )
    med_after_str = str( round(df_after[y_var].median(), 3) )
    count_before_str = str(len_before)
    count_after_str = str(len_after)

    # Produce table with before and after statistics
    print('Before Data')
    print('Failure Rate: ', fail_rate_before_str)
    print('Median: ', med_before_str)
    print('Mean: ', mean_before_str)
    print('Count: ', count_before_str)
    print()
    print('After Data')
    print('Failure Rate: ', fail_rate_after_str)
    print('Median: ', med_after_str)
    print('Mean: ', mean_after_str)
    print('Count: ', count_after_str)

# } Function graph_failrate()

# End Module project_func_library


