from flask import Flask, request, jsonify
import requests
from flask_cors import CORS
import subprocess

app = Flask(__name__)
cors = CORS(app, resources={r'*': {'origins': '*'}})
@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
       # id = request.json['id']
        #url = f"https://vadss.vercel.app/api/savedImages?id={id}"
        #response = requests.get(url)
        #data = response.json()
        #url = data['url']
    # create the response with the Access-Control-Allow-Origin header
        url = request.json['url']
        weights_path = 'best.pt'
        subprocess.run(['python', 'detect.py', '--source', url, '--weights', weights_path])
        resp = jsonify({'url': url})
        resp.headers.add('Access-Control-Allow-Origin', '*')
        return resp
    else:
        return "YOLOv5 Model APP"