from flask import Flask, jsonify
import requests

topic = 'Github'

r = requests.get(f'https://newsdata.io/api/1/news?apikey=pub_544209fb7e00f06ea6ca6907d51e7c8a8bcb7&q={topic}')
app = Flask(__name__)
@app.route('/')
def get_api() :
    response = {'response': r.json()}
    return jsonify(response)

app.run(port = 5000)