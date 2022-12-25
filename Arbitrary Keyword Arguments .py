#!/usr/bin/env python
# coding: utf-8

# In[2]:


#We can define a function's parameter as seen below:


def number_squared_cust(number, power):
    print(number**power)


# In[3]:


#and call it as such:

number_squared_cust(5,2)


# In[4]:


#Cool right?

#We actually can also have more control, based on how
#we define the parameters.


# In[ ]:





# In[8]:


def number_squared_cust(number, power):
    print(number**power)


# In[9]:


number_squared_cust(power = 5, number = 2)


# In[10]:


#So, typically, 5 is assigned to number, and 2 to power
#...perhaps, based on the arrangements. However, with 
#what the cool guys call 'keyword arguments' - we just
#switched things. Control!! CONTROLLL...LAHAHAHAHAHAHA!!!


# In[12]:


#So because of our alteration, where we would formerly 
#have 5**2 = 25, we now have 2**5 = 32. 

#Thanks to Keyword Arguments.


# In[ ]:





# In[ ]:




