# -*- coding: utf-8 -*-
"""perch.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Y0j9W7favLlcbK-f1hke2u94_tFvIXsy

### 1. Import the necessary libraries
"""

import pandas as pd
import numpy as np
import seaborn as sb
from sklearn.preprocessing import LabelEncoder
import copy
import matplotlib.pyplot as plt

"""##2. Read the data as a data frame"""

data = pd.read_csv("./insurance (2).csv")

data.head()

"""### 3a. Shape of the data """

data.shape

"""Given Data has **1338 Rows**(customers data) and **7 columns(features)**

### Q.3b. Data type of each attribute
"""

data.dtypes

"""## Q.3c. Checking the presence of missing values """

data.isna().sum()

"""### Q.3d. 5 point summary of numerical attributes """

data.describe()

"""### 3-e. Distribution of ‘bmi’, ‘age’ and ‘charges’ columns """

plt.figure(figsize= (20,15))
plt.subplot(3,3,1)
sb.distplot(data.bmi)

plt.subplot(3,3,2)
sb.distplot(data.charges)

plt.subplot(3,3,3)
sb.distplot(data.age)

plt.show()

"""### Q.3 f. Measure of skewness of ‘bmi’, ‘age’ and ‘charges’ columns """

data.skew()

"""### 3g. Checking the presence of outliers in ‘bmi’, ‘age’ and ‘charges columns """

plt.figure(figsize= (20,15))
plt.subplot(3,1,1)
sb.boxplot(x= data.bmi, color='yellow')

plt.subplot(3,1,2)
sb.boxplot(x= data.age, color='yellow')

plt.subplot(3,1,3)
sb.boxplot(x= data.charges, color='yellow')

plt.show()

"""from above plot it can be seen that


1.  **bmi** has **few outliers** and
---
2.  **charges** attribute has lot of extreme values
---
3.  **age** has** No **outliers

"""

plt.figure(figsize=(30,30))

smoker = data.smoker.value_counts()
x1 = smoker.index  
y1 = list(smoker.values)  
plt.subplot(4,2,1)
plt.barh(x1,y1) 
plt.xlabel('Is Smoker')
plt.ylabel('Count ')
plt.title('Smoker distribution')

gender = data.sex.value_counts()
x2 = gender.index  
y2 = list(gender.values)  
plt.subplot(4,2,2)
plt.barh(x2,y2, color = 'orange') 
plt.xlabel('Gender')
plt.ylabel('Count ')
plt.title('Gender distribution')


children = data.children.value_counts()
x3 = children.index  
y3 = list(children.values)  
plt.subplot(4,2,3)
plt.barh(x3,y3, color = 'yellow') 
plt.xlabel('no of children')
plt.ylabel('Count ')
plt.title('Children distribution')


region = data.region.value_counts()
x4 = region.index  
y4 = list(region.values)  
plt.subplot(4,2,4)
plt.barh(x4,y4, color = 'green') 
plt.xlabel('Different regions')
plt.ylabel('Count ')
plt.title('Region distribution')
plt.show

"""


1.   **Gender** and **region** are evenly distributed
2.   Most of the costumers are non **smokers** and very few have smoking habit.
3.  Very less customers have **4 or 5 children** and majority of them have less than **2 or no children**.




"""

data_encode = copy.deepcopy(data)
data_encode.loc[:,['sex', 'smoker', 'region']] = data_encode.loc[:,['sex', 'smoker', 'region']].apply(LabelEncoder().fit_transform) 
sb.pairplot(data_encode)

"""### 4.a. Do charges of people who smoke differ significantly from the people who don't? """

plt.figure(figsize=(9,9))
sb.scatterplot(data.age, data.charges,hue=data.smoker,palette= ['red','green'])
plt.show()

x_sm = data['charges']
y_sm = data['smoker']
sb.stripplot(x_sm,y_sm)

"""From the above graph it can be seen that
A customer **without Smoking habit** has **very low charges** as compared to customer with **Smoking habit**.

### 4-b. Does bmi of males differ significantly from that of females?
"""

x_s = data['bmi']
y_s = data['sex']

sb.stripplot(x_s,y_s)

x = data_encode['sex']
y = data_encode['bmi']
plt.scatter(x,y)

"""It can be seen that there **no significant difference** in BMI of female and male customers.

## 4 c. Is the proportion of smokers significantly different in different genders?
"""

a= data[data['smoker']=='yes']
num_f = a[a['sex']=='female'].shape[0]
denom = a.shape[0]
num_m = a[a['sex']=='male'].shape[0]

print("Proportion of smokers who are male is ", (num_f/denom))
print("Proportion of smokers who are female is ", (num_m/denom))

"""The proportions being **58% **and** 42%** for male and female genders who smoke are not significantly different.

### 4.d. Is the distribution of bmi across women with no children, one child and two children, the same?
"""

sb.stripplot(data['bmi'], data[data['sex']=='female']['children'])

"""**Yes**, the distributions of ‘bmi’ are nearly same across women with 0, 1 or 2 children."""