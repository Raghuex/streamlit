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

with st.expander('Data visualization'):
  st.scatter_chart(data=df, x='bill_length_mm', y='body_mass_g', color='species')

# SideBar
with st.sidebar:
  st.header('Input features')
  island = st.selectbox('Island', ('Biscoe', 'Dream', 'Torgersen'))
  gender = st.selectbox('Gender', ('male', 'female'))
  #creating slider for numeric data using their min-max
  bill_length_mm = st.slider('Bill length (mm)', 32.1, 59.6)
  bill_depth_mm = st.slider('Bill depth (mm)', 13.1, 21.5)
  flipper_length_mm = st.slider('Flipper length (mm)', 172.0, 231.0)
  body_mass_g = st.slider('Body mass (g)', 2700.0, 6300.0)

# create a dataframe for input features
data = {
  'island':island,
  'bill_length_mm': bill_length_mm,
  'bill_depth_mm': bill_depth_mm,
  'flipper_length_mm': flipper_length_mm,
  'body_mass_g': body_mass_g,
  'sex': gender
}

input_df = pd.DataFrame(data, index=0)
  

  
