import os
import streamlit as st
from google import genai
from dotenv import load_dotenv
load_dotenv("api_key.env")

# Gemini Client
client = genai.Client(api_key= os.getenv("GEMINI_API_KEY"))

# Page Configuration
st.set_page_config(
    page_title="GuideAI",
    page_icon="logo.png",
    layout="wide"
)

# Session Memory
if "messages" not in st.session_state:
    st.session_state.messages = []

# Sidebar
with st.sidebar:
    st.image("logo.png", width=120)
    st.title("GuideAI")
    st.write("Choose an expert mode")

    assistant_mode = st.selectbox(
        "Choose Expert Mode",
        [
            "Supply Chain Consultant",
            "Data Analyst",
            "Mechanical Engineer"
        ]
    )

    st.caption(f"Current Mode: {assistant_mode}")

    st.divider()

    st.write("### Capabilities")

    if assistant_mode == "Supply Chain Consultant":
        st.write("• Inventory Management")
        st.write("• Demand Forecasting")
        st.write("• Logistics")
        st.write("• Procurement")
        st.write("• Warehouse Operations")

    elif assistant_mode == "Data Analyst":
        st.write("• SQL")
        st.write("• Excel")
        st.write("• Power BI")
        st.write("• Python")
        st.write("• Statistics")

    else:
        st.write("• Thermodynamics")
        st.write("• Fluid Mechanics")
        st.write("• SOM")
        st.write("• Manufacturing")
        st.write("• CAD / CFD")

    st.divider()

    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []
        st.rerun()

# Main Page
st.title("GuideAI")

# Welcome Message
if len(st.session_state.messages) == 0:

    st.info(
        f"""
Welcome to {assistant_mode} Mode.

Ask anything related to this domain.
"""
    )

# Display Previous Messages
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        if message["role"] == "assistant":
            st.caption(f"Expert: {message.get("Mode", "AI")}")
        st.markdown(message["content"])

# Chat Input
user_input = st.chat_input(
    "Ask your question..."
)

# Process User Input
if user_input and user_input.strip():

    # Show User Message
    with st.chat_message("user"):
        st.markdown(user_input)

    # Store User Message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    # Conversation History
    conversation_history = ""

    for msg in st.session_state.messages:

        conversation_history += (
            f"{msg['role']}: {msg['content']}\n"
        )

    # Role Prompts
    if assistant_mode == "Supply Chain Consultant":

        role_prompt = """
You are an expert Supply Chain and Operations Consultant.

Expertise:
- Inventory Management
- Demand Forecasting
- Procurement
- Logistics
- Warehouse Management

Give practical business-focused answers.
Use headings and bullet points.
"""

    elif assistant_mode == "Data Analyst":

        role_prompt = """
You are an expert Data Analyst.

Expertise:
- SQL
- Excel
- Power BI
- Python
- Statistics
- Data Visualization

Explain concepts clearly with examples.
Use headings and bullet points.
"""

    else:

        role_prompt = """
You are an expert Mechanical Engineer.

Expertise:
- Thermodynamics
- Fluid Mechanics
- SOM
- TOM
- Manufacturing
- CAD
- CFD

Explain engineering concepts simply and practically.
Use headings and bullet points.
"""

    # Final Prompt
    prompt = f"""
{role_prompt}

Conversation History:

{conversation_history}

Current User Question:

{user_input}
"""

    # Gemini Response
    try:
        with st.spinner("Thinking..."):
            response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        assistant_reply = response.text

    except Exception as e:

        assistant_reply = f"""
 AI service temporarily unavailable.

Reason:
{str(e)}

Please try again.
"""

    # Show Assistant Message
    with st.chat_message("assistant"):
        st.caption(f"Expert: {assistant_mode}")
        st.markdown(assistant_reply)

    # Save Assistant Message
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": assistant_reply,
            "mode": assistant_mode
        }
    )