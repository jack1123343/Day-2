#https://newsdata.io/api/1/news?apikey=pub_544209fb7e00f06ea6ca6907d51e7c8a8bcb7&q=Technology
import requests

def get_news(Title) :
    url = f"https://newsdata.io/api/1/news?apikey=pub_544209fb7e00f06ea6ca6907d51e7c8a8bcb7&q={Title}"
    request = requests.get(url)
    content = request.json()
    print(content)

get_news("Technology")
