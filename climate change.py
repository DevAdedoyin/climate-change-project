# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 22:24:06 2023

@author: Adedoyin Idris
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Global Variable
countries = ["Argentina", "Australia", "Brazil", "Canada", 
             "China", "United Kingdom", "Ghana", "India", 
             "Nigeria", "United States"
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
    
    # Clean the transposed dataframe by removing row not needed and 
    # filling NaN cells with 0
    #country_as_column_dataframe = country_as_column_dataframe.drop(1)                       
    country_as_column_dataframe = country_as_column_dataframe.fillna(
        0, inplace=False
        )
    
    return years_as_column_dataframe, country_as_column_dataframe

years_as_column_dataframe, country_as_column_dataframe = \
                                        read_dataset("data.csv")


# This function explore the statistical properties of Co2 emissions
def co2_emission():
    """
        This function explores the statistical properties of the 
        "CO2 emissions from liquid fuel consumption (kt)" indicator. 
        It also plots a graph showing the rate of emission of "C02 from
        liquid fuel consumption (kt)" for every 10 years from 1966 to 2016.
    """
    
    # Call the read_dataset function and store its two return dataframe in 
    # new variables
    years_as_column_dataframe_, country_as_column_dataframe_ = read_dataset(
                                                                "data.csv")

    # Select from the "Country Name" and "Indicator Name" index, the rows with 
    # 'CO2 emissions from liquid fuel consumption (kt)' and preferred countries
    # in the countries list
    co2_emission_df = years_as_column_dataframe_ \
        .loc[(years_as_column_dataframe_.index.get_level_values(1) == 
              'CO2 emissions from liquid fuel consumption (kt)') &
                 years_as_column_dataframe_\
                  .index.get_level_values(0).isin(countries)]
    
    # Generate an evenly spaced array with length of the countries list        
    country_column_axis = np.arange(len(countries)) 

    # Create a figure and modify the size of the plot
    plt.figure(figsize=(10, 6))
    
    # Local variables
    year = 1966
    increase_year_by = 10
    decrease_axis = 0.5
    
    # This for-loop, loops 6 times and plots the bar graph in group of years 
    for _range in range(6):
        year = str(year)
        plt.bar(country_column_axis - decrease_axis, 
                co2_emission_df[year], 0.15, label=year)
        decrease_axis -= 0.15
        year = int(year) + increase_year_by
    
    # Identify ticks for the x-axis and customize the labels
    plt.xticks(country_column_axis, labels=countries, rotation=60, fontsize=11)
    plt.yticks(fontsize=11)
    
    # Labels for the x and y axis respectively
    plt.xlabel("Country Name", fontsize=12)
    plt.ylabel("CO2 emissions (kt)", fontsize=12)
    
    # Title of the plot and legend
    plt.title("CO2 emissions from liquid fuel consumption (kt)", fontsize=14)
    plt.legend()
    
    # Save plot image
    plt.savefig("Co2 Emission Bar Plot.jpg")
    
    # Display plot
    plt.show()

# Function to explore the statistical properties of urban population
def urban_population():
    """
        This function explores the statistical properties of the 
        "Urban Population" indicator. 
        It also plots a graph showing the Urban Population" for every 10 
        years from 1966 to 2016.
    """
    
    # Call the read_dataset function and store its two return dataframe in 
    # new variables
    years_as_column_dataframe_, country_as_column_dataframe_ = read_dataset(
                                                                "data.csv")

    # Select from the "Country Name" and "Indicator Name" index, the rows with 
    # "Urban population" and preferred countries
    # in the countries list
    urban_population_df = years_as_column_dataframe_\
        .loc[(years_as_column_dataframe_.index.get_level_values(1) == 
              'Urban population') & years_as_column_dataframe_\
                  .index.get_level_values(0).isin(countries)]
    
    # Generate an evenly spaced array with length of the countries list
    country_column_axis = np.arange(len(countries)) 
    
    # Create a figure and modify the size of the plot
    plt.figure(figsize=(10, 6))
    
    # Local variables 
    year = 1966
    increase_year_value = 10
    decrease_axis = 0.45
    
    # This for-loop, loops 6 times and plots the bar graph in group of years
    for _range in range(6): 
        year = str(year)
        plt.bar(country_column_axis - decrease_axis, urban_population_df[year], 
                0.15, label=year)
        decrease_axis -= 0.15
        year = int(year) + increase_year_value
    
    # Identify ticks for the x-axis and customize the labels
    plt.xticks(country_column_axis, labels=countries, rotation=80)
    plt.yticks(fontsize=11)
    
    # Labels for the x and y axis respectively
    plt.xlabel("Country Name", fontsize=12)
    plt.ylabel("Urban Population", fontsize=12)
    
    # Title of the plot and legend
    plt.title("Urban population of 10 countries", fontsize=14)
    plt.legend()
    
    # Display plot
    plt.show()

# Funtion to analyze arable land area of some countries
def arable_land():
    """
        This function explores the statistical properties and trends 
        of Arable land (% of land area). 
    """
    
    # Call the read_dataset function and store its two return dataframe in 
    # new variables
    years_as_column_dataframe_, country_as_column_dataframe_ = read_dataset(
                                                                "data.csv")
    
    # This for-loop, loops through both the number_of_women and labels list 
    # and plots out each line in the plot    
    increase_year_value = 10
    start_year = 1966
    years = []
    
    # Select from the "Country Name" and "Indicator Name" index, the rows with 
    # "Urban population growth (annual %)" and preferred countries
    # in the countries list    
    arable_land_df = years_as_column_dataframe_.loc[(years_as_column_dataframe_\
             .index.get_level_values(1) == 'Arable land (% of land area)')
             &
             years_as_column_dataframe_\
                  .index.get_level_values(0).isin(countries)]
    
    # Set "Country Name" as the index of the datafreame.  
    arable_land_df = arable_land_df.reset_index().set_index("Country Name")
    
    # Remove the "Indicator Name" column from the columns 
    arable_land_df = arable_land_df.drop("Indicator Name", axis=1)
    
    # Transpose, reset the index and set the index of the dataframe
    arable_land_df = arable_land_df.transpose().reset_index().\
                        set_index("index")
    
    # Set the index name to Year
    arable_land_df.index.name = "Year"
    
    # Create a figure and modify the size of the plot
    plt.figure(figsize=(10, 8))
    
    # This for-loop, loops 6 times add each year to the years list
    for year_range in range(6):
        years.append(str(start_year))
        start_year += increase_year_value 
    
    # Get the years data needed from the "arable land dataframe"
    arable_land_df = arable_land_df.loc[arable_land_df.index.\
                                        get_level_values(0).isin(years)]
    
    # Loops 10 times and plot the line plot of the arable land area
    for index in range(10):
        plt.plot(years, arable_land_df[countries[index]], 
                 marker='o', label=countries[index])
    
    # Identify ticks for the x-axis and customize the labels
    plt.xticks(fontsize=11)
    plt.yticks(fontsize=11)
    
    # Labels for the x and y axis respectively
    plt.xlabel("Years", fontsize=12)
    plt.ylabel("Percentage land area", fontsize=12)
    
    # Title of the plot and legend
    plt.title("Arable land (% of land area)", fontsize=14)
    plt.legend()
    
    # Display plot
    plt.show()

# Function to plot the forest area some countries 
def forest_area():
    """
        This function explores the statistical properties and trends 
        of Forest Area of some countries.
    """
    
    # Call the read_dataset function and store its two return dataframe in 
    # new variables
    years_as_column_dataframe_, country_as_column_dataframe_ = read_dataset(
                                                                "data.csv")
    
    # Local variable    
    increase_year_value = 10
    start_year = 1966
    years = []
    
    # Select from the "Country Name" and "Indicator Name" index, the rows with 
    # "Total population" and preferred countries
    # in the countries list    
    total_population_df = years_as_column_dataframe_.loc[(years_as_column_dataframe_\
             .index.get_level_values(1) == 'Population, total')
             &
             years_as_column_dataframe_\
                  .index.get_level_values(0).isin(countries)]
    
    # Set "Country Name" as the index of the datafreame.  
    total_population_df = total_population_df.reset_index().set_index("Country Name")
    
    # Remove the "Indicator Name" column from the columns 
    total_population_df = total_population_df.drop("Indicator Name", axis=1)
    
    # Transpose, reset the index and set the index of the dataframe
    total_population_df = total_population_df.transpose().reset_index().\
                        set_index("index")
    
    # Set the index name to Year
    total_population_df.index.name = "Year"
    
    # Create a figure and modify the size of the plot
    plt.figure(figsize=(10, 8))
    
    # This for-loop, loops 6 times add each year to the years list
    for year_range in range(6):
        years.append(str(start_year))
        start_year += increase_year_value 
    
    # Get the years data needed from the "Population Total"
    total_population_df = total_population_df.loc[total_population_df.index.\
                                        get_level_values(0).isin(years)]
    
    # Loops 10 times and plot the line plot of the population
    for index in range(10):
        plt.plot(years, total_population_df[countries[index]], 
                 marker='o', label=countries[index])
    
    # Identify ticks for the x-axis and customize the labels
    plt.xticks(fontsize=11)
    plt.yticks(fontsize=11)
    
    # Labels for the x and y axis respectively
    plt.xlabel("Years", fontsize=12)
    plt.ylabel("Population", fontsize=12)
    
    # Title of the plot and legend
    plt.title("Population, total", fontsize=14)
    plt.legend()
    
    # Display plot
    plt.show()


co2_emission()
urban_population()
arable_land()
forest_area()
