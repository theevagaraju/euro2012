import streamlit as st
import numpy as np
import pandas as pd
# st.set_page_config(layout="wide")
st.title('EURO 2020 ANALYSIS')# st.set_page_config(layout="wide")
st.markdown("""
This app is developed by Theevagaraju to perform an analysis on EURO 2020
* **Python**: pandas,streamlit
""")
@st.cache
def load_data():
   data = pd.read_csv("Euro_2012_stats_TEAM.csv",encoding= 'unicode_escape')
   return data
df = load_data()
st.write('Data Dimension: ' +str(df.shape[0])+' **rows** and '+str(df.shape[1]) +' **columns**')
st.write(df.head())
st.markdown("Sorted by **Goals**, **Shots On Target**, **Passing Accuracy**, and **Displinary**")
st.write(df[['Team','Goals','Shots on target','Passing Accuracy','Yellow Cards', 'Red Cards']].sort_values(['Team'], ascending = True))
# st.write(df.loc[df.Team.isin(['England', 'Italy', 'Russia']), ['Team','Shooting Accuracy']])

st.sidebar.header('User Input')
option = st.sidebar.selectbox('Country',df['Team'])
st.sidebar.markdown('You have chosen : '+ option)



