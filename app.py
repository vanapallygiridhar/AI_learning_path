import streamlit as st
from utils import run_agent_sync

st.set_page_config(
    page_title="SkillPath AI",
    page_icon="🚀",
    layout="wide"
)


st.title("🚀 SkillPath AI")
st.subheader("Personalized Learning Roadmap Generator")

st.markdown("""
Generate a structured day-wise roadmap for any skill using Gemini AI.

Examples:

- Learn Python in 30 days
- Become a Data Analyst in 45 days
- Learn Machine Learning from scratch
- Master DSA in 60 days
""")

# Session state
if "is_generating" not in st.session_state:
    st.session_state.is_generating = False

# Sidebar
st.sidebar.header("Configuration")

google_api_key = st.sidebar.text_input(
    "Google Gemini API Key",
    type="password"
)

# Main Input
user_goal = st.text_area(
    "What do you want to learn?",
    placeholder="Example: Learn Python in 30 days"
)

# Generate Button
if st.button(
    "Generate Learning Roadmap",
    type="primary",
    disabled=st.session_state.is_generating
):

    if not google_api_key:
        st.error("Please enter your Google Gemini API Key.")
    elif not user_goal:
        st.error("Please enter a learning goal.")
    else:

        st.session_state.is_generating = True

        try:
            with st.spinner("Generating roadmap..."):

                result = run_agent_sync(
                    google_api_key=google_api_key,
                    user_goal=user_goal
                )

            st.success("Roadmap generated successfully!")

            st.markdown("---")
            st.markdown(result)

        except Exception as e:
            st.error(str(e))

        finally:
            st.session_state.is_generating = False