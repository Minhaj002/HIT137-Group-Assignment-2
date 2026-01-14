import math

#Function for Temperature Stability 
def temp_stability(data):
    # Find the most steady and most shaky station temps
    def get_score(nums):
        mid = sum(nums) / len(nums)
        diff = sum((x - mid) ** 2 for x in nums)
        return math.sqrt(diff / len(nums))

    low_score, high_score = None, None
    steady, shaky = [], []

    for place, temps in data.items():
        if not temps: continue
        score = get_score(temps)

        if low_score is None or score < low_score:
            low_score = score
            steady = [(place, score)]
        elif score == low_score:
            steady.append((place, score))

        if high_score is None or score > high_score:
            high_score = score
            shaky = [(place, score)]
        elif score == high_score:
            shaky.append((place, score))

    with open("temperature_stability_stations.txt", "w") as f:
        for place, score in steady:
            f.write(f"Most Stable: Station {place}: StdDev {score:.1f}°C\n")
        for place, score in shaky:
            f.write(f"Most Variable: Station {place}: StdDev {score:.1f}°C\n")