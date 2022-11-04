from flask import Flask, make_response, jsonify, request, render_template, send_from_directory
import requests
from logger import reqLog, backLogs
import json
from flask_cors import CORS
import os

# PORT for the server to listen. Use env PORT if available else 5500
PORT = 3000

# Items to get
filterItems = [
   "ip",
   "network",
   "version",
   "asn",
   "postal",
   "latitude",
   "longitude",
   "country_code",
]

# Instantiate Flask app
app = Flask(__name__)
CORS(app)

@app.route('/', methods=["GET"])
def home():
   return render_template('index.html')

@app.route('/<path:path>', methods=["GET"])
def serverFiles(path):
   return send_from_directory('templates', path)

# Get Current IP Information Route
@app.route('/ip/info', methods=["POST"])
def getMyIP():
   reqLog(request.path, request.method)
   
   my_json = request.data.decode('utf8').replace("'", '"')
   data = json.loads(my_json)
   # s = json.dumps(data, indent=4, sort_keys=True)
   myIP = data['data']
   

   # Fetch data from ipapi.co REST API
   data = requests.post(f'https://ipapi.co/{myIP}/json/')
   myInfo = data.json()
   
   if(data.status_code == 429): return make_response(myInfo, data.status_code)
   if(data.status_code >= 400): return make_response(myInfo, data.status_code)

   # Filter fetched data using filterItems
   filteredIpInfo = {}
   for key in myInfo:
      if(key in filterItems):
         filteredIpInfo.update({key: myInfo[key]})

   # Response
   backLogs(filteredIpInfo, request.path, request.method)
   res = make_response(filteredIpInfo, 200)
   
   return res

# Get Backlog Items Route
@app.route('/ip/backlog', methods=["GET"])
def printBackLog():
   reqLog(request.path, request.method)
   # Update Backlog
   with open ('/home/IPAPP/logs/backlog.json', 'r') as jsonLog:
      backlog = json.loads(jsonLog.readline())
   
   for i,log in enumerate(backlog):
      print(f'LOG ITEM {i}')
      for key in log:
         print(f'{key}: {log[key]}')
      print('\n')   
   
   # Response
   return make_response(jsonify(backlog), 200)


if __name__ == "__main__":
   app.run(host="0.0.0.0", port=PORT)