#!/usr/bin/env python

# coding: utf-8

# In[1]:


#the first keyword for defining a functino is 'def'



# In[2]:


def first_function():
    
    print('We did it!')


# In[3]:


#the function and its body above does not execute, rather
#it defines the function. It seems the cool guys calls it 'declare', not sure though

#That aside, while still on the matters of mortals and mere humans, phhh! ...

#To execute the function, we must 'call' the function. 


# In[4]:


first_function()


# In[ ]:





# In[6]:


#Arguments:


# In[7]:


def number_squared(number):
    print(number**2)


# In[8]:


number_squared(5)


# In[ ]:





# In[20]:


def number_squared_cust(number, power):
    print(number**power)


# In[21]:


number_squared_cust(5,2)


# In[22]:


#If you have two arguments in your function, you have
#to pass in two parameters, you can't just pass in 
# 5 only, or 2 only. Doing that will return an error.


# In[ ]:





# In[ ]:





# In[ ]:





# In[23]:


#ARBITARY ARGUMENTS.


# In[24]:


#If you don't know how many arguments you're going to 
#pass to the function, it is possible to define 
#something called an arbitrary argument. So that you
#specify that later, when you're running the function, so you don't have to know upfront, what the argument values are.


# In[27]:


#typically, in many tutorials, it is common to find arbitrary arguments defined in functions as seen...:


def number_args(*args)


# In[29]:


#We are going to define ours as *numbers, so... :



def number_args(*number):
    print(number[0]*number[1])


# In[ ]:





# In[30]:


def number_args(*number):
    print(number[0]*number[1])


# In[34]:


number_args(5,6,1,2)


# In[ ]:


#since the outlined numbers are a tuple, we can 
#clearly define the tuple. 

#and then run the function by calling the tuple.


# In[43]:


args_tuple = (5,6,1,2,8)


def number_args(*number):
    print(number[0]*number[1]*number[2]*number[3]*number[4])


# In[44]:


number_args(*args_tuple)


# In[ ]:




