#!/usr/bin/env python
# coding: utf-8

# #### Importing Libraries

# In[121]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# ### Q1. Using the data frame incomedata.csv, perform the following operations:

# In[122]:


inc = pd.read_csv('incomedata.csv')
inc.head()


# In[123]:


inc.shape


# In[124]:


inc.info()


# In[125]:


inc.describe()


# #### i) Select the variables age category (agecat) and gender for the subjects who did not complete high school

# In[126]:


inc[inc['educ']=='Did not complete high school']


# #### ii) Select the variables age category and gender for the subjects who did not complete high school and have the income greater than 20

# In[127]:


inc[(inc['educ']=='Did not complete high school') & (inc['income']>20)]


# #### iii) Select the male subjects with the income lower than 65 and compute their average income

# In[128]:


inc[(inc['gender']=='Male') & (inc['income']<65)].mean()


# #### iv) Group the subjects by age category and compute the mean and the standard deviation of the income

# In[129]:


inc.groupby('agecat').describe()


# #### V) Sort the data frame by income, in ascending and descending order

# In[130]:


inc.sort_values(by="income", ascending=True)
inc.sort_values(by="income", ascending=False)


# #### vi) Count the number of subjects in each education category

# In[131]:


inc['educ'].value_counts()


# ### Q2. Using the data frame satisfaction.csv, perform the following operations

# In[132]:


sat = pd.read_csv('satisfaction.csv')
sat.head()


# In[133]:


sat.shape


# In[134]:


sat.info()


# In[135]:


sat.describe()


# #### i) group the travelers by type, select the travelers aged over 35 and compute their average satisfaction

# In[136]:


sat[sat['age']>35].groupby('type').mean()


# #### ii) group the travelers by importance of price (imprice), select the pleasure travelers aged under 50 and compute their average satisfaction

# In[137]:


sat[(sat['type']=='Pleasure traveler') & (sat['age']<50)].groupby('imprice').mean()


# #### iii) extract 55 travelers at random, without replacement, select the business travelers and compute their average price importance

# In[138]:


sample=sat.sample(n=55)
sample[sample['type']== "Business traveler"].mean()


# #### iv) count the number of pleasure and business travelers

# In[139]:


sat["type"].value_counts()


# #### v) count the number of business travelers for each satisfaction level

# In[140]:


s1=sat[sat['type']=="Business traveler"].value_counts()
s1.value_counts()


# #### vi) select the top 20 travelers based on age

# In[141]:


sat.sort_values(by="age", ascending=False).head(20)


# #### vii) select the travelers that have of satisfaction level greater than 2 and compute their average age and price importance

# In[142]:


sat[sat["satisfaction"]>2].mean()


# ### Q3. Using the data frame vehicles.csv, perform the following operations:

# In[143]:


veh = pd.read_csv('vehicles.csv')
veh.head()


# #### i) select the automobiles with the horsepower greater than 120

# In[144]:


veh[veh["horsepow"]>120]


# #### ii) select the automobiles with the fuel capacity lower than 20, retaining only the following variables: price, engine size (engine) and width

# In[145]:


veh[veh["fuelcap"]>20]


# #### iii) group the data frame by vehicle type, select the vehicles with the price greater than 30 and compute their average mpg

# In[147]:


veh[veh['price']>30].groupby('type').mean()


# #### iv) group the data frame by vehicle type, select the vehicles with the engine size greater than 2.5 and compute their average price

# In[149]:


veh[veh['engine']>2.5].groupby('type').mean()


# #### v) select the top 25 vehicles by horsepower and fuel capacity, respectively

# In[150]:


veh.sort_values(['horsepow', 'fuelcap'],ascending = [False, False]).head(25)


# #### vi) compute a new variable as a product of the vehicle width and length

# In[151]:


veh['product'] = veh['width'] * veh['length']
veh.head()


# #### vii) compute the number of unique values in the variables engine size and mpg

# In[154]:


veh['engine'].nunique()


# In[155]:


veh['mpg'].nunique()


# #### viii) extract 30 vehicles at random and compute their average width

# In[156]:


veh['width'].sample(n=30).mean()


# ### Q4. Using the data frame company.csv, perform the following operations:

# In[157]:


company = pd.read_csv('company.csv')
company.head()


# #### i) extract the male employees (gender=1) with a salary over 30000, retaining the variables education and job time only

# In[158]:


m30000 = company[(company['gender']==1) & (company['salary']>30000)]
m30000[['educ', 'jobtime']]


# #### ii) group the data frame by gender, select the employees in the sales department (sales=3) and compute their average salary

# In[159]:


company[company['dept']==3].groupby('gender').mean()


# #### iii) select 50 employees at random, group them by department and compute the average job time by department

# In[160]:


company.sample(n = 50).groupby('dept').mean()


# #### iv) compute a new variable by adding the variables job time and previous experience

# In[161]:


company['jobtime+prevexp'] = company['jobtime'] + company['prevexp']
company.head()


# #### v) select the top 10 employees by salary

# In[162]:


company.sort_values(by="salary", ascending=False).head(10)


# #### vi) group the data frame by department and gender, then compute the average previous experience for each group

# In[163]:


company.groupby(['dept','gender']).mean()


# #### vii) count the number of employees in each department, by gender

# In[164]:


company.groupby(['dept', 'gender']).count()


# ### Q5. Using the data frame countries.csv, perform the following operations

# In[165]:


countries = pd.read_csv('countries.csv')
countries.head()


# #### i) select the top 5 countries by population increase (popincr)

# In[166]:


countries.sort_values(by="popincr", ascending=False).head()


# #### ii) select the countries with a GDP over 1500 and population density over 130 and compute their average urban population rate (urban)

# In[167]:


gdpdensity=countries[(countries["gdp"]>1500) & (countries['density']>130)]
gdpdensity['urban'].mean()


# #### iii) select 45 countries at random and compute their average GDP

# In[168]:


countries['gdp'].sample(n = 45).mean()


# #### iv) compute a new variable by averaging the variables female life expectancy and male life expectancy (flexp, mlexp)

# In[169]:


countries['flexp+mlexp'] = (countries['flexp'] + countries['mlexp'])/2
countries.head()


# #### v) compute the number of distinct values in the variables literacy and infant mortality (infmort), respectively

# In[170]:


countries['literacy'].nunique()


# In[171]:


countries['infmort'].nunique()


# #### vi) select 50 countries at random, and compute their average population density and population increase

# In[172]:


countries[['density', 'popincr']].sample(n = 50).mean()


# #### vii) sort the countries by GDP and literacy, in ascending orde

# In[173]:


countries.sort_values(['gdp', 'literacy'],ascending = [True, True]).head()


# #### viii) sort the countries by male life expectancy in ascending order and population increase, in descending order

# In[174]:


countries.sort_values(['mlexp', 'popincr'],ascending = [True, False]).head()


# ### Q6. Using the data frame forestfires.csv, perform the following operations:

# In[175]:


forest = pd.read_csv('forestfires.csv')
forest.head()


# #### i) group the data frame by the variable fire (no/yes, 0/1), select the cases with the temperature over 20 and compute the average wind speed

# In[176]:


gbfire = forest[forest['temp']>20].groupby(by="fire").mean()
gbfire['wind']


# #### ii) select the cases with the RH over 30 and compute the average temperature

# In[177]:


rhover30 = forest[forest['RH'] > 30].mean()
rhover30['temp']


# #### iii) sort the observations by temperature, in descending order

# In[178]:


forest.sort_values(by="temp", ascending=False).head()


# #### iv) count the number of unique values in the variables RH

# In[179]:


forest['RH'].nunique()


# #### v) count the observations in each category of the variable fire

# In[180]:


forest['fire'].value_counts()


# #### vi) select the observations where the variable rain is greater than zero and compute the average temperature for these observations

# In[181]:


rainover0 = forest[forest['rain'] > 0].mean()
rainover0['temp']


# ### Q7. Using the data frames people1.csv and people2.csv, perform the following operations:

# In[182]:


p1 = pd.read_csv('people1.csv')
p1.head()


# In[183]:


p2 = pd.read_csv('people2.csv')
p2.head()


# #### i) get the rows that can be found in both data frames

# In[184]:


df1 = pd.merge(p1,p2,how='inner')
df1


# #### ii) join the data frames (discarding the common rows)

# In[185]:


df2 = pd.concat([p1,p2])
df2.drop_duplicates(keep=False)


# #### iii) get the rows that can be found in people1.csv, but not in people2.csv

# In[186]:


df3 = pd.merge(p1,p2,how='left')
df3


# #### iv) get the rows that can be found in people2.csv, but not in people3.csv

# In[187]:


df4 = pd.merge(p1,p2,how='right')
df4


# #### v) verify whether the data frames are identical

# In[188]:


p1.equals(p2)


# ### Q8. Join the data frames car-owners.csv and car-models.csv using all the join types you know (inner join, right join, left join, full join). Observe and explain the results.

# In[189]:


c1 = pd.read_csv('car-owners.csv')
c1.head()


# In[190]:


c2 = pd.read_csv('car-models.csv')
c2.head()


# In[191]:


inner_c = pd.merge(c1,c2,how='inner')
inner_c


# In[192]:


left_c = pd.merge(c1,c2,how='left')
left_c


# In[193]:


right_c = pd.merge(c1,c2,how='right')
right_c


# In[194]:


outer_c = pd.merge(c1,c2,how='outer')
outer_c


# ### Q9. Join the data frames actors.csv and movies.csv using all the join types you know (inner join, right join, left join, full join). Observe and explain the results.

# In[195]:


actors = pd.read_csv('actors.csv')
actors.head()


# In[196]:


movies = pd.read_csv('movies.csv')
movies.head()


# In[197]:


inner_am = pd.merge(actors, movies, how='inner')
inner_am


# In[198]:


left_am = pd.merge(actors, movies, how='left')
left_am


# In[199]:


right_am = pd.merge(actors, movies, how='right')
right_am


# In[200]:


outer_am = pd.merge(actors, movies, how='outer')
outer_am


# ### Q10. Using the bankloan.csv data frame, build a column chart that represents the average balance by housing loan category (housing) for the married customers.

# In[201]:


bank = pd.read_csv('bankloan.csv')
bank.head()


# In[202]:


bank1 = bank[bank['marital']=='married'].groupby('housing').mean()
bank1.balance.plot.bar()


# ### Q13. Using the bankloan.csv data frame, build a mean plot chart that represents the average duration by education level, for the customers who have a personal loan (loan).

# In[203]:


bank2 = bank[bank['loan']=='yes'].groupby('education').mean()
bank2.duration.plot.bar()


# ### Q16. Using the countries.csv data frame, build a scatterplot chart that represents the relationship between the male life expectancy (mlexp) and female life expectancy (flexp), for the countries with a population increase greater than or equal to 1.

# In[204]:


countries.head()


# In[205]:


sns.scatterplot(x="mlexp",y="flexp", data=countries[countries['popincr']>=1])
plt.show()


# ### Q17. Using the forestfires.csv data frame, build a scatterplot chart that represents the relationship between temperature and wind speed, for the observation where the RH is over 39.

# In[206]:


forest.head()


# In[207]:


sns.scatterplot(x="temp",y="wind", data=forest[forest['RH']>=39])
plt.show()


# ### Q18. Using the company.csv data frame, build a scatterplot chart that represents the relationship between job time and salary, for the female employees (gender=2).

# In[208]:


company.head()


# In[209]:


sns.scatterplot(x="jobtime",y="salary", data=company[company['gender']==2])
plt.show()


# ### Q20. Using the forestfires.csv data frame, build a histogram of temperature by the categories of the variable fire (0/1, no/yes).

# In[210]:


forest.head()


# In[211]:


sns.histplot(data=forest[forest['fire']==0], x="temp", y="fire")


# In[223]:


sns.histplot(data=forest[forest['fire']==1], x="temp", y="fire")


# ### Q21. Using the vehicles.csv data frame, build a histogram of horsepower by vehicle type.

# In[224]:


veh.head()


# In[225]:


sns.histplot(data=veh, x="horsepow", y="type")


# ### Q22. Using the bankloan.csv data frame, build a boxplot chart of age by default categories (no/yes).

# In[226]:


bank.head()


# In[227]:


sns.boxplot(x="default", y="age", data=bank)
plt.show()


# ### Q24. Using the vehicles.csv data frame, build a boxplot chart of engine size by vehicle type

# In[228]:


veh.head()


# In[229]:


sns.boxplot(x="type", y="engine", data=veh)
plt.show()


# ### Q26. Import the olympics_data.csv dataset provided

# In[230]:


olympics = pd.read_csv('olympics_data.csv')
olympics.head()


# #### i) What is the first country in the dataframe ? (The function answer_one should return a Series of the first row)

# In[231]:


def answer_one():
    one = olympics.head(1)
    return one

answer_one()


# #### ii) Which country has won the most gold medals in summer games? (The function answer_two should return a single string value)
# 

# In[232]:


def answer_two():
    two = olympics.sort_values(by="Gold", ascending=False).head(1)
    return two

answer_two()


# #### iii) Which country had the biggest difference between their summer and winter gold medal counts? (The function answer_three should return a single string value

# In[233]:


olympics['Difference'] = abs(olympics['# Summer'] - olympics['# Winter'])


# In[234]:


def answer_three():
    three = olympics.sort_values(by="Difference", ascending=False).head(1)
    return three['Country']

    
answer_three()


# #### iv) Which country has the biggest difference between their summer and winter gold medal counts relative to their total gold medal count? Only include countries that have won at least 1 gold in both summer and winter

# In[235]:


olympics['S+W'] = abs(olympics['# Summer'] + olympics['# Winter'])
olympics['Diff2'] = abs(olympics['S+W'] - olympics['Combined total'])


# In[236]:


df10 = olympics[(olympics['Gold']>=1) & (olympics['Gold.1']>=1)]


# In[237]:


def answer_four():
    four = df10.sort_values(by="Diff2", ascending=False).head(1)
    return four['Country']

    
answer_four()


# #### v) Write a function to update the dataframe to include a new column called "Points" which is a weighted value where each gold medal counts for 3 points, silver medals for 2 points, and bronze medals for 1 point. The function should return only the column (a Series object) which you created.

# In[238]:


def answer_five():
    olympics['Points'] = olympics['Gold.2']*3 + olympics['Silver.2']*2 + olympics['Bronze.2']*1
    five = olympics['Points']
    return five

answer_five()


# ### Q25. The questions in this section are based on the datasets within the archive game-of-thrones.zip. These are intended to give you a feel for what real data looks like out there in the wild. Real data is often messy - contains missing/invalid values, redundant/ unhelpful fields, ambiguities etc. Also, you might need to use more than one dataset or transform the raw data to answer business questions.

# In[219]:


c_p = pd.read_csv('character-predictions.csv')
c_p.head()


# #### i) What percentage of popular characters are dead?

# In[239]:


len(c_p[(c_p['isPopular']==1) & (c_p['isAlive']==0)])/len(c_p[c_p['isPopular']==1])
#52% popular characters are dead


# #### iii) What battle_type is optimal for the for an attacker based on the data provided?

# In[100]:


optimal = battles[battles['attacker_outcome']=='win']
optimal['battle_type'].value_counts(normalize=True)


# In[240]:


#Chances of winning are 31.25% in Pitched Battle, Ambush and Siege


# In[221]:


battles = pd.read_csv('battles.csv')
battles.head()

