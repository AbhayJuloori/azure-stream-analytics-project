
### 1. Project Overview

This project demonstrates a real-time data ingestion and processing pipeline using Microsoft Azure services. The primary goal is to ingest simulated real-time data from an IoT device via an Azure Event Hub, process the data using an Azure Stream Analytics (ASA) job, and visualize the results in real-time using Power BI.

---

### 2. Project Components

- **Azure Event Hub:**  
  An instance created to simulate and receive real-time data. It acts as the entry point for streaming data.

- **Azure Stream Analytics Job:**  
  A processing job set up in Azure that reads data from the Event Hub, processes it using a SQL-like query, and sends the output to Power BI.

- **Power BI Dashboard:**  
  A real-time dashboard created to visualize the processed data. This is configured as the output of the ASA job.

- **Python Simulator Script:**  
  A Python script developed to simulate an IoT device by sending JSON-formatted messages (data) to the Event Hub at regular intervals.

---

### 3. Implementation Details

#### 3.1. Azure Event Hub Instance
- **Namespace and Instance:**  
  An Event Hub namespace was created in the Azure Portal, followed by an Event Hub instance (named, for example, `RealTimeDataHub`). This instance is configured with default partitions and message retention settings.
  
- **Shared Access Policies:**  
  The default `RootManageSharedAccessKey` policy was used to secure the connection. The connection string was copied and used later in the ASA job and Python script.

#### 3.2. Azure Stream Analytics Job
- **Job Creation:**  
  A new Stream Analytics job was created in the Azure Portal under the same resource group as the Event Hub. The job was named (e.g., `RealTimeStreamJob`).

- **Input Configuration:**  
  The ASA job was configured to read data from the Event Hub using the connection string from the shared access policy. The input alias was set (e.g., `InputFromEventHub`).

- **Output Configuration (Power BI):**  
  The ASA job was configured to output data directly to Power BI. The output alias (e.g., `PowerBIOutput`), dataset name, and table name were defined. Authorization with the Power BI account was completed through the portal.

- **Stream Analytics Query:**  
  A SQL-like query was written to process the incoming data. For example:
  ```sql
  SELECT 
      DeviceId,
      Temperature,
      Humidity,
      EventEnqueuedUtcTime AS IngestionTime
  INTO 
      PowerBIOutput
  FROM 
      InputFromEventHub
  WHERE 
      Temperature > 25
  ```
  This query filters out events where the temperature is less than or equal to 25 and passes the required data fields to the Power BI output.

#### 3.3. Python Data Simulator
- **Script Purpose:**  
  The Python script (`simulator.py`) was created to simulate an IoT device. It continuously sends JSON-formatted data to the Event Hub.

- **Key Features of the Script:**
  - Uses the `azure-eventhub` package.
  - Generates random temperature and humidity data.
  - Sends data at regular intervals (e.g., every 5 seconds).
  - Includes error handling and logging for debugging purposes.

- **Example Code Snippet:**
  ```python
  import json
  import time
  import random
  from azure.eventhub import EventHubProducerClient, EventData

  connection_str = "YOUR_EVENT_HUB_CONNECTION_STRING"
  eventhub_name = "RealTimeDataHub"

  producer = EventHubProducerClient.from_connection_string(conn_str=connection_str, eventhub_name=eventhub_name)

  while True:
      data = {
          "DeviceId": "Device001",
          "Temperature": random.uniform(20, 35),
          "Humidity": random.uniform(30, 70)
      }
      event = EventData(json.dumps(data))
      with producer:
          producer.send_batch([event])
      print("Sent data: ", data)
      time.sleep(5)
  ```

---

### 4. Testing and Verification

- **Simulated Data Flow:**  
  The Python script was executed locally on a Windows machine, sending simulated sensor data to the Event Hub.
  
- **Monitoring the ASA Job:**  
  The Stream Analytics job was monitored through the Azure Portal. The job diagram, metrics, and query test features were used to ensure that data was being processed correctly.

- **Real-Time Visualization:**  
  The Power BI dashboard was configured to display the incoming data in real-time. Visualizations such as charts and graphs were used to represent temperature and humidity trends.

---

### 5. Deployment and Future Enhancements

- **Deployment:**  
  After testing, the ASA job was started to run continuously in production mode. All configurations were reviewed, and appropriate scaling was set based on expected data volume.

- **Future Enhancements:**
  - **Advanced Analytics:** Integration of more complex queries and windowing functions in ASA.
  - **Alerting and Monitoring:** Setting up alerts in Azure Monitor for system thresholds.
  - **Security Improvements:** Using Managed Identities to improve security and avoid hardcoding credentials.

---

### 6. Conclusion

This project successfully demonstrates the implementation of a real-time data ingestion and processing pipeline using Azure Event Hubs, Azure Stream Analytics, and Power BI. The Python simulator script ensured continuous data flow, while the ASA job processed and filtered the data before sending it to a live Power BI dashboard. This comprehensive approach not only highlights proficiency in Azure technologies but also showcases the ability to integrate various components into a cohesive real-time solution.

---

*Prepared by: Abhay Juloori*  


---
