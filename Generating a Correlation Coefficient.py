# -*- coding: utf-8 -*-

“”“

Created on Sat Jan 16 01:36:49 2016

@author: Bernard

”“”

import pandas

import numpy

import seaborn

import scipy

import matplotlib.pyplot as plt

 

 

data = pandas.read_csv(‘gapminder_ghana_updated.csv’, low_memory=False)

 

 

#setting variables you will be working with to numeric

data['incomeperperson’] = data['incomeperperson’].convert_objects(convert_numeric=True)

data[“lifeexpectancy”] = data[“lifeexpectancy”].convert_objects(convert_numeric=True)

 

 

#replacing missen values with Nan

data['incomeperperson’]=data['incomeperperson’].replace(“, numpy.nan)

data['lifeexpectancy’]=data['lifeexpectancy’].replace(”, numpy.nan)

 

 

scat1 = seaborn.regplot(x=“incomeperperson”, y=“lifeexpectancy”, fit_reg=True, data=data)

plt.xlabel('incomeperperson’)

plt.ylabel('lifeexpectancy’)

plt.title('Scatterplot for the Association Between incomeperperson and lifeexpectancy of Ghana’)

 

 

print (“)

print (”)

print (“)

 

 

print ('association between incomeperperson and lifeexpectancy of Ghana’)

print (scipy.stats.pearsonr(data['incomeperperson’], data['lifeexpectancy’]))

 

 

print (”)

print (“)

print (”)
