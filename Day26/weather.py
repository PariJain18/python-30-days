import requests

city = input("Enter city name: ")

try:
    # Find city location
    url = "https://geocoding-api.open-meteo.com/v1/search"

    response = requests.get(
        url,
        params={"name": city, "count": 1},
        timeout=10
    )
    response.raise_for_status()

    data = response.json()

    if "results" not in data:
        print("City not found!")

    else:
        latitude = data["results"][0]["latitude"]
        longitude = data["results"][0]["longitude"]

        # Get weather
        weather_url = "https://api.open-meteo.com/v1/forecast"

        weather_response = requests.get(
            weather_url,
            params={
                "latitude": latitude,
                "longitude": longitude,
                "current": "temperature_2m,wind_speed_10m"
            },
            timeout=10
        )
        weather_response.raise_for_status()

        weather = weather_response.json()
        current = weather["current"]

        print("City:", city)
        print("Temperature:", current["temperature_2m"], "°C")
        print("Wind Speed:", current["wind_speed_10m"], "km/h")

except requests.exceptions.Timeout:
    print("Request timed out!")

except requests.exceptions.ConnectionError:
    print("Internet connection error!")

except requests.exceptions.RequestException as e:
    print("Something went wrong:", e)