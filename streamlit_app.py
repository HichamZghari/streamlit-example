from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

# Title
st.title("This is a title")

# Header
st.header("This is a header") 
 
# Subheader
st.subheader("This is a subheader")

# Text
st.text("Test")

# Markdown
st.markdown("### This is a markdown")

# success
st.success("Success")

st.write(pd.DataFrame({
    'first column': [1, 2], 'second column': [10, 20, 30],
}))