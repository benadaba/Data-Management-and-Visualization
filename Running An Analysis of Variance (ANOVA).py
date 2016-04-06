# -*- coding: utf-8 -*-

“”“

Created on Mon Jan  4 00:59:30 2016

@author: Bernard

”“”

import numpy

import pandas

#to be able to get the p value and conduct the ANOVA F TEST we import this library

import statsmodels.formula.api as smf

import statsmodels.stats.multicomp as multi

#load the gapminder_ghana_updated dataset csv into the program

data = pandas.read_csv(‘gapminder_ghana_updated.csv’, low_memory = False)

#Converting data to numeric

data[“incomeperperson”] = data[“incomeperperson”].convert_objects(convert_numeric=True)

data[“lifeexpectancy”] = data[“lifeexpectancy”].convert_objects(convert_numeric=True)

data[“literacyrate”] = data[“literacyrate”].convert_objects(convert_numeric= True)

data[“Inflation”] = data[“Inflation”].convert_objects(convert_numeric= True)

#create a variable for inflationcategory

data[“inflationCategory”] = data[“Inflation”]

#categorical groupings for inflation. This is to get one categorical variable for the

#ANOVA test

data[“inflationCategory”] = pandas.cut(data.inflationCategory, [-4, 32, 64, 96, 128])

#including only data relevant for our testing by droping irrelavant data

dataSub = data[[“incomeperperson”, “inflationCategory”]].dropna()

 

#Change format from numberic to categorical

dataSub[“inflationCategory”] = dataSub[“inflationCategory”].astype(“category”)

#describe inflation category

print(“describe inflation Category”)

desc1 = dataSub[“inflationCategory”].describe()

print(desc1)

#inflationCategory count

print(“inflation category”)

c1 = dataSub[“inflationCategory”].value_counts(sort=False, dropna=True)

print(c1)

 

#print size of incomeperperson

ct1 = dataSub.groupby('incomeperperson’).size()

print(“Incomeperperson - 2010 Gross Domestic Product per capita in constant 2000 US$ of Ghana. ”)

print (ct1)

 

# using ordinaary least squares (ols)function for calculating the F-statistic and associated p value

model1 = smf.ols(formula='incomeperperson ~ C(inflationCategory)’, data=dataSub)

results1 = model1.fit()

print (results1.summary())

#Examining the means of incomeperperson and inflationcategory, hence i will be

#looking at only the variables concerned

dataSub1 = data[['incomeperperson’, 'inflationCategory’]].dropna()

print ('means for incomeperperson by inflationCategory’)

mean1= dataSub1.groupby('inflationCategory’).mean()

print (mean1)

print ('standard deviations for incomeperperson by inflationCategory’)

sd1 = dataSub1.groupby('inflationCategory’).std()

print (sd1)

#running a post hoc ANOVA TEST for levels of the categorical variables using TUKEYHSD

mc1 = multi.MultiComparison(dataSub1['incomeperperson’], dataSub1['inflationCategory’])

res1 = mc1.tukeyhsd()

print(res1.summary())

 
