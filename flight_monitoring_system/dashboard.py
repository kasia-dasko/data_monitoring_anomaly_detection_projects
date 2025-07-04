import streamlit as st
import pandas as pd
import time

CSV_FILE = 'flight_data.csv'

st.set_page_config(page_title="Flight data monitoring dashboard", layout="wide")
st.title("Flight data monitoring dashboard")

placeholder = st.empty()

while True:
    try:
        data = pd.read_csv(CSV_FILE)
    except FileNotFoundError:
        st.warning("Waiting for flight_data.csv...")
        time.sleep(1)
        continue

    data['timestamp'] = pd.to_datetime(data['timestamp'], unit='s')
    data = data.sort_values('timestamp')

    with placeholder.container():
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Altitude over time")
            st.line_chart(data.set_index('timestamp')['altitude'])

        with col2:
            st.subheader("Speed over time")
            st.line_chart(data.set_index('timestamp')['speed'])

        st.subheader("🚨 Recent Alerts")
        alert_data = data[data['alert'].notnull() & (data['alert'] != "")]
        if not alert_data.empty:
            st.dataframe(alert_data[['timestamp', 'altitude', 'speed', 'alert']].sort_values(by="timestamp", ascending=False).head(10))
        else:
            st.success("No alerts detected.")

    time.sleep(3)