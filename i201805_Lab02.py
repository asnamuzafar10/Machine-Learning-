#!/usr/bin/env python
# coding: utf-8

# # Task 1

# In[39]:


class University:
    __campus=6 #__ is private _ is protected
    def __init__(self,uname,location):
        self.uname = uname
        self.location = location
    def __display2(self):
        print("This is a protected function")
    def display(self):
        #print("\nName: ", self.name, "\nLocation: ", self.location)
        print(f'\nName: {self.uname} \nLocation: {self.location}')
   
class Department(University): #Inheritance
        def __init__(self,name,program, u_name, u_location):
            super().__init__(u_name,u_location)
            #University.__init__()
            self.name = name
            self.program=program
        def display(self):
            super().display()
            print(f"\nName: {self.name} \nPrograms: {self.program}")


# In[40]:


obj2 =University("FAST", "Islamabad")
obj2.__display2()


# In[29]:


obj1=Department("AI",5,"FAST",'Islamabad')
obj1.display()


# # Task 2

# In[31]:


IvyLeague = ['Harvard', 'Yale', 'Columbia', 'Princeton', 'Dartmouth', 'Princeton', 'Cornell', 'Brown']

print("\nList of Ivy League Universities: ")
for i, value in enumerate(IvyLeague,1):
    print('\n',i,value)


# # Task 3

# ## Part 1

# In[46]:


l1 = ['aura', 'I', 'wander', 'aqua', 'blob', 'field', 'I', 'wonder', 'tart', 'life']
count = 0
for i in range(0,len(l1)):
    if(len(l1[i])>=2):
        first = l1[i][0]
        last = l1[i][-1]
        if(first==last):
            count+=1
print("\nNumber of Strings with length greater than 2 and the same first and last characters: ", count)


# ## Part 2

# In[74]:


l2 = ['blob', 'crate', 'xanax', 'forever', 'korea', 'x-ray', 'twelve']
group = []
for i in range(0,len(l2)):
    if(l2[i][0]=='x'):
        group.append(l2[i])
group


# In[78]:


for i in group:
    for j in l2:
        if (j == i):
            l2.remove(j)
l2


# In[80]:


res = group + l2
res


# ## Part 3

# In[86]:


tup = [(1,2,3), (2,3,8), (3,7,5), (7,1,2)]

for i in range(0,len(tup)): 
    for j in range(0,(len(tup)-i-1)): 
            if(tup[j][-1]>tup[j+1][-1]): 
                temp = tup[j] 
                tup[j] = tup[j + 1] 
                tup[j+1] = temp 
tup


# ## Part 4

# In[98]:


l1 = [7,9,6,13,13,10,8,8,5]
l2 = []
for i in range(0,(len(l1)-1)):
    if(l1[i]!=l1[i+1]):
        l2.append(l1[i])
l2


# ## Part 5

# In[109]:


l1 = [5,1,3,7,8]
l2 = [4,2,9,6]
l1.sort()
l2.sort()
l1


# In[110]:


l2


# In[111]:


res = l1 + l2
res


# In[112]:


res.sort()
res


# # Task 4

# In[113]:


import numpy as np
import pandas as pd


# In[114]:


df = pd.read_csv("drinks.csv")
df.head()


# In[115]:


#Getting number of rows
rows = df.shape[0]
rows


# In[116]:


#Dropping na values
df.dropna(axis = 0, inplace = False)


# In[120]:


#A function that takes name of the column and outputs the data in column
col = input('\nPlease enter the name of the column: ')
df.loc[:,col]


# In[123]:


#plot histograms of data
df.hist()


# In[128]:


#2D Scatterplot
import matplotlib.pyplot as plt
plt.scatter(df.country, df.wine_servings)


# In[133]:


#3D Scatterplot
x = df['beer_servings']
y = df['spirit_servings']
z = df['wine_servings']
mplt = plt.figure().gca(projection='3d')
mplt.scatter(x,y,z)
mplt.set_xlabel('Spirit Servings')
mplt.set_ylabel('Wine Servings')
mplt.set_zlabel('Beer Servings')
plt.show()


# In[142]:


#pie chart
country = df['country'].head(10)
x = df['beer_servings'].head(10)
fig = plt.figure(figsize =(10, 7))
plt.pie(x, labels = country)


# In[148]:


#bar chart
fig = plt.figure(figsize = (10, 5))
plt.bar(x, country, color ='maroon',
        width = 5.2)
plt.ylabel("Country")
plt.xlabel("Beer Servings")
plt.title("Beer Servings across countries")
plt.show()


# In[ ]:




