from datetime import datetime
import json

# Logging the request info
def reqLog(path, method):
   today = str(datetime.now())
   logItem = f'{today}\t{method}\t{path}'
   try:
      with open ('./logs/logRequest.log', 'a+') as writeLog:
         writeLog.write(logItem+"\n")
   except:
      print("Cannot write to file logRequest.log")

# Logging the data info into backlogs.json
def backLogs(data,path,method):
   backlog=[]
   try:
      with open ('./logs/backlog.json', 'r') as jsonLog:
         backlog = json.loads(jsonLog.readline())
   except:
         print("Cannot read file backlog.json")
   
   today = str(datetime.now())
   
   metadata = {
      "timestamp": today,
      "path": path,
      "method": method, 
   }
   
   newBackLog = {
      "meta": metadata,
      "body": data
   }
   
   backlog.append(newBackLog)
   
   try:
      with open ('./logs/backlog.json', 'w') as writeBackLog:
         writeBackLog.write(json.dumps(backlog))
   except:
      print("Cannot write to file backlog.json")