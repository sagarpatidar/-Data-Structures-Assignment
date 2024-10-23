#!/usr/bin/env python
# coding: utf-8

# Q1. How do you comment code in Python? What are the different types of comments?

# In python comments are used to eplain and annotate code. making it easir ti undertand there are two primary types of 
# comment 
# 1. single line commnet - single  line comment with # symbol 
# 2. Multiple_line comment (block comments ) - Python does not 
# have a special syntax for multi-line commnets 
# but you can achieve this by using multiple- line comments 
# print ("Multiple line comments ")
# 

# Q2. What are variables in Python? How do you declare and assign values to variables?

# IN python variables are used to store data values. A varibale is 
# essentiallt a name that pints to a memory lostion where the data is 
# stored 
# 1. Declaring Varible:
#     variable_name = vaue 
# 2. assigning_value = 
# x = 10 # integer value assign 
# name = "ssd" # string value assign 
# pi = 2.3  # float value assign 
# is_active = true 
#   
# Multiple assignments 
# a,v,d,g = 23,34,42,23
#   
# same value multiple variables 
# x = y = z = 100 
Q3. How do you convert one data type to another in Python?
# In python you can convert one data type using type conversion. 
# there are two types main types of type convcertion 
# 1- implicit type conversion = pytohn autmatically convert one data type to another when required 
# 2 = Explicit type onvertion = You manually convert a data type using 
# python's build in funciton . This is also callled type casting 
# 

# Q4. How do you write and execute a Python script from the command line?

# to write and execute a python script form the command line 
# follow those steps 
# 1. writting a pytohn cript 
# 2. executing the python Scripyt form tje command line
# 3. Run the python cript 
# 4. varifying python installation 
# 
# 

# Q5. Given a list my_list = [1, 2, 3, 4, 5], write the code to slice the list and obtain the sub-list [2, 3].

# In[2]:


my_list = [1,2,3,4,5]
sub_list = my_list[1:3] # slicing form index 1 to index 3 (executing 3)
print (sub_list) # output:[2,3]                  


# Q6. What is a complex number in mathematics, and how is it represented in Python?

# In amthermatics a complex numeber is a mnimenr that consist of two Parts:
#     1 real part: A real number 
#     2 Imaginary part: A mulplitple of the imagonary unit i where i is a sqare root of 
#         -1 
#      A complex number is tpyically written in form of  
#     z = a+bi 
#     Reperesent in python 
#     a is real part 
#     b is imagonary part 
#     j is used instead of i to reperesnt the imaginary unit in python 
#     

# In[6]:


z = 3+4j 
print(z)


# Q7. What is the correct way to declare a variable named age and assign the value 25 to it?

# The correct way to declare a varibale named age and assign the value 25 is 
# 

# In[7]:


age = 25 


# age is the varibale name. 
# = is the assignment operator , which assign the value 
# on teh right (25) to the varibale on the left 
# 25 is the integer value being assign to age 
# after the declaration , the varible age holds the value 25

# To declare name price and assign teh value 9.99 to it 
# you can write 
# price = 9.99
# 

# In[9]:


price = 9.99 
print (type(price ))


# It's belong to float 

# Q9. Create a variable named name and assign your full name to it as a string. How would you print the
# value of this variable?

# To create a variable named and assign your full name to it 
# as a string, you write 
# 

# In[17]:


name = "Sagar Patidar"
print (name)


# Q10. Given the string "Hello, World!", extract the substring "World".

# In[19]:


text = "Hellow, world!"
substring = text[7:13] #slicing from index 7 to 12 
print (substring )


# Q11. Create a variable named "is_student" and assign it a boolean value indicating whether you are
# currently a student or not.

# In[20]:


is_student = True  # If you are currently a student


# In[21]:


is_student = False  # If you are not currently a student


# In[22]:


is_student = True
print(is_student)  # Output: True


# In[23]:


is_student = False
print(is_student)  # Output: False


# In[ ]:




