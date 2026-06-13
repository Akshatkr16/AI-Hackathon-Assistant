#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
st.title("Chat Memory Demo")
if "messages" not in st.session_state:
    st.session_state.messages = []
message = st.text_input("Type a message")
if st.button("Send"):
    st.session_state.messages.append(message)
st.write("Conversation History")
for msg in st.session_state.messages:
    st.write(msg)
# In[ ]:




