#!/usr/bin/env python
# coding: utf-8

# In[2]:


from nltk.corpus import stopwords
import nltk


# In[4]:


from nltk.tokenize import sent_tokenize,word_tokenize
nltk.download('punkt')
text1 = "The data set given satisfies the requirement for model generation. This is used in Data Science Lab"
print(sent_tokenize(text1))


# In[5]:


print(word_tokenize(text1))


# In[7]:


nltk.download('stopwords')
print(stopwords.words('english'))


# In[8]:


text = word_tokenize(text1)
text= [word for word in text if word not in stopwords.words('english')]
print(text)


# In[10]:


nltk.download('averaged_perceptron_tagger')
print(nltk.pos_tag(text))


# In[11]:


temp=zip(*[text[i:] for i in range(0,2)])
ans=[' '.join(ngram) for ngram in temp]
print(ans)


# In[12]:


temp=zip(*[text[i:] for i in range(0,4)])
ans=[' '.join(ngram) for ngram in temp]
print(ans)


# In[ ]:




