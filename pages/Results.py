
import streamlit as st
from itertools import cycle
import sys
import os
from PIL import Image
import requests
import glob
st.header("PREDICTA RESULTS PAGE ")
imagelist=glob.glob("./reslutsimage/*.jpeg")

st.image(imagelist,use_column_width=True, caption=['Results'] *len(imagelist))
# filteredImages = ["https://github.com/Cedric0852/predicta/blob/main/reslutsimage/Results.jpeg?raw=true":"https://github.com/Cedric0852/predicta/blob/945552a1853a3d8659492f6dc564d48c98fe6d3b/reslutsimage/1.jpeg"] # your images here
# caption = ["Results"] # your caption here
# cols = cycle(st.columns(4)) # st.columns here since it is out of beta at the time I'm writing this
# for idx, filteredImage in enumerate(filteredImages):
#     next(cols).image(filteredImage, width=150, caption=caption[idx])