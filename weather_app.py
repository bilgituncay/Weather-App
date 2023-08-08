import requests

def get_weather_data(api_key, location, forecast=False, days = 1):
    base_url = "http://api.weatherapi.com/v1/"
    endpoint = 'forecast.json' if forecast else 'current.json'
    params = {
        'key': api_key,
        'q': location,
        'days': days if forecast else None
        }

    try:
        response = requests.get(base_url + endpoint, params=params)
        response_data = response.json()
        
        
        if "error" in response_data:
            print("Error:", response_data['error']['message'])
        else:
            location_name = response_data['location']['name']

            if forecast:
                forecast_days = response_data['forecast']['forecastday']
                print(f"Forecast for {location_name}:")
                for day in forecast_days:
                    date = day['date']
                    condition = day["day"]["condition"]["text"]
                    max_temp_c = day["day"]["maxtemp_c"]
                    min_temp_c = day["day"]["mintemp_c"]
            
                    print(f"Date: {date}")
                    print(f"Condition: {condition}")
                    print(f"Max Temperature: {max_temp_c}°C")
                    print(f"Min Temperature: {min_temp_c}°C")
                    print("=" * 20)

            else:
                temperature_c = response_data['current']['temp_c']
                condition = response_data['current']['condition']['text']
                humidity = response_data["current"]["humidity"]
                wind_kph = response_data["current"]["wind_kph"]

                print(f"Weather data for {location_name}:")
                print(f"Temperature: {temperature_c}°C")
                print(f"Condition: {condition}")
                print(f"Humidity: {humidity}%")
                print(f"Wind Speed: {wind_kph} kph")

    except requests.exceptions.RequestException as e:
        print("Error making the request:", e)

if __name__ == '__main__':
    api_key = 'c0932fe916034ecb828140024230708'
    location = input("Enter the location (city or city, country): ")
    choice = input("Current or forecast?")

    if choice.lower() == "current":
        get_weather_data(api_key, location)
    elif choice.lower() == "forecast":
        num_days = int(input("Enter the amount of forecast days: "))
        get_weather_data(api_key, location, forecast=True, days = num_days)
    else:
        print("Invalid choice. Please choose either 'current' or 'forecast'.")
