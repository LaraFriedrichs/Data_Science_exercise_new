import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly

st.title('Data Science Short Course')
st.write('*This is a test for a streamlit App*')

df = pd.read_csv("data/Banda Arc.csv")

cat_names = df.columns.tolist()[27:]

#st.write(cat_names)

st.multiselect('Chose coloumns',options=cat_names)

col1,col2 = st.columns(2)

with col1:
    el1 = st.selectbox('x-axis',cat_names)
    el2 = st.selectbox('y-axis', cat_names)
with col2:
    fig = plt.figure()
    plt.scatter(df[el1]/1000,df[el2]/1000)
    st.pyplot(fig)

st.dataframe(df)