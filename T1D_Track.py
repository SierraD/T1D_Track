# T1D_Track.py

import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd
import numpy as np

st.header("T1D Tracking")
st.write("V0; 2025-04-20")

conn = st.connection("gsheets", type=GSheetsConnection)

data = conn.read(worksheet="Sheet1")

df_WO = pd.DataFrame(data.T)
# df_WO = pd.DataFrame(data, columns=("%dHR" % i for i in range(25)))
# df_WO = df_WO.T
# st.write(df_WO)
# df_W = pd.DataFrame(data, columns=("%dHRW" % i for i in range(25)))
# df_W = df_W.T
# st.write(df_W)

chart = st.scatter_chart(df_WO)
# chart.add_rows(df_W)
