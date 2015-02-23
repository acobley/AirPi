import output
import datetime
import json
import socket

class SensorWeb(output.Output):
	requiredData = ["Device","Host"]
	optionalData = ["Lat","Lng","Town","Name"]
	def __init__(self,data):
		self.Device=data["Device"]
		self.Host=data["Host"]
		meta=[]
		if "Lat" in data.keys():
		   meta.append({"Lat":data["Lat"]})
		meta.append({"Lng":data["Lng"]})
		meta.append({"Town":data["Town"]})
		meta.append({"Name":data["Name"]})
	def outputData(self,dataPoints):
		arr = []
		for i in dataPoints:
			arr.append({"name":i["name"],"fValue":i["value"]})
		a = json.dumps({"SensorData":{"device":self.Device,"insertion_time":str(datetime.datetime.now())},"version":"1.0.0","meta":meta,"sensors":arr})
	
		print ""
		print "Time: " + str(datetime.datetime.now())
		for i in dataPoints:
			print "Sensor "+i["name"] + ": " + str(i["value"]) + " " + i["symbol"]
		print "Json "+a
		clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		clientsocket.connect((self.Host, 19877))
		clientsocket.send(a)
		return True
