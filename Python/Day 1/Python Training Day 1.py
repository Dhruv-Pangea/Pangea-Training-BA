#!/usr/bin/env python
# coding: utf-8

# #### Q1.	Write a function that accepts a string and checks whether it is a palindrome at a word level and returns a Boolean. Concretely, a string like “He was so he” is a palindrome by this definition because the last word is identical to first and the last second word is equal to the second word. The function should be case insensitive, meaning it should return True for both “ThEY CAME CAME tHey” and “they came came they”. Bonus: Write a version of the function that ignores any punctuation/numbers that might be present in the string.

# In[1]:


import re

def check_palindrome(text):
  text = text.lower()
  text = re.sub('[^A-Za-z0-9]+', ' ', text)
  words = text.split()
  words_reversed = list(reversed(words))
  if words == words_reversed:
    return True
  else:
    return False

check_palindrome(input("Type a sentence to check if it's a palindrome or not: "))


# #### Q2.	Given 2 lists [1,2,3,4,5,6] and [73, 26, 65, 30, 15, 85] use list comprehension to multiply the corresponding elements of the lists and return a list containing the products. Use of numpy is forbidden for this question and will result in negative marking if used. (This was something that came up in class)

# In[2]:


Q2_L1 = [1,2,3,4,5,6]
Q2_L2 = [73,26,65,30,15,85]

Q2_L3 = [Q2_L1[i] * Q2_L2[i] for i in range(0, len(Q2_L1))]
Q2_L3


# #### Q3. How do you find all pairs of an integer array whose sum is equal to a given number?
# #### Given Input Array: [2, 4, 3, 5, 6, -2, 4, 7, 8, 9] 
# #### Given Sum: 7 
# #### Integer numbers, whose sum is equal to value: (2, 5) (4, 3) (3, 4) (-2, 9)
# 

# In[3]:


def pairs(given_array, given_sum):
    
    for i in range(0, len(given_array)):
        
        for j in range(i+1, len(given_array)):
            
            if (given_array[i] + given_array[j] == given_sum):
                print("Pair: ", (given_array[i], given_array[j]))

given_array = [2, 4, 3, 5, 6, -2, 4, 7, 8, 9]
given_sum = 7

pairs(given_array, given_sum)


# #### Q4.	Given a list with names of people like some_people = ['Sir Issac Newton', 'Mr Nikola Tesla', 'Dr Erwin Schrodinger', 'Dr. Richard Feynman'] generate a list with that contains the honorific-Lastname combinations. Concretely, we need ['Sir Newton', 'Mr Tesla', 'Dr Schrodinger', 'Dr. Feynman']. This was already solved in class (almost). Hint: This one easier to solve if broken down into subproblems. 
# #### a.	We already know how to manipulate individual strings – try to describe this logic as function
# #### b.	Apply this function to the list

# In[4]:


name_list = ['Sir Issac Newton', 'Mr Nikola Tesla', 'Dr Erwin Schrodinger', 'Dr. Richard Feynman']

def extract_title_last(list_of_names):
  name_list_updated = [' '.join(name.split()[::len(name.split())-1]) for name in name_list]
  return name_list_updated

print(extract_title_last(name_list))


# #### Q5. Here’s a question that brings a few things together. Many organizations have user ids which are constrained in some way. Imagine you work at an internet service provider and the user ids are all two letters followed by two numbers (e.g., aa49). Your task at such an organization might be to hold a record on the billing activity for each possible user. Generate a list of all possible user ids (Bonus points for using list comprehension)

# In[5]:


lowercase = 'abcdefghijklmnopqrstuvwxyz'
digits = '0123456789'
all_possibilities = [''.join([lowercase[l1],lowercase[l2],digits[d1],digits[d2]]) for l1 in range(26) for l2 in range(26) for d1 in range(10) for d2 in range(10)]
print(all_possibilities[:30])
# Another way of performing it 
all_possibilities = [l1+l2+d1+d2 for l1 in lowercase for l2 in lowercase for d1 in digits for d2 in digits]
print(all_possibilities[:50])


# #### Q6. Write a function that accepts two lists as input and returns the common elements of both the lists (and an empty list there are common elements) as output. Hint: We learnt about a data-structure that was tailormade for something like this.

# In[6]:


empty_list =[]

def common_elements(a, b):
    a_set = set(a)
    b_set = set(b)
 
    if (a_set & b_set):
        print(a_set & b_set)     
    else:
        print(empty_list)
          
  
a = [1, 2, 3, 4, 5, 6, 7]
b = [5, 6, 7, 8, 9]
common_elements(a, b)
  
a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]
common_elements(a, b)


# #### Q7. Write python program to import data from multiple sources like excel sheet(.xlsx,.csv), text file (.txt), SQL database (MySQL server) using Classes.

# In[7]:


# Importing Excel file using classes

import pandas as pd

class sample(object):

    df = pd.read_excel('Email Analysis.xlsx')

    sample = df.values.tolist()

    print(sample)


# In[8]:


#Importing a text file into Python 

file = open('apology.txt', 'r')
file


# In[9]:


#Importing SQL file into Python 

query = open('Sample-SQL-File-10rows.sql', 'r')
query


# #### Q8. Check whether a substring is present in a string. Also, print the total length (count of characters) of the original string. 
# #### Original string: Football 
# #### Substring: ball 
# #### Expected Result: The given substring is present. 
# #### Total length = 8

# In[10]:


def check(string, sub_str):
    if (string.find(sub_str) == -1):
        print("The given substring is not present")
    else:
        print("The given substring is present")
            
# driver code
string = "Football"
sub_str ="ball"
check(string, sub_str)
len(string)


# #### Q9. Find the largest prime divisor of 299792458 using python

# In[11]:


import math
  
def maxPrimeFactors (n):
    maxPrime = -1
    while n % 2 == 0:
        maxPrime = 2
        n >>= 1
          
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            maxPrime = i
            n = n / i
    if n > 2:
        maxPrime = n
    return int(maxPrime)
  
n = 299792458
print(maxPrimeFactors(n))


# #### Q10. The file apology.txt contains the text of Socrates’ apology. Generate a dictionary of the 20 most frequent words (as keys) and their counts (as values) occurring in the text after omitting Apology.txt

# In[12]:


import re
string = open('apology.txt').read()
new_str = re.sub('[^a-zA-Z0-9\n\.]', ' ', string)
open('output.txt', 'w').write(new_str)

text = open("output.txt", "r")

d = dict()

for line in text:

    line = line.strip()

    line = line.lower()

    words = line.split(" ")
    

    for word in words:
        if word in d:

            d[word] = d[word] + 1
        else:
            d[word] = 1

list1 = []
for key in list(d.keys()):
    list1.append((key, d[key]))


# In[13]:


def Convert(list1, di):
    di = dict(list1)
    return di

dictionary = {}
print (Convert(list1, dictionary))


# In[14]:


from operator import itemgetter

N=20

res = dict(sorted((Convert(list1, dictionary)).items(), key = itemgetter(1), reverse = True)[:N])

print("The top N value pairs are  " + str(res))

