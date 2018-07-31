#!/usr/bin/env python

# Simple temperature/humidity module.
# Will print temperature, humidity and other details.
# Will send each message to Microsoft Azure ServiceBus in JSON format
import sys, datetime, json
import Adafruit_DHT

from utility import *

# Create Service Bus object
client = connectIoTHub()

# Create ID for Raspberry Pi
iD = getId()

# Get DHT11 sensor data, convert into JSON, and send data to ServiceBus
while True:	
	# Get Timestamp
	dt = str(datetime.datetime.now())

	# Get DHT Sensor data on from GPIO4
	humid, temp = Adafruit_DHT.read_retry(11, 4)

	# Convert C to F
	# f = t * 9. / 5. + 32 # from C to F

	# Create JSON message
	data = {
	'DeviceID': iD,
	'Time': dt,
	'Temperature': temp,
	'Humidity': humid
	}
	msg = json.dumps(data)

	# Print JSON message for testing purposes
	print(msg)
    
    iot_msg = IoTHubMessage(msg)

	# Send msg to ServiceBus using Queue name
	client.send_event_async(iot_msg)

    print("Message sent to IoT Hub")
