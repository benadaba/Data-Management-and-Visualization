# -*- coding: utf-8 -*-

“”“

Created on Sat Jan  2 12:33:55 2016

@author: Bernard

”“”

#import statements

import pandas

import numpy

import seaborn

import matplotlib.pyplot as plt

 

 

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

 

 

#univariate bar graph for quantitative variable - incomeperperson

seaborn.distplot(data[“incomeperperson”].dropna(), kde=False);

plt.xlabel(“Incomeperperson - 2010 Gross Domestic Product per capita in constant 2000 US$”)

plt.title(“Incomeperperson - 2010 Gross Domestic Product per capita in constant 2000 US$ of Ghana. ”)

 

 

#univariate bar graph for quantitative variable - lifeexpectancy

seaborn.distplot(data[“lifeexpectancy”].dropna(), kde=False);

plt.xlabel(“Lifeexpectancy- 2011 life expectancy at birth (years)”)

plt.title(“Lifeexpectancy- 2011 life expectancy at birth (years) of Ghana ”)

 

 

#univariate bar graph for quantitative variable - literacyrate

seaborn.distplot(data[“literacyrate”].dropna(), kde=False);

plt.xlabel(“literacyrate - 2010, Literacy rate, adult total (% of people ages 15 and above)”)

plt.title(“Literacyrate - 2010, Literacy rate, adult total (% of people ages 15 and above) of Ghana ”)

 

 

#Standard deviation and other descriptive statistics for the quantitative variables

print(“describe Incomeperperson - 2010 Gross Domestic Product per capita in constant 2000 US$ of Ghana.”)

desc1 = data[“incomeperperson”].describe()

print(desc1)

 

 

print(“describe Lifeexpectancy- 2011 life expectancy at birth (years) of Ghana”)

desc2 = data[“lifeexpectancy”].describe()

print(desc2)

 

 

print(“describe Literacyrate - 2010, Literacy rate, adult total (% of people ages 15 and above) of Ghana”)

desc3 = data[“literacyrate”].describe()

print(desc3)

 

 

#Scatterplot for the relationship between Literacy Rate and Life Expectancy of Ghana

scat1 = seaborn.regplot(x=“literacyrate”, y=“lifeexpectancy”, fit_reg=False, data=data)

plt.xlabel(“LITERACYRATE”)

plt.ylabel(“LIFEEXPECTANCY”)

plt.title(“Scatterplot for the Association between Literacy Rate and Life Expectancy of Ghana”)

 

 

#Showing The Line of Best Fit by dropping “fit_reg” in the seaborn.regplot function to show Scatterplot for the

#relationship between Literacy Rate and Life Expectancy of Ghana

scat2 = seaborn.regplot(x=“literacyrate”, y=“lifeexpectancy”, data=data)

plt.xlabel(“LITERACYRATE”)

plt.ylabel(“LIFEEXPECTANCY”)

plt.title(“Scatterplot for the Association between Literacy Rate and Life Expectancy of Ghana”)

 

 

#Scatterplot for the relationship between Literacy Rate and Income Per Person of Ghana

scat3 = seaborn.regplot(x=“literacyrate”, y=“incomeperperson”, fit_reg=False, data=data)

plt.xlabel(“LITERACYRATE”)

plt.ylabel(“INCOMEPERPERSON”)

plt.title(“Scatterplot for the Association between Literacy Rate and Income Per Person of Ghana”)

 

 

#Showing The Line of Best Fit by dropping “fit_reg” in the seaborn.regplot function to show Scatterplot for the

#relationship between Literacy Rate and Income Per Person of Ghana

scat4 = seaborn.regplot(x=“literacyrate”, y=“incomeperperson”, data=data)

plt.xlabel(“LITERACYRATE”)

plt.ylabel(“INCOMEPERPERSON”)

plt.title(“Scatterplot for the Association between Literacy Rate and Income Per Person of Ghana”)

 

 
