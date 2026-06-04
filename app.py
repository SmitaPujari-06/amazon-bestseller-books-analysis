import streamlit as st

st.set_page_config(
    page_title="Amazon Bestselling Books Dashboard",
    page_icon="📚",
    layout="wide"
)

st.title("📚 Amazon Bestselling Books Dashboard")

st.markdown("""
Analyze Amazon's Top 500 Bestselling Books.

### Features
- Dataset Overview
- Category Analysis
- Author Insights
- Price & Rating Analysis

Use the sidebar to navigate.
""")
