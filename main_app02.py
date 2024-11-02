import streamlit as st
from PIL import Image

st.title('test アプリ')
st.caption('これはテストアプリです')

image = Image.open('./data/dog_shibainu_brown.png')
# st.image(image)
st.image(image, width=200)
