# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 23:25:53 2016

@author: adaba
"""

import numpy
import pandas
import matplotlib.pyplot as plt
import statsmodels.api as sm
import statsmodels.formula.api as smf
import seaborn


data = pandas.read_csv('gapminder_ghana_updated.csv')


# convert to numeric format
data["incomeperperson"] = data["incomeperperson"].convert_objects(convert_numeric=True)
data['lifeexpectancy'] = data['lifeexpectancy'].convert_objects(convert_numeric=True)
data["exports"] = data["exports"].convert_objects(convert_numeric=True)
data['inflation'] = data['inflation'].convert_objects(convert_numeric=True)


# listwise deletion of missing values
sub1 = data[['incomeperperson', 'lifeexpectancy', 'exports', 'inflation']].dropna()

####################################################################################
# POLYNOMIAL REGRESSION
####################################################################################

# first order (linear) scatterplot
scat1 = seaborn.regplot(x="incomeperperson", y="lifeexpectancy", scatter=True, data=sub1)
plt.xlabel('Income Per Person')
plt.ylabel('Life Expectancy')


# center quantitative IVs for regression analysis
sub1['incomeperperson_c'] = (sub1['incomeperperson'] - sub1['incomeperperson'].mean())
sub1['inflation_c'] = (sub1['inflation'] - sub1['inflation'].mean())
sub1['exports_c'] = (sub1['exports'] - sub1['exports'].mean())
sub1[["incomeperperson_c", "inflation_c"]].describe()


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


# linear regression analysis
#primary explanatory variable and response variable
reg1 = smf.ols('lifeexpectancy ~ incomeperperson_c', data=sub1).fit()
print (reg1.summary())


# quadratic (polynomial) regression analysis
# run following line of code if you get PatsyError 'ImaginaryUnit' object is not callable
#del I
#reg2 = smf.ols('lifeexpectancy ~ incomeperperson_c + I(incomeperperson_c**2)', data=sub1).fit()
#print (reg2.summary())

####################################################################################
# EVALUATING MODEL FIT
####################################################################################
# adding exports

reg2 = smf.ols('lifeexpectancy  ~ incomeperperson_c + exports_c', 
             data=sub1).fit()
print (reg2.summary())



# adding inflation_c
reg3 = smf.ols('lifeexpectancy  ~ incomeperperson_c + exports_c + inflation_c', 
              data=sub1).fit()
print (reg3.summary())

#Q-Q plot for normality
fig4=sm.qqplot(reg3.resid, line='r')

# simple plot of residuals
stdres=pandas.DataFrame(reg3.resid_pearson)
plt.plot(stdres, 'o', ls='None')
l = plt.axhline(y=0, color='r')
plt.ylabel('Standardized Residual')
plt.xlabel('Observation Number')


# additional regression diagnostic plots

fig2 = plt.figure( figsize =(12,8))
#fig2 = sm.graphics.plot_regress_exog(reg3,  "inflation_c", fig=fig2)
fig2 = sm.graphics.plot_regress_exog(reg3,  "exports_c", fig=fig2)


#dditional regression diagnostic plots
##[[fig2a = plt.figure(2,figsize =(22,18))
#fig2a = sm.graphics.plot_regress_exog(reg3,  "exports_c", fig=fig2)

# leverage plot
fig3=sm.graphics.influence_plot(reg3, size=8)
print(fig3)


