import streamlit as st


st.title("Weather Forecast App")
place =st.text_input("Enter Place:")
days=st.slider("Select Days:", min_value=1, max_value=7, help="Select the number of days for the weather forecast (1-7).")
option = st.selectbox("Select data to view",("Temperature","Weather"))

st.subheader(f"{option} for the next {days} days in {place}")
