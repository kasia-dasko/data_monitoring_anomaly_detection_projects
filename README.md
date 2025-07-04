**Flight Monitoring System**

The Flight Monitoring System is an entry-level project demonstrating the use of real-time data streaming and visualization technologies within the aviation industry. The project consumes live flight data (such as altitude and speed) using Apache Kafka, analyzes it for potential anomalies (e.g., exceeding safe thresholds), saves the data to a CSV file, and visualizes it on an interactive dashboard built with Streamlit. In aviation, such systems are crucial for ensuring flight safety and enabling rapid response to critical situations. This project serves as a foundational base that can be extended with advanced features like automatic alert notifications (SMS/email), integration with databases, and enhanced analytical dashboards.

**Technologies used:**

1. Python – main programming language
2. Apache Kafka – real-time data streaming platform
3. Streamlit – for building the interactive dashboard

**How to run the project**

1. Install the required Python packages:
   python3 -m pip install -r requirements.txt
   
2. Start the necessary containers using Docker Compose:
   docker-compose up -d
   
3. Start the data producer to simulate flight data:
   python3 kafka/producer.py

4. Start the data consumer which receives data, generates alerts, and writes to CSV:
   python3 kafka/consumer.py
   
5. Launch the streamlit dashboard to visualize the data:
   python3 -m streamlit run dashboard.py


The dashboard refreshes automatically every 5 seconds to show current data and alerts and runs on the default endpoint: http://localhost:8501.  


