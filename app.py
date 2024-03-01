import streamlit as st
view = [100,150,300]
st.write('# youtube view')
st.write('## raw')
view
st.write('## bar chart')
st.bar_chart(view)
import pandas as pd
sview = pd.Series(view)
sview