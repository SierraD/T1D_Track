# T1D_Track.py

import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd
import numpy as np

st.header("T1D Tracking")
st.write("V0; 2025-04-20")

conn = st.connection("gsheets", type=GSheetsConnection)

data = conn.read()

df_WO = pd.DataFrame(data, columns=("%dHR" % i for i in range(25)))
st.write(df_WO)
df_W = pd.DataFrame(data, columns=("%dHRW" % i for i in range(25)))
st.write(df_W)

st.write(df_WO["0HR"][0])
s0 = np.zeros(len(df_WO["0HR"]))
st.write(s0)

# chart = st.scatter_chart(x=s0, y=df_WO["0HR"])

# chart = st.scatter_chart(df_W)

# st.scatter_chart(
#     chart_data,
#     x="col1",
#     y="col2",
#     color="col4",
#     size="col3",
# )

