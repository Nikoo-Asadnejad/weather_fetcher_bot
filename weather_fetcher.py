import requests

def get_latitude_longitude(location):
    url = f"https://nominatim.openstreetmap.org/search?format=json&q={location}"
    response = requests.get(url)
    data = response.json()

    if data:
        latitude = data[0]['lat']
        longitude = data[0]['lon']
        return latitude, longitude
    else:
        return None, None

def get_weather(latitude, longitude):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"
    response = requests.get(url)
    data = response.json()
    
    if 'current_weather' in data:
        weather = data['current_weather']
        print(f"Temperature: {weather['temperature']}°C")
        print(f"Weather State: {weather['weathercode']}")
    else:
        print("Error fetching weather data")

def main():
    location = input("Enter a location: ")
    latitude, longitude = get_latitude_longitude(location)

    if latitude is not None and longitude is not None:
        get_weather(latitude, longitude)
    else:
        print("Location not found.")

if __name__ == "__main__":
    main()