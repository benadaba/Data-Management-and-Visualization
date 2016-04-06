# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 23:25:53 2016
@author: Bernard
"""


import pandas
import numpy
#import statsmodels.api as sm
import statsmodels.formula.api as smf



# bug fix for display formats to avoid run time errors
pandas.set_option('display.float_format', lambda x:'%.2f'%x) 

data = pandas.read_csv('gapminder_ghana_updated.csv',  low_memory=False)



# convert to numeric format
data["incomeperperson"] = data["incomeperperson"].convert_objects(convert_numeric=True)
data['lifeexpectancy'] = data['lifeexpectancy'].convert_objects(convert_numeric=True)
data["exports"] = data["exports"].convert_objects(convert_numeric=True)
data['inflation'] = data['inflation'].convert_objects(convert_numeric=True)



# listwise deletion of missing values
sub1 = data[['incomeperperson', 'lifeexpectancy', 'exports', 'inflation']].dropna()

print("print sub1 to see values in the data which are used for the analysis")
print(sub1)


#bining response variable into 2 categories
#from the sub1 values, all nan rows were dropped , so the mininum value is greater than 50
def lifeExpectancyCat (row):
    if row["lifeexpectancy"]<=60:
        return 0
    elif row["lifeexpectancy"] >60:
        return 1   


sub1["lifeExpectancyCat"] = sub1.apply(lambda row: lifeExpectancyCat(row), axis =1)

#print and see values in lifeExpectancyCat
print("lifeExpectancyCat values")
print(sub1['lifeExpectancyCat'])

lecCount = sub1['lifeExpectancyCat'].value_counts(sort=False, dropna = False)
print("Life Expectancy Value Counts")
print(lecCount)



#print and see values in inflation
print("inflation values")
print(sub1['inflation'].dropna())

#describe Life Expectancy to see the highest and smallest values
print("describe inflation")
print(sub1['inflation'].describe())


#creating a categorical explanatry variable out of inflation for logistic regression analyis
def inflationCatGrp (row):
    if row["inflation"] <=60:
        return 0
    elif row["inflation"]  >60:
        return 1


sub1["inflationCatGrp"] = sub1.apply(lambda row:inflationCatGrp(row), axis =1)

print ("Value Count for inflationCatGrp ")
inflationCatVal = sub1["inflationCatGrp"].value_counts(sort=False, dropna=True)
print(inflationCatVal)


#creating a categorical explanatry variable out of exports for logistic regression analyis
def exportsCatGrp (row):
    if row["exports"] <=40:
        return 0
    elif row["exports"] >40:
        return 1
    
        
sub1["exportsCatGrp"] = sub1.apply(lambda row:exportsCatGrp(row), axis =1)

print ("Value Count for exportsCatGrp ")
exportsCatVal = sub1["exportsCatGrp"].value_counts(sort=False, dropna=True)
print(exportsCatVal)


#creating a categorical explanatry variable out of incomeperperson for logistic regression analyis
def incomeLevelGrp (row):
    if row["incomeperperson"] <=2200:
        return 0
    elif row["incomeperperson"] >2200:
        return 1
        
sub1["incomeLevelGrp"] = sub1.apply(lambda row:incomeLevelGrp(row), axis =1)

print ("Value Count for incomeLevelGrp ")
incomeLevelGrpVal = sub1["incomeLevelGrp"].value_counts(sort=False, dropna=True)
print(incomeLevelGrpVal)


####################################################################################
# MULTIPLE REGRESSION
####################################################################################



# center quantitative IVs for regression analysis
sub1['incomeperperson_c'] = (sub1['incomeperperson'] - sub1['incomeperperson'].mean())
sub1['inflation_c'] = (sub1['inflation'] - sub1['inflation'].mean())
sub1['exports_c'] = (sub1['exports'] - sub1['exports'].mean())
sub1[["incomeperperson_c", "exports_c", "inflation_c"]].describe()



#chekcing means of centered explanatory variables
incomeperperson_c_mean = sub1['incomeperperson_c'].mean()
print("incomeperperson_c mean")
print(incomeperperson_c_mean)



inflation_c_mean = sub1['inflation_c'].mean()
print("inflation_c mean")
print(inflation_c_mean)



exports_c_mean = sub1['exports_c'].mean()
print("exports_c mean")
print(exports_c_mean)



# multiple regression analysis
#primary explanatory variable and response variable
#adding categorical explanatory variable inflationCatGrp
reg3 = smf.ols('lifeexpectancy  ~ incomeperperson_c + inflation_c + exports_c + C(inflationCatGrp)', 
              data=sub1).fit()
print (reg3.summary())



######################################################
#LOGISTIC REGRESSION
######################################################

# logistic regression with income level group
lreg1 = smf.logit(formula = 'lifeExpectancyCat ~ incomeLevelGrp', data = sub1).fit()
print (lreg1.summary())



# odds ratios for incomeperperson
print ("Odds Ratios")
print (numpy.exp(lreg1.params))


# odd ratios with 95% confidence intervals for incomeperperson
params = lreg1.params
conf = lreg1.conf_int()
conf['OR'] = params
conf.columns = ['Lower CI', 'Upper CI', 'OR']
print (numpy.exp(conf))


# logistic regression with inflation
lreg2 = smf.logit(formula = 'lifeExpectancyCat ~ inflationCatGrp', data = sub1).fit()
print (lreg2.summary())


# odds ratios for inflation
print ("Odds Ratios")
print (numpy.exp(lreg2.params))


# odd ratios with 95% confidence intervals for inflation
params = lreg2.params
conf = lreg2.conf_int()
conf['OR'] = params
conf.columns = ['Lower CI', 'Upper CI', 'OR']
print (numpy.exp(conf))


# logistic regression with exports
lreg3 = smf.logit(formula = 'lifeExpectancyCat ~ exportsCatGrp', data = sub1).fit()
print (lreg3.summary())


# odds ratios for exports
print ("Odds Ratios")
print (numpy.exp(lreg3.params))


# odd ratios with 95% confidence intervals for exports
params = lreg3.params
conf = lreg3.conf_int()
conf['OR'] = params
conf.columns = ['Lower CI', 'Upper CI', 'OR']
print (numpy.exp(conf))


# logistic regression with panic and depression
lreg4 = smf.logit(formula = 'lifeExpectancyCat ~ exportsCatGrp + incomeLevelGrp + inflationCatGrp', data = sub1).fit()
print (lreg4.summary())



# odds ratios for exports, incomeperperson and inflation
print ("Odds Ratios")
print (numpy.exp(lreg4.params))


# odd ratios with 95% confidence intervals for exports, incomeperperson and inflation
params = lreg4.params
conf = lreg4.conf_int()
conf['OR'] = params
conf.columns = ['Lower CI', 'Upper CI', 'OR']
print (numpy.exp(conf))
