# -*- coding: utf-8 -*-

“”“

Created on Mon Jan  4 00:59:30 2016

@author: Bernard

”“”

import pandas

import scipy.stats

import seaborn

import matplotlib.pyplot as plt

 

#load the gapminder_ghana_updated dataset csv into the program

data = pandas.read_csv(‘gapminder_ghana_updated.csv’, low_memory = False)



#Converting data to numeric

data['incomeperperson’] = pandas.to_numeric(data['incomeperperson’], errors='coerce’)

data['lifeexpectancy’] = pandas.to_numeric(data['lifeexpectancy’], errors='coerce’)

data['literacyrate’] = pandas.to_numeric(data['literacyrate’], errors='coerce’)

data['Inflation’] = pandas.to_numeric(data['Inflation’], errors='coerce’)

data['exports’] = pandas.to_numeric(data['exports’], errors='coerce’)



#create a variable for inflationCategory

data[“inflationCategory”] = data[“Inflation”]

 

#categorical groupings for inflation. This is to get one categorical variable for the

#Chi Square test

data[“inflationCategory”] = pandas.cut(data.inflationCategory, [-4, 32, 64, 96, 128])

 

#create a variable for exportsCategory

data[“exportsCategory”] = data[“exports”]

 

#categorical groupings for exports. this is to get a two level categorical varible

# for the CHI SQUARE Test

data[“exportsCategory”] = pandas.qcut(data[“exports”], 2)

 



#including only data relevant for our testing by droping irrelavant data

dataSub = data[[“inflationCategory”, “exportsCategory”]].dropna()

 

#describe inflation category

print(“describe inflation Category”)

desc1 = dataSub[“inflationCategory”].describe()

print(desc1)



print(“”)

print(“”)

#inflationCategory count

print(“inflation category”)

c1 = dataSub[“inflationCategory”].value_counts(sort=False, dropna=True)

print(c1)

print(“”)

print(“”)

#describe exportsCategory

print(“describe Exports Category”)

desc1 = dataSub[“exportsCategory”].describe()

print(desc1)



print(“”)

print(“”)



#Exports category count

print(“Exports category”)

c1 = dataSub[“exportsCategory”].value_counts(sort=False, dropna=True)

print(c1)

print(“”)

print(“”)

 

# contingency table of observed counts

count1=pandas.crosstab(dataSub['exportsCategory’], dataSub['inflationCategory’])

print (count1)

 

print(“”)

print(“”)

 

# column percentages

colmnSum=count1.sum(axis=0)

colPercent=count1/colmnSum

print(colPercent)

print(“”)

print(“”)

# chi-square

print ('chi-square value, p value, expected counts’)

chiSq1= scipy.stats.chi2_contingency(count1)

print (chiSq1)

print(“”)

print(“”)

 

#Change format of inflationCategory from numberic to categorical

dataSub[“inflationCategory”] = dataSub[“inflationCategory”].astype(“category”)

# make exportsCategory numberic

dataSub[“exportsCategory”] = pandas.to_numeric(dataSub['exportsCategory’], errors='coerce’)

 

# graph percent with export level within each inflation group

seaborn.factorplot(x=“inflationCategory”, y=“exportsCategory”, data=dataSub, kind=“bar”, ci=None)

plt.xlabel(“Inflation group level ”)

plt.ylabel(“Proportion Export level”)

 

#compare [-4, 32] and [32, 64]

recode1 = {[-4, 32]: [-4, 32], [32, 64]: [32, 64]}

dataSub['COMP-4v32’]= dataSub['inflationCategory’].map(recode1)

 

# contingency table of observed counts

count2=pandas.crosstab(dataSub['inflationCategory’], dataSub['COMP-4v32’])

print (count2)

 

# column percentages

colmnSum2=count2.sum(axis=0)

columnPerc2=count2/colmnSum2

print(columnPerc2)

 

print ('chi-square value, p value, expected counts’)

chis2= scipy.stats.chi2_contingency(count2)

print (chis2)

 

#compare [-4, 32] and [64, 96]

recode2 = {[-4, 32]: [-4, 32], [64, 96]: [64, 96]}

dataSub['COMP-4v64’]= dataSub['inflationCategory’].map(recode2)

# contingency table of observed counts

count2=pandas.crosstab(dataSub['inflationCategory’], dataSub['COMP-4v64’])

print (count2)

# column percentages

colmnSum2=count2.sum(axis=0)

columnPerc2=count2/colmnSum2

print(columnPerc2)

print ('chi-square value, p value, expected counts’)

chis2= scipy.stats.chi2_contingency(count2)

print (chis2)

 

#compare [-4, 32] and [96, 128]

recode3 = {[-4, 32]: [-4, 32], [96, 128]: [96, 128]}

dataSub['COMP-4v96’]= dataSub['inflationCategory’].map(recode3)

# contingency table of observed counts

count3=pandas.crosstab(dataSub['inflationCategory’], dataSub['COMP-4v96’])

print (count3)

# column percentages

colmnSum3=count3.sum(axis=0)

columnPerc3=count3/colmnSum3

print(columnPerc3)

print ('chi-square value, p value, expected counts’)

chis3= scipy.stats.chi2_contingency(count3)

print (chis3)

 

#compare [32, 64] and [64, 96]

recode4 = {[32, 64]: [32, 64], [64, 96]: [64, 96]}

dataSub['COMP32v64’]= dataSub['inflationCategory’].map(recode4)

# contingency table of observed counts

count4=pandas.crosstab(dataSub['inflationCategory’], dataSub['COMP32v64’])

print (count4)

# column percentages

colmnSum4=count4.sum(axis=0)

columnPerc4=count4/colmnSum4

print(columnPerc4)

print ('chi-square value, p value, expected counts’)

chis4= scipy.stats.chi2_contingency(count4)

print (chis4)

 

#compare [32, 64] and [96, 128]

recode5 = {[32, 64]: [32, 64], [96, 128]: [96, 128]}

dataSub['COMP32v96’]= dataSub['inflationCategory’].map(recode5)

# contingency table of observed counts

count5=pandas.crosstab(dataSub['inflationCategory’], dataSub['COMP32v96’])

print (count5)

# column percentages

colmnSum5=count5.sum(axis=0)

columnPerc5=count5/colmnSum5

print(columnPerc5)

print ('chi-square value, p value, expected counts’)

chis5= scipy.stats.chi2_contingency(count5)

print (chis5)

 

#compare [64, 96] and [96, 128]

recode6 = {[64, 96]: [64, 96], [96, 128]: [96, 128]}

dataSub['COMP64v96’]= dataSub['inflationCategory’].map(recode6)

# contingency table of observed counts

count6=pandas.crosstab(dataSub['inflationCategory’], dataSub['COMP64v96’])

print (count6)

# column percentages

colmnSum6=count6.sum(axis=0)

columnPerc6=count6/colmnSum6

print(columnPerc6)

print ('chi-square value, p value, expected counts’)

chis6= scipy.stats.chi2_contingency(count6)

print (chis6)

 
