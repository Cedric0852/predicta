
import streamlit as st
from itertools import cycle
import sys
import os
st.header("PREDICTA RESULTS PAGE ")
filteredImages = ["https://github.com/Cedric0852/predicta/blob/main/reslutsimage/Results.jpeg?raw=true"] # your images here
caption = ["Results"] # your caption here
cols = cycle(st.columns(4)) # st.columns here since it is out of beta at the time I'm writing this
for idx, filteredImage in enumerate(filteredImages):
    next(cols).image(filteredImage, width=150, caption=caption[idx])