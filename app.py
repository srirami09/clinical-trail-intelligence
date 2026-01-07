
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os


st.set_page_config(
    page_title="Clinical Trial Intelligence",
    layout="wide"
)

st.title("Integrated Clinical Trial Intelligence Platform")
DATA_FOLDER = "data"

if not os.path.exists(DATA_FOLDER):
    st.error("❌ Data folder not found")
    st.stop()

files = os.listdir(DATA_FOLDER)

if len(files) == 0:
    st.warning("⚠️ No data files found")
    st.stop()

selected_file = st.selectbox("Select a dataset", files)
file_path = os.path.join(DATA_FOLDER, selected_file)

df = pd.read_csv(file_path)

st.success("Streamlit is working successfully 🎉")

st.write("Welcome! This is your first working Streamlit app.")
st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Go to",
    ["Overview", "Data Quality", "Charts", "About"]
)

if page == "Overview":
    st.subheader("Overview")
    st.write("This section gives a summary of the clinical trial data.")

elif page == "Data Quality":
    st.subheader("Data Quality Checks")
    st.write("Missing values, duplicates, basic statistics will appear here.")

elif page == "Charts":
    st.subheader("Visualizations")
    st.write("Charts and graphs will be displayed here.")

elif page == "About":
    st.subheader("About")
    st.write("Clinical Trial Intelligence Dashboard built using Streamlit.")
import pandas as pd

df = pd.read_csv("data/sample_data.csv")
st.subheader("Clinical Trial Data")
st.dataframe(df)
st.subheader("Download Data")
csv = df.to_csv(index=False).encode("utf-8")
st.download_button(
    label="Download filtered data as CSV",
    data=csv,
    file_name="filtered_clinical_trials.csv",
    mime="text/csv",
)
st.subheader("Key Metrics")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Trials", len(df))
col2.metric("Completed", (df["status"] == "Completed").sum())
col3.metric("Ongoing", (df["status"] == "Ongoing").sum())
col4.metric("Planned", (df["status"] == "Planned").sum())

st.subheader("📊 Visual Analytics")

# Phase-wise count
st.subheader("Phase-wise Trial Count")
phase_counts = df["phase"].value_counts()
st.bar_chart(phase_counts)

# Status-wise pie chart
st.subheader("Status Distribution")
status_counts = df["status"].value_counts()

import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.pie(
    status_counts,
    labels=status_counts.index,
    autopct="%1.1f%%",
    startangle=90
)
ax.axis("equal")
st.pyplot(fig)
st.subheader("Trial Status Distribution (Bar Chart)")
st.bar_chart(status_counts)

st.subheader("Summary")

col1, col2, col3 = st.columns(3)

col1.metric("Total Trials", len(df))
col2.metric("Completed", status_counts.get("Completed", 0))
col3.metric("Ongoing", status_counts.get("Ongoing", 0))
phase = st.selectbox("Filter by Phase", ["All"] + sorted(df["phase"].unique()))

if phase != "All":
    df = df[df["phase"] == phase]


