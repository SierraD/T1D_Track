# T1D_Track.py

import streamlit as st
from streamlit_gsheets import GSheetsConnection

[connections.gsheets]
spreadsheet = "https://docs.google.com/spreadsheets/d/111nDe7ePRJaJ1TpSBkEK87sae92dNLLZUNaWCPyLZrI/edit?gid=0#gid=0"

conn = st.connection("T1D_Track", type=GSheetsConnection)
df = conn.read()
st.write(df)
