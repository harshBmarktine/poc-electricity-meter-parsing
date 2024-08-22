import streamlit as st
from parsing import obj_elec_meter_parsing
from PIL import Image
import os
import pandas as pd


st.sidebar.image("https://marktine.com/wp-content/uploads/2024/07/marktine_new_logo.png", use_column_width=True)
with st.sidebar:
    st.write("129, Shri Hans Marg, Usha Vihar, Keshav Vihar, Arjun Nagar, Jaipur, Rajasthan 302018")



st.title("Upload Multiple Images")

# Upload multiple images
uploaded_files = st.file_uploader("Choose images", type=["png", "jpg", "jpeg"], accept_multiple_files=True)
save_dir="upload Image"


# If files are uploaded
if uploaded_files:
    list_file = []
    for uploaded_file in uploaded_files:
        # Open the image using PIL
        
        img = Image.open(uploaded_file)
        file_path = os.path.join(save_dir, uploaded_file.name)
        img.save(file_path)
        list_file.append(save_dir+"/"+uploaded_file.name)
    

    parse_data = obj_elec_meter_parsing.main(list_file)

    data  = pd.DataFrame(parse_data)

    st.dataframe(data)

    