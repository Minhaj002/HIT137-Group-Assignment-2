# Function for Temperature Range
def temp_range(data):
    # Find which station has the biggest difference between high and low
    big_gap = 0
    diff_list = []

    for place, temps in data.items():
        if not temps: continue
        
        high, low = max(temps), min(temps)
        gap = high - low

        if gap > big_gap:
            big_gap = gap
            diff_list = [(place, high, low)]
        elif gap == big_gap:
            diff_list.append((place, high, low))

    with open("largest_temp_range_station.txt", "w") as f:
        for place, hi, lo in diff_list:
            f.write(f"Station {place}: Range {big_gap:.1f}°C (Max: {hi:.1f}°C, Min: {lo:.1f}°C)\n")