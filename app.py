import streamlit as st
import pandas as pd
import os

st.write(os.listdir("archive"))
st.write(os.listdir("archive/price_data"))

df = pd.read_csv("archive/price_data/AAPL.csv")

st.title("Test DataFrame S&P 500")
st.dataframe(df)
