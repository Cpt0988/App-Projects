import streamlit as st
import pandas

st.set_page_config(layout="wide")
col1, col= st.columns(2)

with col1:
    st.title("The Best Company",)
    content="""
    Introduce to be filled out later.
    """
    st.info(content)
    st.text("Our Team")
    
col2,empty1,col3,empty2,col4 = st.columns([1.5,0.5,1.5,0.5,1.5])
df = pandas.read_csv("data.csv", sep=",")

with col2:
    for index, rows in df[:4].iterrows():
        st.subheader(f"{rows['first name'].title()} {rows['last name'].title()}")
        st.write(rows["role"])
        st.image("images/"+rows["image"])
        
with col3:
    for index, rows in df[4:8].iterrows():
        st.subheader(f"{rows['first name'].title()} {rows['last name'].title()}")
        st.write(rows["role"])
        st.image("images/"+rows["image"])
        
with col4:
    for index, rows in df[8:].iterrows():
        st.subheader(f"{rows['first name'].title()} {rows['last name'].title()}")
        st.write(rows["role"])
        st.image("images/"+rows["image"])