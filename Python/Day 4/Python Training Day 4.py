#!/usr/bin/env python
# coding: utf-8

# ### Q1.

# In[2]:


def question1(x):
    sequence = [x]
    if x<1:
        return []
    while x>1:
        if x%2 == 0:
            x = x/2
        else:
            x = 3*x + 1
        
        sequence.append(x)
    return sequence

question1(12)


# ### Q2. 

# In[3]:


def question2(r):
    
    for i in range(r+1):
        for j in range(r-i):
            print(" ", end="")
        
        c=1
        for j in range(1, i+1):
            print(c, " ", sep="", end="")
            c = c * (i-j)//j
        print()

question2(6)


# ### Q3. 

# In[4]:


def question3(a,b):
    a= list(set(a))
    b = list(set(b))
    c = set(a).union(set(b)) - set(a).intersection(set(b))
    return c

a= [1,2,3,4,5,6,7]
b= [1,2,3,5,6,7]
question3(a,b)


# ### Q4. 

# In[5]:


import re

def password(passw):

    if passw == "\n" or passw == " ":
        return "Password cannot be a newline or space!"
    

    if 9 <= len(passw) <= 20:
        if re.search(r'(.)\1\1', passw):
            return "Weak Password: Same character repeats three or more times in a row"
        
        if re.search(r'(..)(.*?)\1',passw):
            return "Weak Password: Same string pattern repetition"
        
        else:
            return "Strong Password!"
    
    else:
        return "Password length must be 9-20 characters!"

print(password("Qggf!@ghf3"))
print(password("aaabnil1gu"))
print(password(" "))


# ### Q5. 

# In[6]:


def Fib(n):
    
    if n<0:
        print('Enter correct number')
        
    elif n==0:
        return 0
        
    elif n==1 or n==2:
        return 1
    
    else:
        return Fib(n-1) + Fib(n-2)
    

Fib(15)


# ### Q6.

# In[7]:


import numpy as np
import pandas as pd


# In[8]:


countries = pd.read_csv('Countries.csv')
countries.head()


# In[9]:


countries.shape


# In[10]:


countries.info()


# In[11]:


countries.describe()


# #### i) 

# In[12]:


iran = countries.iloc[12,:]
(iran['2006']+iran['2007']+iran['2008']+iran['2009']+iran['2010']+iran['2011']+iran['2012']+iran['2013']+iran['2014'])/9


# In[13]:


countries.fillna(444222222222.2222, inplace=True)


# In[14]:


countries['avgGDP'] = (countries['2006']+countries['2007']+countries['2008']+countries['2009']+countries['2010']+countries['2011']+countries['2012']+countries['2013']+countries['2014']+countries['2015'])/10
countries.head(15)


# In[15]:


def answer_one():
    one = countries.sort_values(by='avgGDP', ascending=False)
    return one[['Country', 'avgGDP']]

answer_one()


# #### ii)

# In[16]:


def answer_two():
    unitedkingdom = countries.iloc[3,:]
    return  unitedkingdom['2015']-unitedkingdom['2006'] 

answer_two()
#Sixth largest average GDP is United Kingdom and GDP has changed by 250000000000.0 in 10 years


# #### iii)

# In[17]:


def answer_three():
    return countries['Energy Supply per Capita'].mean()

answer_three()
#Mean energy supply per capita is 157.6


# #### iv)

# In[18]:


def answer_four():
    four = countries.sort_values(by='% Renewable', ascending=False).head(1)
    return four[['Country', '% Renewable']]

answer_four()
# Brazil has the maximum % Renewable with 69.64%


# #### v)

# In[19]:


countries['Ratio'] = countries['Self-citations']/countries['Citations']
countries.head()


# In[21]:


def answer_five():
    five = countries.sort_values(by='Ratio', ascending=False).head(1)
    return five[['Country', 'Ratio']]

answer_five()
#0.689313 is the maximum value for this new column, and China has the highest ratio


# #### vi)

# In[22]:


countries['Population'] = countries['Energy Supply']/countries['Energy Supply per Capita']
countries.head()


# In[29]:


def answer_six():
    six = countries.sort_values(by='Population', ascending=False).iloc[2]
    return six['Country']

answer_six()
# United States is the third most populous country according to this estimate

