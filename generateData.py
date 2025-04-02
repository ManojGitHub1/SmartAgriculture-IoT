import pandas as pd
import numpy as np
import datetime

# Generate 7 days of data with hourly readings
start_date = datetime.datetime(2025, 3, 30)
hours = 24 * 7  # 7 days
data = []

# Base values
soil_moisture = 45
temperature = 20
humidity = 65
light = 0
pH = 6.8
rainfall = 0
battery = 100
wind = 5

for hour in range(hours):
    current_time = start_date + datetime.timedelta(hours=hour)
    
    # Time of day factor (0 to 1, peaks at noon)
    hour_of_day = current_time.hour
    day_factor = -np.cos(hour_of_day/24 * 2 * np.pi)
    
    # Daily variations
    temp_variation = 10 * day_factor
    humidity_variation = -15 * day_factor
    light_variation = max(0, 1500 * day_factor)
    
    # Random variations
    temp_random = np.random.normal(0, 1)
    humidity_random = np.random.normal(0, 2)
    moisture_random = np.random.normal(0, 1)
    
    # Calculate values
    curr_temp = temperature + temp_variation + temp_random
    curr_humidity = humidity + humidity_variation + humidity_random
    curr_light = max(0, light_variation + np.random.normal(0, 50))
    
    # Soil moisture decreases during hot day, increases after rain
    moisture_change = -0.2 * day_factor + moisture_random
    soil_moisture = max(25, min(60, soil_moisture + moisture_change))
    
    # Occasional rainfall (5% chance during daytime)
    curr_rainfall = 0
    if 10 <= hour_of_day <= 16 and np.random.random() < 0.05:
        curr_rainfall = np.random.exponential(3)
        # Soil moisture increases after rain
        soil_moisture = min(60, soil_moisture + curr_rainfall * 0.5)
    
    # Battery decreases slightly each day, recharges with sunlight
    battery = max(80, min(100, battery - 0.02 + curr_light/10000))
    
    # Wind varies throughout the day
    curr_wind = wind + 5 * day_factor + np.random.normal(0, 2)
    curr_wind = max(0, curr_wind)
    
    # pH varies slightly
    curr_pH = pH + np.random.normal(0, 0.05)
    
    data.append({
        'timestamp': current_time.strftime('%Y-%m-%d %H:%M:%S'),
        'field1': round(soil_moisture, 1),
        'field2': round(curr_temp, 1),
        'field3': round(curr_humidity, 1),
        'field4': round(curr_light, 0),
        'field5': round(curr_pH, 1),
        'field6': round(curr_rainfall, 1),
        'field7': round(battery, 0),
        'field8': round(curr_wind, 1)
    })

# Create DataFrame and save to CSV
df = pd.DataFrame(data)
df.to_csv('smart_agriculture_extended_data.csv', index=False)
print("Extended dataset created!")