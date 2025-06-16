import pandas as pd
import streamlit as st
import matplotlib as pyplot
import numpy as np
import seaborn as sns


#read a csv file
#import csv file
#convert file to dataframe


df = pd.read_csv("diabetes.csv")
st.markdown("# First Five Items")
st.write(df.head())

df = pd.read_csv("diabetes.csv")
st.markdown("# last Five Items")
st.write(df.tail())

st,title("General Information About Diabetes Analysis")
st.narkdown('#Overview')
hall = df.describe
st.write(hall)