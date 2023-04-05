# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 22:24:06 2023

@author: Adedoyin Idris
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# Global Variable
countries = ["United States", "Canada", "Brazil", "Argentina", 
             "United Kingdom", "Australia", "Nigeria", "Ghana", 
             "China", "India"
             ]

# Function to read the dataset
def read_dataset(filename):
    """
        This function reads in a climate change dataset from worldbank,
        and remove all unnecessary columns from the dataframe.
        The function also creates a transposed dataframe which gets cleaned
        after being transposed.
        The function returns two dataframe ne with years as columns and one 
        with countries as columns.
    """
    
    # Reads the csv dataset, passed as an argument into the function
    # Also skip the first four rows of the dataset
    dataframe = pd.read_csv(filename, skiprows=(4))
    
    # A list of the unnecessary columns to remove from the dataframe
    columns_to_drop = ["Country Code", "Indicator Code", "Unnamed: 66"]
    
    # Remove unnecessary columns from the dataframe 
    dataframe = dataframe.drop(labels=columns_to_drop, axis=1)
    
    # Create a multi-index, by making "Country Name" and "Indicator Name"
    # the index of the dataframe and make the years from 1960 t0 2021
    # the columns of the dataframe
    years_as_column_dataframe = dataframe.set_index(["Country Name", 
                                                       "Indicator Name"])
    
    # Transpose the the "years_as_column_dataframe" and store the transposed 
    # dataframe into "country_as_column_dataframe" variable
    country_as_column_dataframe = years_as_column_dataframe.reset_index().T
    
    # Reset the index of the "country_as_column_dataframe"
    country_as_column_dataframe = country_as_column_dataframe.reset_index()
    
    # Clean Dataset: Remove unnecessary row and fill NaN with 0                    
    country_as_column_dataframe = country_as_column_dataframe.drop(1)                       
    country_as_column_dataframe = country_as_column_dataframe.fillna(
        0, inplace=False
        )
    
    return years_as_column_dataframe, country_as_column_dataframe

years_as_column_dataframe, country_as_column_dataframe = \
                                        read_dataset("data.csv")
#print(years_as_column_dataframe)
