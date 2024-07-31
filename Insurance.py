import streamlit as st
import pandas as pd
import altair as alt
from PIL import Image
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

st.set_page_config(
    page_title="Eden Care Insurance Dashboard",
    page_icon=Image.open("C:/Users/Student/Downloads/Documents/Eden Care/Health Insurance/EC_logo.png"),
    layout="wide",
    initial_sidebar_state="expanded")
st.markdown(
    """
    <style>
    .reportview-container {
        background-color: #013220;
        color: white;
    }
    .sidebar .sidebar-content {
        background-color: #013220;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.markdown('''
    <style>
        .main-title {
            color: #E66C37; /* Title color */
            text-align: center; /* Center align the title */
            font-size: 3rem; /* Title font size */
            font-weight: bold; /* Title font weight */
            margin-bottom: .5rem; /* Space below the title */
            text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.1); /* Subtle text shadow */
        }
        div.block-container {
            padding-top: 2rem; /* Padding for main content */
        }
    </style>
''', unsafe_allow_html=True)
st.markdown('<h1 class="main-title">EDEN CARE SERVICES DASHBOARD</h1>', unsafe_allow_html=True)
logo = "ECM_logo.png"
st.sidebar.image(logo, use_column_width=True)

# Your Streamlit app content
st.sidebar.success("Select from the options above")

