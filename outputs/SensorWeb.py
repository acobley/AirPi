import output
import datetime
import json

class Print(output.Output):
	requiredData = []
	optionalData = []
	def __init__(self,data):
		pass
	def outputData(self,dataPoints):
		arr = []
		for i in dataPoints:
			arr.append({"id":i["name"],"current_value":i["value"]})
		a = json.dumps({"version":"1.0.0","datastreams":arr})
	
		print ""
		print "Time: " + str(datetime.datetime.now())
		for i in dataPoints:
			print "Sensor "+i["name"] + ": " + str(i["value"]) + " " + i["symbol"]
		print "Json "+a
		return True
