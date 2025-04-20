# T1D_Track.py

import streamlit as st
from streamlit_gsheets import GSheetsConnection

conn = st.connection("T1D_Track", type=GSheetsConnection)
df = conn.read()
st.write(df)
