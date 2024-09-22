#!/usr/bin/env python
# coding: utf-8

# In[3]:


import streamlit as st
import pandas as pd

dataset = pd.read_excel("ratio_analysis.xlsx")
st.dataframe(dataset)


# In[ ]:




