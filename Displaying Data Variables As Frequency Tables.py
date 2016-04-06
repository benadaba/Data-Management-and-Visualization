# -*- coding: utf-8 -*-
“”“
Created on Sat Dec 19 11:24:10 2015

@author: Bernard
”“”

#import statements
import pandas
import numpy

#load the gapminder_ghana_updated dataset csv into the program
data = pandas.read_csv(‘gapminder_ghana_updated.csv’, low_memory = False)

#print number of observations(rows) which is the number of years this data 
#has been looked at; print length
print(“number of observations(rows) which is the number of years this data has been looked at: ”)
print(len(data))

#print number of variables (columns)
print(“number of variables (columns) available in the dataset: ”)
print(len(data.columns))

print(“data index: ”)
print(len(data.index))

#Converting datat to numeric
data[“incomeperperson”] = data[“incomeperperson”].convert_objects(convert_numeric=True)
data[“lifeexpectancy”] = data[“lifeexpectancy”].convert_objects(convert_numeric=True)
data[“literacyrate”] = data[“literacyrate”].convert_objects(convert_numeric= True)

#displaying rows or observation in Dataframe.
#inc_pp_count is the name that will hold the result from incomeperperson count
# sort = false ; i use value false so that the data will be sorted according 
#to the original format and sequence  of the loaded data

print(“counts for incomeperperson - 2010 Gross Domestic Product per capita in constant 2000 US$ of Ghana. ”)
inc_pp_count = data[“incomeperperson”].value_counts(sort = False)
#print the count of inc_pp_count ; incomeperperson
print(inc_pp_count)

print(“percentages for incomeperperson - 2010 Gross Domestic Product per capita in constant 2000 US$ of Ghana. ”)
inc_pp_percent = data[“incomeperperson”].value_counts(sort=False, normalize =True)
#print the percentage of incomeperperson
print(inc_pp_percent)

print(“counts for lifeexpectancy- 2011 life expectancy at birth (years) of Ghana”)
life_exp_count = data[“lifeexpectancy”].value_counts(sort = False)
#print the count of life_exp_count ; lifeexpectancy
print(life_exp_count)

print(“percentages for lifeexpectancy- 2011 life expectancy at birth (years) of Ghana ”)
life_exp_percent = data[“lifeexpectancy”].value_counts(sort =False, normalize = True)
#print the percentage of life_exp_count ; lifeexpectancy
print(life_exp_percent)

print(“counts for literacyrate - 2010, Literacy rate, adult total (% of people ages 15 and above) of Ghana”)
lit_rate_count = data[“literacyrate”].value_counts(sort = False ,dropna=False) #dropna displays missen values
#print the count of lit_rate_count ; literacyrate
print(lit_rate_count)

print(“percentages literacyrate - 2010, Literacy rate, adult total (% of people ages 15 and above) of Ghana ”)
lit_rate_percent = data[“literacyrate”].value_counts(sort =False, normalize = True)
#print the percentage of lit_rate_count ; literacyrate
print(lit_rate_percent)

