#!/usr/bin/env python
# coding: utf-8

# In[1]:
import streamlit as st
from google import genai
client = genai.Client(api_key="Your_api_key")

st.set_page_config(
    page_title="SupplyChain AI Assistant",
    page_icon="📦",
    layout="wide"
)
# Sidebar
with st.sidebar:

    st.title("📦 SupplyChain AI")

    st.write("AI-powered Supply Chain Assistant")

    st.divider()

    st.write("### Capabilities")
    st.write("• Inventory Management")
    st.write("• Demand Forecasting")
    st.write("• Logistics")
    st.write("• Procurement")
    st.write("• Warehouse Operations")

    st.divider()

    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []
        st.rerun()
# Main Title
st.title("SupplyChain AI Assistant")
# Session Memory
if "messages" not in st.session_state:
    st.session_state.messages = []

# Welcome Message
if len(st.session_state.messages) == 0:

    st.info("""
👋 Welcome to SupplyChain AI Assistant.

Try asking:

• How can I reduce inventory costs?

• What is EOQ?

• Explain demand forecasting.

• How can warehouses improve efficiency?

• What causes stockouts?
"""
)
# Display Previous Messages
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])
# Chat Input
user_input = st.chat_input(
    "Ask a supply chain question"
)
# Process User Input
if user_input and user_input.strip():

    # Display User Message

    with st.chat_message("user"):
        st.markdown(user_input)

    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    #Role Prompt

    prompt = f"""
You are SupplyChain AI, an expert Supply Chain and Operations Consultant.

Your expertise includes:

- Inventory Management
- Demand Forecasting
- Logistics
- Procurement
- Warehouse Management
- Supply Chain Analytics
- Production Planning
- Supplier Management

Guidelines:

1. Give practical and professional answers.
2. Use headings and bullet points.
3. Explain technical terms simply.
4. Give real business examples whenever possible.
5. Keep responses concise but useful.
6. If a question is outside supply chain, answer politely but briefly.
7. Never claim to have real-time company data.

User Question:

{user_input}
"""

    try:

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        assistant_reply = response.text

    except Exception:

        assistant_reply = """
⚠️ Sorry, the AI service is temporarily unavailable.

Possible reasons:

• API quota exceeded

• Gemini server busy

• Network issue

Please try again in a few moments.
"""

    # Display Assistant Message

    with st.chat_message("assistant"):
        st.markdown(assistant_reply)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": assistant_reply
        }
    )
# In[ ]:




