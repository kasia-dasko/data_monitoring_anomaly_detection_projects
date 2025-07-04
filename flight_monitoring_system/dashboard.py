import streamlit as st
import pandas as pd
from streamlit_autorefresh import st_autorefresh

CSV_FILE = 'flight_data.csv'

st.set_page_config(page_title="Flight data monitoring dashboard", layout="wide")
st.title("Flight data monitoring dashboard")

st_autorefresh(interval=5000, limit=None, key="datarefresh")

try:
    data = pd.read_csv(CSV_FILE)
except FileNotFoundError:
    st.warning("Waiting for flight_data.csv...")
    st.stop()

data['timestamp'] = pd.to_datetime(data['timestamp'], unit='s')
data = data.sort_values('timestamp')

st.subheader("Summary")
normal_count = len(data[data['alert'] == "No alert"])
alert_count = len(data[data['alert'] != "No alert"])

col1, col2 = st.columns(2)
col1.metric("Normal range", normal_count)
col2.metric("Detected anomalies", alert_count)

st.subheader("Recent alerts")
alert_data = data[data['alert'] != "No alert"]
if not alert_data.empty:
    st.dataframe(
        alert_data[['timestamp', 'altitude', 'speed', 'alert']]
        .sort_values(by="timestamp", ascending=False)
        .head(10)
    )
else:
    st.success("No alerts detected")