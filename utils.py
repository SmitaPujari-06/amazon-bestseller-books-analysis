import pandas as pd
import streamlit as st

@st.cache_data
def load_data():
    return pd.read_csv(
        "Amazon bestseller books dataset/Amazon_BestSelling_Books_500.csv"
    )
