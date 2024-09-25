import requests

def get_weather(city, api_key, units) :
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units={units}"
    request = requests.get(url)
    content = request.json()
    print(content)

get_weather("Kannur", "f2539ef462470ee6cf947c339bab0905", 'Standard')