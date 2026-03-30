import urllib.request
import json
import random

LOCATIONS = [
    ("San Jose", 37.3382, -121.8863),
    ("Santa Clara", 37.3541, -121.9552),
    ("Sunnyvale", 37.3688, -122.0363),
    ("Mountain View", 37.3861, -122.0839),
    ("Palo Alto", 37.4419, -122.1430),
    ("Menlo Park", 37.4530, -122.1817),
    ("Redwood City", 37.4852, -122.2364),
    ("San Mateo", 37.5630, -122.3255),
    ("South San Francisco", 37.6547, -122.4077),
    ("San Francisco", 37.7749, -122.4194),
]


def get_weather(location_index=0):
    try:
        _, lat, lon = LOCATIONS[location_index]
        url = (
            f"https://api.open-meteo.com/v1/forecast"
            f"?latitude={lat}&longitude={lon}"
            f"&current_weather=true"
        )
        with urllib.request.urlopen(url, timeout=3) as response:
            data = json.loads(response.read())
            code = data["current_weather"]["weathercode"]
            temp = data["current_weather"]["temperature"]

        if code == 0:
            condition = "sunny"
        elif code in [1, 2, 3]:
            condition = "cloudy"
        elif code in [51, 53, 55, 61, 63, 65, 80, 81, 82]:
            condition = "rain"
        elif code in [71, 73, 75]:
            condition = "cold"
        elif code in [95, 96, 99]:
            condition = "storm"
        elif code in [45, 48]:
            condition = "fog"
        elif temp > 30:
            condition = "heat"
        else:
            condition = "cloudy"

        return condition, temp, LOCATIONS[location_index][0]

    except Exception:
        fallback = random.choice(["sunny", "cloudy", "rain", "cold", "heat", "storm", "fog"])
        return fallback, None, None
