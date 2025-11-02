import requests


def get_weather(city_name, api_key):
    url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city_name,
        "appid": api_key
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()

        description = data["weather"][0]["description"]
        temp_kelvin = data["main"]["temp"]
        temp_celsius = temp_kelvin - 273.15

        return description, temp_celsius

    except requests.exceptions.RequestException as e:
        return None, f"Error fetching weather data: {e}"
    except KeyError:
        return None, "City not found or invalid response from API."


if __name__ == "__main__":
    api_key = input("Enter your OpenWeather API key: ").strip()
    city_name = input("Enter city name: ").strip()

    description, temp = get_weather(city_name, api_key)

    if description:
        print(f"Weather in {city_name}: {description}, Temperature: {temp:.1f}°C")
    else:
        print(temp)
