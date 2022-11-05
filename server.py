from flask import Flask, render_template, send_from_directory
from flask_restful import Api
from logic import getMyIP, printBackLog
from flask_cors import CORS

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
api = Api(app)

api.add_resource(getMyIP, '/ip/info')
api.add_resource(printBackLog, '/ip/backlog')

@app.route('/', methods=["GET"])
def home():
   return render_template('index.html')

@app.route('/<path:path>', methods=["GET"])
def serverFiles(path):
   return send_from_directory('templates', path)


if __name__ == "__main__":
   app.run(host="0.0.0.0", port=PORT)