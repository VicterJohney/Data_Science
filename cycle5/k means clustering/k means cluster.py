#!/usr/bin/env python
# coding: utf-8

# In[65]:


from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import pandas as pd
customers = pd.read_csv('customer_data.csv')
customers.head()


# In[66]:


kmeans = KMeans(n_clusters=4, random_state=0)
kmeans.fit(points)
predicted_cluster_indexes = kmeans.predict(points)
plt.scatter(x, y, c=predicted_cluster_indexes, s=50, alpha=0.7, cmap='viridis')


# In[67]:


kmeans = KMeans(n_clusters=6, random_state=0)
kmeans.fit(points)
predicted_cluster_indexes = kmeans.predict(points)
plt.scatter(x, y, c=predicted_cluster_indexes, s=50, alpha=0.7, cmap='viridis')
centers = kmeans.cluster_centers_
plt.scatter(centers[:, 0], centers[:, 1], c='red', s=100)


# In[68]:


centers = kmeans.cluster_centers_
plt.scatter(centers[:, 0], centers[:, 1], c='red', s=100)


# In[69]:


kmeans = KMeans(n_clusters=9, random_state=0)
kmeans.fit(points)
predicted_cluster_indexes = kmeans.predict(points)
plt.scatter(x, y, c=predicted_cluster_indexes, s=50, alpha=0.7, cmap='viridis')
centers = kmeans.cluster_centers_
plt.scatter(centers[:, 0], centers[:, 1], c='red', s=100)


# In[70]:


#Display the cluster labels of each point.(print cluster indexes)
print(predicted_cluster_indexes)


# In[ ]:




