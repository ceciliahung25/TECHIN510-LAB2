import streamlit as st
import pandas as pd
import plotly.

st.set_page_config(
    page_title="Penguins Explorer",
    page_icon="🐧",
    layout="centered",
)

st.title("🐧 Penguins Explorer")

df = pd.read_csv("https://raw.githubusercontent.com/mcnakhaee/palmerpenguins/master/palmerpenguins/data/penguins.csv")

#Input filter option
bill_length_slider = st.slider(
    "Bill Length (mm)",
    min(df["bill_length_mm"]),
    max(df["bill_length_mm"]),
)

df = df[df["bill_length_mm"] > bill_length_slider]

species_filter = st.selectbox(
    "Species",
    df["species"].unique(),
    index = None
)
st.write(species_filter)

#Filter Data
if species_filter:
    df = df[df["species"] == species_filter]

islands_filter = st.multiselect,("Island", df["Island", df["island"]])

if islands_filter:
    df=df[df["species"] == species_filter]







# st.selectbox("Species",["Adelie","Chinstrap"])

# st.selectbox("Species", df["species"], unique())
# st.multiselect("Species", df["species"], unique())
# st.write(df)