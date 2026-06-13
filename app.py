#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
st.title("SupplyChain AI Assistant")
user_query = st.text_input("Ask a question")
if user_query:
    st.write("You asked: ",user_query)

# In[ ]:




