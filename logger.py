from datetime import datetime
import json
import os

# Logging the request info
def reqLog(path, method):
   today = str(datetime.now())
   logItem = f'{today}\t{method}\t{path}'

   
   with open ('/home/IPAPP/logs/logRequest.log', 'a+') as writeLog:
      writeLog.write(logItem+"\n")

# Logging the data info into backlogs.json
def backLogs(data,path,method):
   
   with open ('/home/IPAPP/logs/backlog.json', 'r') as jsonLog:
      backlog = json.loads(jsonLog.readline())
   
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
      
      with open ('/home/IPAPP/logs/backlog.json', 'w') as writeBackLog:
         writeBackLog.write(json.dumps(backlog))

      