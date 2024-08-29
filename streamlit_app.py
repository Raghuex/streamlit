import streamlit as st
import pandas as pd

st.title('Machine Learning App')

st.info('This is a machine learning app')

with st.expander('Data'):
  st.write('**Raw data**')
  df = pd.read_csv("penguins_cleaned.csv")
  df

  st.write('**X**')
  X_raw = df.drop('species', axis=1)
  X_raw

  st.write('**y**')
  y_raw = df.species
  y_raw
