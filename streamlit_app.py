import streamlit as st
import pandas as pd

st.title('Machine Learning App')

st.info('This is a machine learning app')

df = pd.read_csv("penguins_cleaned.csv")
