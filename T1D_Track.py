# T1D_Track.py

import streamlit as st
from streamlit_gsheets import GSheetsConnection

st.header("T1D Tracking")
st.write("V0; 2025-04-20")

conn = st.connection("gsheets", type=GSheetsConnection)

df = conn.read()
dd = st.dataframe(df)
st.write(df["0HR"])


# st.scatter_chart(
#     chart_data,
#     x="col1",
#     y="col2",
#     color="col4",
#     size="col3",
# )

