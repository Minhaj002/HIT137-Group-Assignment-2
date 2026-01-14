"""
Group Name: DAN/EXT 03
Group Members:
MINHAJ ABDUL KHALEQ - 396076
NIMETH DULSITH KODAGODA DISSANAYAKE LIYANAGE - 397445
PRASHANNA RATNA BAJRACHARYA - 398024
SUGAM KAFLE - 398343
"""
import os
import csv
# Import the functions from the other files
from seasonal_average import temp_average
from temperature_range import temp_range
from temperature_stability import temp_stability

# folder name containing the CSV files
folder = "temperatures"

# Lists to hold the temps for each season
season_data = {
    "Summer": [],
    "Autumn": [],
    "Winter": [],
    "Spring": []
}

# Dictionary to hold temps for each station
station_data = {}

# Match months to seasons
season_map = {
    "January": "Summer", "February": "Summer", "March": "Autumn",
    "April": "Autumn", "May": "Autumn", "June": "Winter",
    "July": "Winter", "August": "Winter", "September": "Spring",
    "October": "Spring", "November": "Spring", "December": "Summer"
}

months = list(season_map.keys())

# loop to read all the files in the folder
if os.path.exists(folder):
    for name in os.listdir(folder):
        if name.endswith(".csv"):
            path = os.path.join(folder, name)

            with open(path, "r") as f:
                reader = csv.DictReader(f)

                for row in reader:
                    place = row["STATION_NAME"]

                    if place not in station_data:
                        station_data[place] = []

                    for m in months:
                        val = row[m]
                        
                        # Skip if there's no value
                        if val == "" or val.lower() == "nan":
                            continue

                        num = float(val)

                        # Add to the right season
                        s = season_map[m]
                        season_data[s].append(num)

                        # Add to the right station
                        station_data[place].append(num)

# Calling the functions 
temp_average(season_data)
temp_range(station_data)
temp_stability(station_data)

print("Program Executed. Check output files for results.")