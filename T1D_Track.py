# T1D_Track.py

import streamlit as st
from streamlit_gsheets import GSheetsConnection

conn = st.connection("gsheets", type=GSheetsConnection)
df = conn.read()
st.write(df)
