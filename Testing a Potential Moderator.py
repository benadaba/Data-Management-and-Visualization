# -*- coding: utf-8 -*-

“”“

Created on Fri Jan 22 10:00:22 2016

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

data[“inflation”] = data[“inflation”].convert_objects(convert_numeric=True)



#replacing missen values with Nan

data['incomeperperson’]=data['incomeperperson’].replace(“, numpy.nan)

data['lifeexpectancy’]=data['lifeexpectancy’].replace(”, numpy.nan)

data['inflation’]=data['inflation’].replace(“, numpy.nan)



print (” “)

print (” “)

print ("association between incomeperperson and lifeexpectancy of Ghana”)

print (scipy.stats.pearsonr(data['incomeperperson’], data['lifeexpectancy’]))

print (“ ”)

print (“ ”)

#describe inflation category

print(“describe inflation Group”)

desc1 = data[“inflation”].describe()

print(desc1)



#grouping the inflation figures into groups of 1 , 2 and 3

# figure group 1 represents LOW inflation group

# figure group 2 represents MEDIUM inflation group

# figure group 3 represents MEDIUM inflation group

def inflationGrp (row):

  if row['inflation’] <= 30:

     return 1

  elif row['inflation’] <= 60 :

     return 2

  elif row['inflation’] > 60:

     return 3

data['inflationGrp’] = data.apply (lambda row: inflationGrp (row),axis=1)

print (“ ”)

print (“ ”)



print (“Print and count all the values in inflationGrp ”)

chk1 = data['inflationGrp’].value_counts(sort=False, dropna=False)

print(chk1)



sub1=data[(data['inflationGrp’]== 1)]

sub2=data[(data['inflationGrp’]== 2)]

sub3=data[(data['inflationGrp’]== 3)]





print (“ ”)

print (“ ”)



print(“Check what values and how many of it in sub1”)

valuesInSub1= sub1[“inflationGrp”].value_counts(sort=False, dropna=False)

print(“value,” “quantity”)

print( valuesInSub1)

print (“ ”)

print (“ ”)

print(“Check what values and how many of it in sub2”)

valuesInSub2= sub2[“inflationGrp”].value_counts(sort=False, dropna=False)

print(“value,” “quantity”)

print( valuesInSub2)

 

print (“ ”)

print (“ ”)

 

print(“Check what values and how many of it in sub3”)

valuesInSub3= sub3[“inflationGrp”].value_counts(sort=False, dropna=False)

print(“value,” “quantity”)

print( valuesInSub3)

 

print (“ ”)

print (“ ”)

 

print ('association between incomeperperson and lifeexpectancy for LOW inflation period’)

print (scipy.stats.pearsonr(sub1['incomeperperson’], sub1['lifeexpectancy’]))

print (“ ”)

print ('association between incomeperperson and lifeexpectancy for MIDDLE inflation period’)

print (scipy.stats.pearsonr(sub2['incomeperperson’], sub2['lifeexpectancy’]))

print (“ ”)

print ('association between incomeperperson and lifeexpectancy for HIGH inflation period’)

print (scipy.stats.pearsonr(sub3['incomeperperson’], sub3['lifeexpectancy’]))

 



#creating the 3 different axes where the 3 plotting illustrations will display

fig = plt.figure()

ax1 = fig.add_subplot(311)

ax2 = fig.add_subplot(312)

ax3 = fig.add_subplot(313)

 

 



scat1 = seaborn.regplot(x=“incomeperperson”, y=“lifeexpectancy”,fit_reg=True, data=sub1, ax=ax1)

plt.xlabel('Income Per Person’)

plt.ylabel('Life Expectancy’)

plt.title('Scatterplot for the Association Between Income Person and Life Expectancy for LOW inflation period’)

print (scat1)

 



scat2 = seaborn.regplot(x=“incomeperperson”, y=“lifeexpectancy”, fit_reg=True, data=sub2, ax=ax2)

plt.xlabel('Income Per Person’)

plt.ylabel('Life Expectancy’)

plt.title('Scatterplot for the Association Between Income Person and Life Expectancy for MIDDLE inflation period’)

print (scat2)

 



scat3 = seaborn.regplot(x=“incomeperperson”, y=“lifeexpectancy”, fit_reg=True, data=sub3, ax=ax3)

plt.xlabel('Income Per Person’)

plt.ylabel('Life Expectancy’)

plt.title('Scatterplot for the Association Between Income Person and Life Expectancy for HIGH inflation period’)

print (scat3)



