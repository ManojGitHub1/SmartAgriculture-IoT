# SmartAgriculture-IoT
IoT-based smart agriculture monitoring system using ThingSpeak

## IoT Application: Smart Agriculture System
### 1. Devices (Sensors) Used for Smart Agriculture
For a smart agriculture IoT system, the following sensors would be utilized:

Soil Moisture Sensors: Measure water content in soil to optimize irrigation
Temperature Sensors: Monitor ambient and soil temperature
Humidity Sensors: Track atmospheric humidity levels
Light Intensity Sensors: Measure sunlight exposure for crop growth analysis
pH Sensors: Monitor soil acidity/alkalinity
Rainfall Sensors: Measure precipitation levels
Water Level Sensors: Monitor water levels in reservoirs and irrigation systems
Leaf Wetness Sensors: Detect moisture on leaf surfaces to predict plant diseases
CO2 Sensors: Measure carbon dioxide levels for greenhouse management
Wind Speed/Direction Sensors: Track weather conditions affecting crops

### 2. Proposed Cloud-Based Architecture
![image](https://github.com/user-attachments/assets/864eb659-9250-4bd3-bd3b-4fc085f49977)

The proposed cloud-based architecture consists of the following layers:

Field Layer:

Multiple sensor nodes deployed across the agricultural field
Each node equipped with different types of sensors (moisture, temperature, etc.)
Battery-powered with solar recharging capabilities
Low-power wireless communication (LoRaWAN, ZigBee, or BLE)


Fog/Edge Computing Layer:

IoT Gateway for data aggregation and preprocessing
Local data storage for offline operation
Edge analytics for real-time decision making
Protocol translation (converting sensor protocols to internet protocols)


Network Layer:

Internet connectivity via Wi-Fi, cellular (4G/5G), or LoRaWAN
Secure data transmission using TLS/SSL
Bandwidth management for efficient data transfer


Cloud Layer (ThingSpeak):

Data ingestion through ThingSpeak channels
Data storage in ThingSpeak database
Data analytics for pattern recognition and predictions
Visualization through ThingSpeak dashboards
Alert system for critical conditions
API access for third-party applications


Application Layer:

Web and mobile interfaces for farmers
Automated control systems for irrigation and fertilization
Decision support system based on analytics
Reporting and notification services



### 3. ThingSpeak Cloud Platform Setup
To set up the ThingSpeak cloud environment for our Smart Agriculture system:

Create a ThingSpeak Account:

Navigate to thingspeak.com and sign up for a new account
Verify email and log in to the platform


Create a New Channel:

From the dashboard, click on "Channels" → "New Channel"
Configure channel settings with appropriate name and description
Enable fields for each sensor type (temperature, humidity, soil moisture, etc.)
Set channel visibility (private or public)
Save the channel configuration


API Keys and Access:

Note the Write API Key for sending data to the channel
Note the Read API Key for reading data from the channel
Configure channel sharing settings if needed


MQTT Setup:

Configure MQTT settings for real-time data streaming
Set up device credentials for secure communication


ThingHTTP Integration:

Configure ThingHTTP for external API integration if needed
Set up webhooks for notifications and alerts

![image](https://github.com/user-attachments/assets/828f0f56-9cfb-4699-a0d6-0b807ad27c12)


### 4. Creating a Channel with Sensor Dataset
For our Smart Agriculture application, I've created a dataset that simulates readings from various sensors over a 24-hour period. This dataset includes:

Soil moisture readings (%)
Temperature values (°C)
Humidity levels (%)
Light intensity (lux)
Soil pH values
Rainfall measurements (mm)
Battery level (%)
Wind speed level (km/hr)

Dataset creation procedure:

Create a CSV file with headers matching ThingSpeak field names and template
Generate realistic values with appropriate variations for a 24-hour cycle
Add timestamps for each data point
Upload the dataset to ThingSpeak using the API or bulk import feature


### 5. Dashboard Creation with Sensor Data Visualization

![image](https://github.com/user-attachments/assets/c4823964-53ea-43da-a312-762058c896a0)


The ThingSpeak dashboard for our Smart Agriculture system includes the following visualizations:

Soil Moisture and Rainfall Graph:

Line chart showing soil moisture percentage over time
Bar chart overlay showing rainfall events
Threshold line indicating optimal moisture levels


Temperature and Humidity Gauge:

Current temperature display with color-coded ranges
Current humidity display with visual indicator
Historical temperature/humidity correlation graph


Soil Health Panel:

pH level indicator with acceptable range highlighting
Soil moisture adequacy indicator
Nutrient level estimation based on sensor data


Environmental Conditions:

Light intensity chart showing daily patterns
Weather condition summary
Daily environmental statistics


System Status:

Sensor node battery levels
Last data update timestamps
System health indicators


Alert Configuration:

Drought condition alerts
Frost warning alerts
Heavy rainfall alerts
Unusual pH change alerts


The dashboard is designed to provide farmers with actionable insights at a glance, with options to drill down into more detailed data for advanced analysis. Color coding is used throughout to quickly identify conditions requiring attention.
