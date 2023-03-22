#!/usr/bin/env python

# coding: utf-8

# In[13]:



#Method 1:

    
def number_squared (number, power):
    
    print(number**power)


# In[14]:


number_squared(5,2)


# In[9]:


#Method 2:
    
def number_squared (number, power):
    print(number**power)
    
  


# In[15]:


number_squared(power = 5, number = 2)

#we call this keyword arguments, it gives us more control.


# In[ ]:





# In[32]:


#ARBITRARY KEYWORD ARGUMENT: Means we don't know exactly how many keyword arguments
#we intend to pass into our function. So we'll just put **number, so that later we will be 
#able to specify it.

def number_klark(**number):
    print('My number is:' + number['integer'] + ' My other number is: ' + number['integer2'])


# In[33]:


number_klark(integer = '300', integer2 = '3.14')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




