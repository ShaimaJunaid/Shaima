#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Consider the following Python dictionary `data` and Python list `labels`:
# 
# ``` python
# data = {'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],
#         'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
#         'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
#         'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}
# 
# labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
# ```
# 
# **1.** Create a DataFrame `df` from this dictionary `data` which has the index `labels`.

# In[2]:


data = {'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],
        'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
        'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df=pd.DataFrame(data,index=labels)
df


# **2.** Display a summary of the basic information about this DataFrame and its data (*hint: there is a single method that can be called on the DataFrame*).

# In[11]:


print("----------Summary of the basic information---------------\n")
print(df.info())


# **3.** Return the first 3 rows of the DataFrame `df`.

# In[10]:


print("---------- Return the first 3 rows of the DataFrame---------------")
df1=df.head(3)
df1


# **4.** Display the 'animal' and 'age' columns from the DataFrame `df`

# In[17]:


print("--------Display the 'animal' and 'age' columns from the DataFrame--------")
print(df[["animal","age"]])


# **5.** Display the data in rows `[3, 4, 8]` *and* in columns `['animal', 'age']'

# In[20]:


print("Display the data in rows [3, 4, 8] and in columns `['animal', 'age']")
print(df.iloc[[3,4,8], [0,1]])


# **6.** Select only the rows where the number of visits is greater than 3.

# In[59]:


print("The rows where the number of visits is greater than 3.")
visit=df["visits"]>3
df[visits]


# **7.** Select the rows where the age is missing, i.e. it is `NaN`.

# In[60]:


print("the rows where the age is missing, i.e. it is NaN\n")
print(df[df['age'].isnull()])


# **8.** Select the rows where the animal is a cat *and* the age is less than 3.

# In[64]:


print("the rows where the animal is a cat and the age is less than 3.")
row=df[(df["animal"] =="cat") & (df["age"] <3)]
print(row)


# **9.** Select the rows where the age is between 2 and 4 (inclusive)

# In[65]:


print("the rows where the age is between 2 and 4 (inclusive)")
age=df[df["age"].between(2,4)]
print(age)


# **10.** Change the age in row 'f' to 1.5.

# In[67]:


print(" the age in row 'f' to 1.5.")
df.loc["f", "age"] = 1.5
df


# **11.** Calculate the sum of all visits in `df` (i.e. the total number of visits).

# In[76]:


print("The sum of all visits in df")
s=df.visits.sum()
print(s)


# **12.** Calculate the mean age for each different animal in `df`.

# In[77]:


print("The mean age for each different animal in df")
mean=df.age.mean()
print(mean)


# **13.** Append a new row 'k' to `df` with your choice of values for each column. Then delete that row to return the original DataFrame.

# In[83]:


print("Append a new row 'k' to df with your choice of values for each column")
df.loc['k'] = ["rabbit",2,2,"no"]
print(df)
print("\n---Delete that row to return the original DataFrame--\n")
df= df.drop('k')
print(df)


# **14.** Count the number of each type of animal in `df`.

# In[88]:


print(" the number of each type of animal in df.")
df["animal"].count()


# **15.** Sort `df` first by the values in the 'age' in *decending* order, then by the value in the 'visits' column in *ascending* order (so row `i` should be first, and row `d` should be last).

# In[97]:


print("Sort df first by the values in the 'age' in decending orderthen")
des=df.sort_values(by=["age","visits"],ascending=[False,True])
print(des)
print("\nthe value in the 'visits' column in ascending order\n")
df.sort_values(by=["visits","age"],ascending=[True,False])


# **16.** The 'priority' column contains the values 'yes' and 'no'. Replace this column with a column of boolean values: 'yes' should be `True` and 'no' should be `False`.

# In[100]:


print("column with a column of boolean values: 'yes' should be True and 'no' should be False\n")
df=df.replace({"priority": {"yes": True,"no": False}})
print(df)


# 17.In the 'animal' column, change the 'snake' entries to 'python'.

# In[101]:


print("change the 'snake' entries to 'python'\n")
df=df.replace({"animal": {"snake":"python"}})
print(df)


# **18.** Load the ny-flights dataset to Python

# In[106]:


data=pd.read_csv("C:/DSA COURSE/ny-flights.csv",encoding='ISO-8859-1')
data


# In[107]:


data.describe()


# **19.** Which airline ID is present maximum times in the dataset

# In[113]:


data["airline_id"].value_counts().reset_index()


# In[116]:


plt.figure(figsize=(13,8))
sns.countplot(x="airline_id",data=data)
plt.show()


# **20.** Draw a plot between dep_delay and arr_delay

# In[117]:


plt.figure(figsize=(14,10))
sns.barplot(x="dep_delay",y="arr_delay",data=data)
plt.show()


# In[123]:


font={'family':'serif','color':'black','size':'20'}
font1={'family':'serif','color':'red','size':'20'}
#plot
plt.figure(figsize=(14,10))
plt.scatter(data["dep_delay"],data["arr_delay"])
plt.xlabel("Departure Delay",fontdict=font)
plt.ylabel("Arrival Delay",fontdict=font)
plt.show()


# In[ ]:




