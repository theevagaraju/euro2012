import pandas as pd
from matplotlib import pyplot as plt
st.set_page_config(layout="wide")
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

st.sidebar.header('User Input')
sorted_unique_team = sorted(df['Team'].unique())
option = st.sidebar.multiselect('Country', sorted_unique_team)
df_option = df[(df.Team.isin(option))]
st.write('Data Dimension: ' +str(df.shape[0])+' **rows** and '+str(df.shape[1]) +' **columns**')
st.write(df.head())
st.markdown("Sorted by **Goals**, **Shots On Target**, **Passing Accuracy**, and **Displinary**")
st.write(df_option[['Team','Goals','Shots on target','Passing Accuracy','Yellow Cards', 'Red Cards']].sort_values(['Team'], ascending = True))
# st.write(df.loc[df.Team.isin(['England', 'Italy', 'Russia']), ['Team','Shooting Accuracy']])


# st.sidebar.markdown('You have chosen : '+ option)


st.markdown("Statistics(Average) for each country on **Goals**, **Shots On Target**, **Passing Accuracy**, **Shooting Accuracy**,**Shots off target**, and **Saves made**")
#filtering data
# 'You selected:', option
st.write(df_option[['Team','Goals','Shots on target','Shots off target','Saves made']].mean())
