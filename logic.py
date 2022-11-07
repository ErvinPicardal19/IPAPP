from flask_restful import Api, Resource
from flask import request, make_response, jsonify
import requests
import json
from logger import backLogs, reqLog

class getMyIP(Resource):
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
   
   def post(self):
      reqLog(request.path, request.method)

      myIP = request.get_json()["data"]
      # print(myIP)
      # Fetch data from ipapi.co REST API
      data = requests.post(f'https://ipapi.co/{myIP}/json/')
      myInfo = data.json()
      
      if(data.status_code >= 300): return make_response(myInfo, data.status_code)

      # Filter fetched data using filterItems
      filteredIpInfo = {}
      for key in myInfo:
         if(key in self.filterItems):
            filteredIpInfo.update({key: myInfo[key]})

      # Response
      backLogs(filteredIpInfo, request.path, request.method)
      res = make_response(filteredIpInfo, 200)
      
      return res
   
class printBackLog(Resource):
   def get(self):
      reqLog(request.path, request.method)
      # Update Backlog
      backlog=[]  
      with open ('/home/IPAPP/logs/backlog.json', 'r') as jsonLog:
         backlog = json.loads(jsonLog.readline())
      
      # Response
      return make_response(jsonify(backlog), 200)