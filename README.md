# 🌱 Smart Agriculture IoT
**IoT-based Smart Agriculture Monitoring System using ThingSpeak**

## 🚀 IoT Application: Smart Agriculture System
This system leverages IoT sensors and cloud computing to provide real-time monitoring and automated decision-making for agriculture.

---
## 📡 1. Devices (Sensors) Used
The following sensors are utilized for data collection:

| Sensor Type          | Function                                      |
|----------------------|-----------------------------------------------|
| 🌱 Soil Moisture    | Measures water content in soil               |
| 🌡️ Temperature     | Monitors ambient and soil temperature        |
| 💧 Humidity        | Tracks atmospheric humidity levels           |
| ☀️ Light Intensity | Measures sunlight exposure for crop growth   |
| 🧪 pH Sensor       | Monitors soil acidity/alkalinity            |
| ☔ Rainfall        | Measures precipitation levels                |
| 🌊 Water Level    | Monitors water levels in reservoirs          |
| 🍃 Leaf Wetness   | Detects moisture on leaf surfaces           |
| 💨 CO2 Sensor     | Measures carbon dioxide levels in greenhouse |
| 🌬️ Wind Speed/Direction | Tracks weather conditions affecting crops |

---
## ☁️ 2. Cloud-Based Architecture
The architecture consists of the following layers:
![image](https://github.com/user-attachments/assets/864eb659-9250-4bd3-bd3b-4fc085f49977)

### 🔹 **Field Layer**
- Multiple sensor nodes deployed across the field
- Battery-powered with solar recharging
- Low-power wireless communication (LoRaWAN, ZigBee, BLE)

### 🔹 **Fog/Edge Computing Layer**
- IoT Gateway for data aggregation and preprocessing
- Local data storage for offline operation
- Edge analytics for real-time decision-making
- Protocol translation (sensor to internet protocols)

### 🔹 **Network Layer**
- Internet connectivity (Wi-Fi, 4G/5G, LoRaWAN)
- Secure data transmission (TLS/SSL)
- Bandwidth optimization

### 🔹 **Cloud Layer (ThingSpeak)**
- Data ingestion via ThingSpeak channels
- Storage, analytics, and visualization
- Alert system for critical conditions
- API access for third-party applications

### 🔹 **Application Layer**
- Web & mobile interfaces for farmers
- Automated irrigation & fertilization control
- Decision support system with analytics
- Reporting & notification services

---
## 🛠 3. ThingSpeak Cloud Setup
### ✅ Create a ThingSpeak Account
1. Go to [ThingSpeak](https://thingspeak.com) and sign up.
2. Verify email and log in.

### ✅ Create a New Channel
1. Navigate to **Channels → New Channel**.
2. Configure settings:
   - Name and description
   - Enable fields for each sensor (temperature, humidity, etc.)
   - Set visibility (private/public)
3. Save the configuration.

### ✅ API Keys & Access
- **Write API Key** → For sending data
- **Read API Key** → For fetching data
- Configure channel sharing if needed

### ✅ MQTT Setup
- Configure MQTT settings for real-time data streaming
- Set up secure device credentials

### ✅ ThingHTTP Integration
- Configure **ThingHTTP** for external API integration
- Set up webhooks for notifications & alerts

---
![image](https://github.com/user-attachments/assets/828f0f56-9cfb-4699-a0d6-0b807ad27c12)

## 📊 4. Sensor Dataset & Data Upload
A dataset simulating 24-hour sensor readings is created with the following:

- **Soil Moisture (%)**
- **Temperature (°C)**
- **Humidity (%)**
- **Light Intensity (lux)**
- **Soil pH**
- **Rainfall (mm)**
- **Battery Level (%)**
- **Wind Speed (km/hr)**

### 🔹 **Dataset Preparation:**
1. Create a CSV file with headers matching ThingSpeak field names.
2. Generate realistic values for a 24-hour cycle.
3. Add timestamps.
4. Upload to ThingSpeak via API or bulk import.

---
## 📈 5. Dashboard & Data Visualization
The **ThingSpeak Dashboard** provides real-time visualization with:

![image](https://github.com/user-attachments/assets/c4823964-53ea-43da-a312-762058c896a0)

### 🌿 **Soil Moisture & Rainfall Graph**
📊 Line chart for soil moisture + 📊 Bar overlay for rainfall
📏 Threshold line for optimal moisture levels

### 🌡 **Temperature & Humidity Gauges**
🎛 Current temperature & humidity display with historical trends

### 🧪 **Soil Health Panel**
📏 pH level indicator + 💧 Soil moisture adequacy + 📊 Nutrient estimation

### 🌎 **Environmental Conditions**
☀️ Light intensity trends + 🌤 Weather conditions summary

### 🔋 **System Status**
⚡ Battery levels + 🕒 Last data update timestamps

### 🚨 **Alert System**
✅ Drought, frost, heavy rainfall, and soil pH alerts

🔹 **Color-coded visualization for quick decision-making!** 🎯

---
## 📌 Conclusion
The Smart Agriculture IoT system integrates **ThingSpeak** for real-time monitoring, analytics, and automation. With cloud connectivity and a well-structured dashboard, farmers can make informed decisions for efficient farming. 🚜🌾

📌 **Next Steps:**
- Integrate AI/ML for predictive insights.
- Automate irrigation and fertilizer control.
- Expand sensor network coverage.

---
💡 *Contributors: Manoj Jivanagi