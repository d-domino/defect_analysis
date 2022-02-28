# defect_analysis
3 defect analysis functions 

My project will explore statistical analysis and graphing using Python. The project will contain three functions – a joining function and two graphing functions. 

The joining function will perform an inner join on two separate datasets based on a specific set of parameters. 
It will also have the option to import two existing CSV files as the datasets to join, or to use a random generator to create either one or both datasets. 
The joined dataset will be saved as a new CSV. 

The first graphing function will graph the joined dataset based on inputs of x and y variables, and a CSV file name. 
It will create a histogram, identify and filter out outliers, create a scatterplot with the outliers filtered out, perform a least squares regression, 
and calculate the correlational coefficient (r) and coefficient of variability (r2) to assess whether the data shows a strong or weak linear correlation. 
It will display r and r2 on the resulting scatterplot, and save both the filtered data and the outliers to new CSV files. 

The second graphing function will analyze the before and after “failure rate” for a pre-existing dataset.  The dataset will contain dates and a y variable that represents 
defect data. It will take a date cutoff and upper control limit (or defining limit for failure) for the defect data as inputs. The function will then calculate a before failure 
rate and an after failure rate based on the given date cutoff. It will produce a scatter plot of defect data vs. date that contains the plotted upper 
control limit and date cutoff. It will also produce a table with the following information for before and after date cutoff: 
failure rate, median of defect data, mean of defect data, and count of  data points.

The purpose of my project is to simulate graphing and statistical analysis that I perform in the semiconductor manufacturing industry. 
There is a need to be able to join data from different systems (which the two datasets represent) and identify the percent variation in a y variable that can be explained 
by a linear relationship with x, or whether two variables have a strong or weak linear correlation. Python will help me quickly visualize the data and filter it 
appropriately to draw conclusions. 
