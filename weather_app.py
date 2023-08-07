import requests

def get_weather_data(api_key, location):
    base_url = "http://api.weatherapi.com/v1/current.json"
    params = {
        "key": api_key,
        "q": location,
    }

    try:
        response = requests.get(base_url, params=params)
        response_data = response.json()

        if "error" in response_data:
            print("Error:", response_data["error"]["message"])
        else:
            location_name = response_data["location"]["name"]
            temperature_c = response_data["current"]["temp_c"]
            condition = response_data["current"]["condition"]["text"]
            humidity = response_data["current"]["humidity"]
            wind_kph = response_data["current"]["wind_kph"]

            print(f"Weather data for {location_name}:")
            print(f"Temperature: {temperature_c}°C")
            print(f"Condition: {condition}")
            print(f"Humidity: {humidity}%")
            print(f"Wind Speed: {wind_kph} kph")
    except requests.exceptions.RequestException as e:
        print("Error making the request:", e)

if __name__ == "__main__":
    api_key = "c0932fe916034ecb828140024230708"
    location = input("Enter the location (city or city,country): ")
    get_weather_data(api_key, location)