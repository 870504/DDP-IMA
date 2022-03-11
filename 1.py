#!/usr/bin/env python
# coding: utf-8

# In[1]:


def case_count(input):
    upper = 0
    lower = 0
    for letter in input:
        if letter.isupper():
            upper += 1
        elif letter.islower():
            lower += 1

    print("Uppercase: " + str(upper), "Lowercase: " + str(lower))


case_count("Hello World")


# In[3]:


def unique_letters(input):
    res = []
    for letter in input:
        if not letter.isalpha():
            continue
        
        if letter.upper() not in res and letter.lower() not in res:
            res.append(letter.upper())
    
    return res, len(res)

input = "Yifeng Li"
print(unique_letters(input))


# In[ ]:




