# T1D_Track.py

import streamlit as st
from streamlit_gsheets import GSheetsConnection

st.header("T1D Tracking")
st.write("V0; 2025-04-20")

conn = st.connection("gsheets", type=GSheetsConnection)

df = conn.read()
st.write(df[0])

#data = st.dataframe(df)
#st.write(data)


