import requests
import csv
import time

# ThingSpeak channel information
channel_id = "YOUR_CHANNEL_ID"
write_api_key = "YOUR_WRITE_API_KEY"
base_url = f"https://api.thingspeak.com/channels/{channel_id}/bulk_update.json"

# Read CSV data
data_points = []
with open('smart_agriculture_data.csv', 'r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        data_point = {
            'created_at': row['timestamp'],
            'field1': row['field1'],
            'field2': row['field2'],
            'field3': row['field3'],
            'field4': row['field4'],
            'field5': row['field5'],
            'field6': row['field6'],
            'field7': row['field7'],
            'field8': row['field8']
        }
        data_points.append(data_point)

# Prepare payload
payload = {
    'write_api_key': write_api_key,
    'updates': data_points
}

# Upload data to ThingSpeak
response = requests.post(base_url, json=payload)
print(f"Response status code: {response.status_code}")
print(f"Response body: {response.text}")