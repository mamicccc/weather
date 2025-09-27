import requests

API_KEY = "YOUR_API_KEY"  # OpenWeather API key buraya
city = input("Enter a city: ")

url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
response = requests.get(url).json()

if response["cod"] == 200:
    print(f"Weather in {city}: {response['weather'][0]['description']}")
    print(f"Temperature: {response['main']['temp']}°C")
else:
    print("City not found!")
