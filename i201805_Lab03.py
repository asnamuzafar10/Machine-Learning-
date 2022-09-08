#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# ### Initialising a random vector

# In[2]:


vector = np.random.randint(9, size = (3,1))
vector


# ### Finding the orthogonal vector of the initialised vector

# In[3]:


vector[:-1]


# In[4]:


col = 0
row = len(vector)
sum1 = 0
for i in range(0,row-1):
    sum1 = sum1 + vector[i][col]
sum1 = sum1*-1
sum1


# In[5]:


row = row - 1
sum1 = sum1/vector[row][col]
row += 1
sum1


# In[6]:


orth = np.ones(vector.shape)
orth


# In[7]:


for i in range(0,row):
    if(i == row-1):
        orth[i][col] = sum1
orth


# In[8]:


print(vector.shape)
print(orth.shape)


# In[9]:


dot = np.dot(vector.T,orth)
dot


# In[10]:


print("\n\nAngle between the two vectors: ", np.arccos(dot))


# ### Taking projection of random vector on orthogonal and vice versa

# In[77]:


p1 = np.dot(vector.T, orth)/(np.dot(vector.T, vector))*vector
p2 = np.dot(orth.T, vector)/(np.dot(orth.T, orth))*orth
print(p1)
print(p2)


# ### Find the initial vectors from the projections

# In[78]:


#We cannot recreate the original vector since the projection is zero


# ### Take two vectors and project one on the other, and find the initial vectors from the projections

# In[16]:


v1 = np.random.randint(9, size = (2,1))
v2 = np.random.randint(9, size = (2,1))
print(v1)
print(v2)


# In[18]:


p11 = np.dot(v1.T, v2)/(np.dot(v1.T, v1))*v1
p22 = np.dot(v2.T, v1)/(np.dot(v2.T, v2))*v2
print(p11)
print(p22)


# In[19]:


dot1 = np.dot(vector.T,orth)
print("\n\nAngle between the two vectors: ", np.arccos(dot1))
print("\nProjection of A onto B",p11)
print("\nProjection of B onto A",p22)


# ### Take the Iris dataset and compute the eigenvalues and eigenvectors

# In[31]:


from numpy import genfromtxt
iris = genfromtxt('iris.csv', delimiter=',')
iris = iris[1:,:-1]
iris


# In[38]:


square = iris[:3,2:]  
square.shape


# In[44]:


ev1, ev2 = np.linalg.eig(square)
print("\nEigenvalues of the Iris dataset\n\n: ", ev1)
print("\nEigenvectors of the Iris dataset:\n\n ", ev2)


# ### Change the Iris data to zero-centered data using techniques learned in the class

# In[48]:


df = np.mean(iris,axis=0)
broadcast = np.ones(len(iris)*5).reshape(-1,5)
mean = df*broadcast
z = iris-mean


# ### Do the same with the ECG dataset provided in the GCR

# In[54]:


df2 = genfromtxt('ECG200_TRAIN.csv', delimiter ='  ')
df2


# In[55]:


center = np.mean(iris,axis=0)
broadcast = np.ones(len(iris)*5).reshape(-1,5)
mean = center*broadcast
z = iris-mean


# In[ ]:




