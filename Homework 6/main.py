# Name: Rakshith Jayakarthikeyan
# Assignment: PROG1003 - HW6 - How Far

import csv
import math

# calculate distance between two cities
def distance(lat1, lon1, lat2, lon2):
    R = 6371.0
    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)

    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    return R * 2 * math.asin(math.sqrt(a))

# read city data
def load(filename):
    data = []
    with open(filename, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            city = [row["City"], row["Country"], float(row["Latitude"]), float(row["Longitude"])]
            data.append(city)
    return data

# main program
def main():
    cities = load("WorldCities.csv")

    while True:
        city_name = input('Enter a city, "list" to see all, or "quit" to exit: ').strip()
        if city_name == "":
            continue
        if city_name.lower() == "quit":
            break
        if city_name.lower() == "list":
            for c in cities:
                print("   " + c[0])
            continue

        # find city index
        found = -1
        for i in range(len(cities)):
            if cities[i][0].lower() == city_name.lower():
                found = i
                break

        if found == -1:
            print("City not found. Try again.\n")
            continue

        # show distances
        print(cities[found][0], "found at index", found)
        start = cities[found]
        results = []

        for i in range(len(cities)):
            if i == found:
                continue
            end = cities[i]
            d = distance(start[2], start[3], end[2], end[3])
            results.append([d, end[0], end[1]])

        results.sort()

        for j in range(13):
            d = results[j][0]
            city = results[j][1]
            country = results[j][2]
            print("  {:3.4f} km to {}, {}".format(d, city, country))

if __name__ == "__main__":
    main()
