import streamlit as st
import pandas as pd
from utils import load_master_data, analyze_shortlist, get_total_cgpa_distribution
import plotly.express as px

st.set_page_config(page_title="Student Shortlist CGPA Analysis")
st.title("Student Shortlist CGPA Analysis")

# Load master dataset
try:
    master_df = load_master_data()
    # Show total CGPA distribution from master file
    total_stats = get_total_cgpa_distribution(master_df)
    st.subheader("📊 Total Student Distribution by CGPA (Master Data)")
    st.dataframe(total_stats)
    fig_total_pie = px.pie(total_stats, names="CGPA Range", values="Count", title="Total CGPA Distribution", hole=0.3)
    st.plotly_chart(fig_total_pie, use_container_width=True)
except Exception as e:
    st.error(f"Error loading master data: {e}")
    st.stop()

# Load master dataset
try:
    master_df = load_master_data()
except Exception as e:
    st.error(f"Error loading master data: {e}")
    st.stop()

st.subheader("Upload Shortlisted Students Excel File")
uploaded_file = st.file_uploader("Choose an Excel file", type=["xlsx"])

if uploaded_file:
    try:
        shortlist_df = pd.read_excel(uploaded_file)
        st.subheader("Preview of Uploaded File")
        st.dataframe(shortlist_df)
        # Check for required columns
        required_cols = ["Registration Number", "Full Name"]
        missing_cols = [col for col in required_cols if col not in shortlist_df.columns]
        if missing_cols:
            st.error(f"Uploaded file must contain columns: {required_cols}. Found columns: {list(shortlist_df.columns)}")
        else:
            shortlisted_stats, not_shortlisted_stats = analyze_shortlist(master_df, shortlist_df)

            st.subheader("📊 Shortlisted Students Distribution by CGPA")
            st.dataframe(shortlisted_stats)
            fig_shortlisted_pie = px.pie(shortlisted_stats, names="CGPA Range", values="Count", title="Shortlisted CGPA Distribution", hole=0.3)
            st.plotly_chart(fig_shortlisted_pie, use_container_width=True)
            st.bar_chart(shortlisted_stats.set_index("CGPA Range")["Count"])

            st.subheader("📊 Not Shortlisted Students Distribution by CGPA")
            st.dataframe(not_shortlisted_stats)
            fig_not_shortlisted_pie = px.pie(not_shortlisted_stats, names="CGPA Range", values="Count", title="Not Shortlisted CGPA Distribution", hole=0.3)
            st.plotly_chart(fig_not_shortlisted_pie, use_container_width=True)
            st.bar_chart(not_shortlisted_stats.set_index("CGPA Range")["Count"])
    except Exception as e:
        st.error(f"Error processing uploaded file: {e}")
else:
    st.info("Please upload a shortlist Excel file to begin analysis.")
