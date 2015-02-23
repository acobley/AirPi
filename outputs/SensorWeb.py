import output
import datetime
import json

class SensorWeb(output.Output):
	requiredData = ["Device"]
	optionalData = []
	def __init__(self,data):
		self.Device=data["Device"]
	def outputData(self,dataPoints):
		arr = []
		arr.append({"Device":self.Device}) 
		for i in dataPoints:
			arr.append({"id":i["name"],"current_value":i["value"]})
		a = json.dumps({"Device":self.Device,"insertion_time":str(datetime.datetime.now(),"version":"1.0.0","datastreams":arr})
	
		print ""
		print "Time: " + str(datetime.datetime.now())
		for i in dataPoints:
			print "Sensor "+i["name"] + ": " + str(i["value"]) + " " + i["symbol"]
		print "Json "+a
		return True
