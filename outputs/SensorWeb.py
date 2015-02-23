import output
import datetime
import json
import socket

class SensorWeb(output.Output):
	requiredData = ["Device"]
	optionalData = []
	def __init__(self,data):
		self.Device=data["Device"]
	def outputData(self,dataPoints):
		arr = []
		for i in dataPoints:
			arr.append({"name":i["name"],"fValue":i["value"]})
		a = json.dumps({"SensorData":{"device":self.Device,"insertion_time":str(datetime.datetime.now())},"version":"1.0.0","sensors":arr})
	
		print ""
		print "Time: " + str(datetime.datetime.now())
		for i in dataPoints:
			print "Sensor "+i["name"] + ": " + str(i["value"]) + " " + i["symbol"]
		print "Json "+a
		clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		clientsocket.connect(('r2proaa2.miniserver.com', 19877))
		clientsocket.send(a)
		return True
