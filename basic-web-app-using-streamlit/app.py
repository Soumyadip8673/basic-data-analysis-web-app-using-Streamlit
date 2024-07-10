# imports
import streamlit as st
import pandas as pd 
import seaborn as sns

# heading & sub-heading
st.title("Data Analysis")
st.subheader("Data analysis using python and streamlit")

# upload & read data
upload=st.file_uploader("upload your dataset in csv format")

if upload is not None:
    df=pd.read_csv(upload)

# show data
if upload is not None:
    if st.checkbox("preview data"):
        if st.button("Head"):
            st.write(df.head(5))
        if st.button("Tail"):
            st.write(df.tail(5)) 

# check data types of each column
if upload is not None:
    if st.checkbox("Data types of each column"):
        st.text("Data Types")
        st.write(df.dtypes)

# find shape of the dataset
if upload is not None:
    if st.checkbox("Shape of dataset"):
        st.text("Shape")
        st.write("Number of Rows :",df.shape[0])
        st.write("Number of Columns :",df.shape[1])

# find null values in the data set
if upload is not None:
    isNull=df.isnull().values.any()
    if isNull:
        if st.checkbox("Show null values in the dataset"):
            sns.heatmap(df.isnull())
            st.pyplot()
            st.set_option('deprecation.showPyplotGlobalUse', False)
    else:
        st.success("YAY!!! No Null values in the dataset")

# handling duplicate values
if upload is not None:
    dup=df.duplicated().any()
    if dup:
        st.warning("dataset having duplicate values")
        dupRemv=st.selectbox("Do you want to remove duplicate values ?",("Select one","Yes","No"))
        if dupRemv=='Yes':
            df=df.drop_duplicates()
            st.success("Duplicate values dropped!!!")
        if dupRemv=='No':
            st.text("Okay , No problem....Your dataset is fine with duplicates")
    else:
        st.text("Dataset does not contain any duplicatae values")

# getting overall statistics about dataset
if upload is not None:
    if st.checkbox("Show summary of the dataset"):
        st.write(df.describe(include='all'))

# about
if st.button("About App"):
    st.text("A simple web application, made using Streamlit and python")
    st.text("To perform basic operations (EDA) on any dataset (must be in .csv format), like - \n1.showing the first & last 5 rows\n2.number of rows and columns\n3.Data types of each column\n4.Checking Null values\n5.Checking Duplicate values\n6.Getting overall summary")
    st.warning("Upload a csv file first to perform these operations.")
    st.text("Thanks to Streamlit.")
if st.button("By"):
    st.warning("Developed by : Soumyadip Jana")
if st.button("Contact Us"):
    st.text("soumyadip729cr@gmail.com")