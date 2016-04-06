# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 08:55:52 2016
@author: Bernard
"""

#from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import matplotlib.pylab as plt
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LassoLarsCV
 
#Load the dataset
data = pd.read_csv("gapminder_ghana_updated.csv")


###############################################################################
# DATA MANAGEMENT
# CONVERTING SOME QUANTITATIVE VARIABLES INTO CATEGORICAL VARIABLES TO GET FEEL 
# OF LASSO REGRESSION
###############################################################################


data_clean = data.dropna()


#check minimum and maximum values of totalpopulationfemale and create categorical 
#variable out of it
print(data_clean["totalpopulationfemale"].describe())

def totalpopulationfemaleGrp(row):
    if row["totalpopulationfemale"]<=7758806:
        return 0
    elif row["totalpopulationfemale"] > 7758806:
        return 1
        
data_clean["totalpopulationfemaleGrp"] = data_clean.apply(lambda row:totalpopulationfemaleGrp(row), axis =1 )

#check values in totalpopulationfemaleGrp
checktotFemPop = data_clean["totalpopulationfemaleGrp"].value_counts(sort=False, dropna=True)
print(checktotFemPop)

#check minimum and maximum values of malebloodpressure and create categorical 
#variable out of it
print(data_clean["malebloodpressure"].describe())

def malebloodpressureGrp(row):
    if row["malebloodpressure"]<=129:
        return 0
    elif row["malebloodpressure"] > 129:
        return 1

data_clean["malebloodpressureGrp"] = data_clean.apply(lambda row:totalpopulationfemaleGrp(row), axis =1 )

#check values ink totalpopulationfemaleGrp
checkmaleblood = data_clean["malebloodpressureGrp"].value_counts(sort=False, dropna=True)
print(checkmaleblood)

#creating categorical explanatory variables out of exports
def exportsCatGrp (row):
    if row["exports"] <=40:
        return 0
    elif row["exports"] >40:
        return 1
    
        
data_clean["exportsCatGrp"] = data_clean.apply(lambda row:exportsCatGrp(row), axis =1)


#creating a categorical explanatry variable out of incomeperperson
def incomeLevelGrp (row):
    if row["incomeperperson"] <=2200:
        return 0
    elif row["incomeperperson"] >2200:
        return 1
        
data_clean["incomeLevelGrp"] = data_clean.apply(lambda row:incomeLevelGrp(row), axis =1)



###############################################################################
#END OF DATA MANAGEMENT
###############################################################################



predvar= data_clean[['incomeLevelGrp','exportsCatGrp','malebloodpressureGrp',
'totalpopulationfemaleGrp','inflation','agriculture','democracyscore',
'agriculturalland','aidreceived','aidreceivedperperson','realgdppercapita',
'femalebloodpressure','malebodymassindex','femalebodymassindex','underfivemortality',
'totalfertilityrate','cholesterolinmen','cholesterolinwomen','crudebirthrate', 
'deadkidsperwoman','externaldebtstocks','energyuse']]



target = data_clean.lifeexpectancy
 
# standardize predictors to have mean=0 and sd=1
predictors=predvar.copy()
from sklearn import preprocessing
predictors['incomeLevelGrp']=preprocessing.scale(predictors['incomeLevelGrp'].astype('float64'))
predictors['exportsCatGrp']=preprocessing.scale(predictors['exportsCatGrp'].astype('float64'))
predictors['inflation']=preprocessing.scale(predictors['inflation'].astype('float64'))
predictors['agriculture']=preprocessing.scale(predictors['agriculture'].astype('float64'))
predictors['democracyscore']=preprocessing.scale(predictors['democracyscore'].astype('float64'))
predictors['agriculturalland']=preprocessing.scale(predictors['agriculturalland'].astype('float64'))
predictors['aidreceived']=preprocessing.scale(predictors['aidreceived'].astype('float64'))
predictors['aidreceivedperperson']=preprocessing.scale(predictors['aidreceivedperperson'].astype('float64'))
predictors['realgdppercapita']=preprocessing.scale(predictors['realgdppercapita'].astype('float64'))
predictors['malebloodpressureGrp']=preprocessing.scale(predictors['malebloodpressureGrp'].astype('float64'))
predictors['femalebloodpressure']=preprocessing.scale(predictors['femalebloodpressure'].astype('float64'))
predictors['malebodymassindex']=preprocessing.scale(predictors['malebodymassindex'].astype('float64'))
predictors['femalebodymassindex']=preprocessing.scale(predictors['femalebodymassindex'].astype('float64'))
predictors['underfivemortality']=preprocessing.scale(predictors['underfivemortality'].astype('float64'))
predictors['totalfertilityrate']=preprocessing.scale(predictors['totalfertilityrate'].astype('float64'))
predictors['cholesterolinmen']=preprocessing.scale(predictors['cholesterolinmen'].astype('float64'))
predictors['cholesterolinwomen']=preprocessing.scale(predictors['cholesterolinwomen'].astype('float64'))
predictors['crudebirthrate']=preprocessing.scale(predictors['crudebirthrate'].astype('float64'))
predictors['deadkidsperwoman']=preprocessing.scale(predictors['deadkidsperwoman'].astype('float64'))
predictors['externaldebtstocks']=preprocessing.scale(predictors['externaldebtstocks'].astype('float64'))
predictors['energyuse']=preprocessing.scale(predictors['energyuse'].astype('float64'))
predictors['totalpopulationfemaleGrp']=preprocessing.scale(predictors['totalpopulationfemaleGrp'].astype('float64'))



# split data into train and test sets
pred_train, pred_test, tar_train, tar_test = train_test_split(predictors, target, 
                                                              test_size=.3, random_state=123)

# specify the lasso regression model
model=LassoLarsCV(cv=10, precompute=False).fit(pred_train,tar_train)

# print variable names and regression coefficients
dict(zip(predictors.columns, model.coef_))

# plot coefficient progression
m_log_alphas = -np.log10(model.alphas_)
ax = plt.gca()
plt.plot(m_log_alphas, model.coef_path_.T)
plt.axvline(-np.log10(model.alpha_), linestyle='--', color='k',
            label='alpha CV')
plt.ylabel('Regression Coefficients')
plt.xlabel('-log(alpha)')
plt.title('Regression Coefficients Progression for Lasso Paths')

# plot mean square error for each fold
m_log_alphascv = -np.log10(model.cv_alphas_)
plt.figure()
plt.plot(m_log_alphascv, model.cv_mse_path_, ':')
plt.plot(m_log_alphascv, model.cv_mse_path_.mean(axis=-1), 'k',
         label='Average across the folds', linewidth=2)
plt.axvline(-np.log10(model.alpha_), linestyle='--', color='k',
            label='alpha CV')
plt.legend()
plt.xlabel('-log(alpha)')
plt.ylabel('Mean squared error')
plt.title('Mean squared error on each fold')
         

# MSE from training and test data
from sklearn.metrics import mean_squared_error
train_error = mean_squared_error(tar_train, model.predict(pred_train))
test_error = mean_squared_error(tar_test, model.predict(pred_test))
print ('training data MSE')
print(train_error)
print ('test data MSE')
print(test_error)

# R-square from training and test data
rsquared_train=model.score(pred_train,tar_train)
rsquared_test=model.score(pred_test,tar_test)
print ('training data R-square')
print(rsquared_train)
print ('test data R-square')
print(rsquared_test)
