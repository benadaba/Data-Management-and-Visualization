incomeperperson_c mean
-5.3499688339584013e-14
inflation_c mean
9.717716827307253e-15
exports_c mean
-4.876273676785002e-16
                            OLS Regression Results                            
==============================================================================
Dep. Variable:         lifeexpectancy   R-squared:                       0.060
Model:                            OLS   Adj. R-squared:                  0.041
Method:                 Least Squares   F-statistic:                     3.111
Date:                Sun, 21 Feb 2016   Prob (F-statistic):             0.0840
Time:                        00:29:42   Log-Likelihood:                -129.83
No. Observations:                  51   AIC:                             263.7
Df Residuals:                      49   BIC:                             267.5
Df Model:                           1                                         
Covariance Type:            nonrobust                                         
=====================================================================================
                        coef    std err          t      P>|t|      [95.0% Conf. Int.]
-------------------------------------------------------------------------------------
Intercept            58.3784      0.441    132.445      0.000        57.493    59.264
incomeperperson_c     0.0022      0.001      1.764      0.084        -0.000     0.005
==============================================================================
Omnibus:                        7.138   Durbin-Watson:                   0.012
Prob(Omnibus):                  0.028   Jarque-Bera (JB):                7.155
Skew:                          -0.873   Prob(JB):                       0.0279
Kurtosis:                       2.436   Cond. No.                         354.
==============================================================================

Warnings:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
                            OLS Regression Results                            
==============================================================================
Dep. Variable:         lifeexpectancy   R-squared:                       0.161
Model:                            OLS   Adj. R-squared:                  0.126
Method:                 Least Squares   F-statistic:                     4.611
Date:                Sun, 21 Feb 2016   Prob (F-statistic):             0.0147
Time:                        00:29:42   Log-Likelihood:                -126.92
No. Observations:                  51   AIC:                             259.8
Df Residuals:                      48   BIC:                             265.6
Df Model:                           2                                         
Covariance Type:            nonrobust                                         
=====================================================================================
                        coef    std err          t      P>|t|      [95.0% Conf. Int.]
-------------------------------------------------------------------------------------
Intercept            58.3784      0.421    138.787      0.000        57.533    59.224
incomeperperson_c     0.0004      0.001      0.320      0.750        -0.002     0.003
exports_c             0.1129      0.047      2.409      0.020         0.019     0.207
==============================================================================
Omnibus:                        6.610   Durbin-Watson:                   0.041
Prob(Omnibus):                  0.037   Jarque-Bera (JB):                6.493
Skew:                          -0.873   Prob(JB):                       0.0389
Kurtosis:                       2.916   Cond. No.                         354.
==============================================================================

Warnings:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
                            OLS Regression Results                            
==============================================================================
Dep. Variable:         lifeexpectancy   R-squared:                       0.331
Model:                            OLS   Adj. R-squared:                  0.288
Method:                 Least Squares   F-statistic:                     7.736
Date:                Sun, 21 Feb 2016   Prob (F-statistic):           0.000267
Time:                        00:29:42   Log-Likelihood:                -121.16
No. Observations:                  51   AIC:                             250.3
Df Residuals:                      47   BIC:                             258.1
Df Model:                           3                                         
Covariance Type:            nonrobust                                         
=====================================================================================
                        coef    std err          t      P>|t|      [95.0% Conf. Int.]
-------------------------------------------------------------------------------------
Intercept            58.3784      0.380    153.730      0.000        57.614    59.142
incomeperperson_c     0.0014      0.001      1.119      0.269        -0.001     0.004
exports_c             0.1433      0.043      3.316      0.002         0.056     0.230
inflation_c           0.0629      0.018      3.449      0.001         0.026     0.100
==============================================================================
Omnibus:                        1.783   Durbin-Watson:                   0.434
Prob(Omnibus):                  0.410   Jarque-Bera (JB):                1.587
Skew:                          -0.304   Prob(JB):                        0.452
Kurtosis:                       2.385   Cond. No.                         354.
==============================================================================

Warnings:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified
