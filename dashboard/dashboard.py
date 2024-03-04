import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
sns.set(style='dark')

def create_season_df(df_day):
    season_df = df_day.groupby(by='season', observed=True).agg({
    'count': 'sum'
    }).reset_index()
    return season_df

def create_day_type(df_day):
    average_counts = df_day.groupby('day_type', observed=True)['count'].mean().reset_index()
    return average_counts

data = pd.read_csv('main_data.csv')

min_date = data["datetime"].min()
max_date = data["datetime"].max()

with st.sidebar:
    
    st.header("Proyek Data Analisis")
    st.subheader("By Denny Rianto")

    with st.expander("About Dataset"):
        st.write(
            """Bike-sharing rental process is highly correlated to the environmental and seasonal settings. For instance, weather conditions,
            precipitation, day of week, season, hour of the day, etc. can affect the rental behaviors. The core data set is related to  
            the two-year historical log corresponding to years 2011 and 2012 from Capital Bikeshare system, Washington D.C., USA which is 
            publicly available in http://capitalbikeshare.com/system-data. We aggregated the data on two hourly and daily basis and then 
            extracted and added the corresponding weather and seasonal information. Weather information are extracted from http://www.freemeteo.com.
            """
        )

season_df = create_season_df(data)
day_type_df = create_day_type(data)

st.header('Welcome to Bike Sharing Dashboard!')

col1, col2, col3 = st.columns(3)
 
with col1:
    st.metric(label="Bikers Count", value=season_df['count'].sum())
    st.caption("This show total of users including registered and casual users.")
 
with col2:
    st.metric(label="Total Registered", value=data['registered'].sum())
    st.caption("This show total of registered users.")
 
with col3:
    st.metric(label="Total Casual", value=data['casual'].sum())
    st.caption("This show total of casual users.")

st.caption("")
st.subheader("Data Visualization")

tab1, tab2 = st.tabs(["Count by Season", "Count by Day Type"])
 
with tab1:
    st.subheader("Count by Season", divider="red")
    plt.figure(figsize=(10,5)) 
    plt.bar(season_df['season'],season_df['count'], color="#ff6f68")
    plt.title("Bikers Count by Season")
    plt.ticklabel_format(style='plain', axis='y')
    st.pyplot(plt)
    st.caption("""This indicates that the trend in bicycle usage is highly influenced by seasonal changes. 
               The number of bicycle users peaks in the Fall season, where cool weather and beautiful scenery may be determining factors. 
               Conversely, during the Spring season, there is a decrease in bicycle user activity, 
               possibly due to weather conditions that are not yet fully stable after winter.""")
 
with tab2:
    st.subheader("Count by Day Type", divider="red")
    plt.figure(figsize=(10,5)) 
    plt.bar(day_type_df['day_type'],day_type_df['count'], color="#ff6f68")
    plt.title("User Count by Day Type")
    st.pyplot(plt)
    st.caption("""This indicates that that the number of bicycle users tends to peak during holidays and weekends. 
               This can be interpreted as the leisure time and greater freedom on these days providing a positive boost to participation 
               in cycling activities. Conversely, on workdays, there is a noticeable decrease in bicycle user activity, possibly due to time 
               constraints and work obligations.""")

st.caption('Copyright (c) 2024 Denny Rianto')