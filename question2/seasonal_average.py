# Function for Seasonal Averages
def temp_average(data):
    # Figure out the average for each season
    with open("average_temp.txt", "w") as f:
        for s, temps in data.items():
            if temps:
                avg = sum(temps) / len(temps)
                f.write(f"{s}: {avg:.1f}°C\n")
