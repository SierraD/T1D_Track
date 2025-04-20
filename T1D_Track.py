# T1D_Track.py

import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd

st.header("T1D Tracking")
st.write("V0; 2025-04-20")

conn = st.connection("gsheets", type=GSheetsConnection)

data = conn.read()

df_WO = pd.DataFrame(data, columns=("%dHR" % i for i in range(25)))
st.write(df_WO)
df_W = pd.DataFrame(data, columns=("%dHRW" % i for i in range(25)))
st.write(df_W)

st.write(df_W.name)

# st.scatter_chart(
#     chart_data,
#     x="col1",
#     y="col2",
#     color="col4",
#     size="col3",
# )

