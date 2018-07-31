from iothub_client import IoTHubClient, IoTHubTransportProvider, IoTHubMessage

CONNECTION_STRING = "HostName=rpi-device-data.azure-devices.net;DeviceId=rpi;SharedAccessKey=ck5epWgCcCywkYTiXonVxiXV4I/WOtc7No5n+0+6wLA="
PROTOCOL = IoTHubTransportProvider.MQTT

def connectIoTHub():
    client = IoTHubClient(CONNECTION_STRING, PROTOCOL)
    return client

# Gets the Raspberry Pi 3 Model B's serial number
def getId():
	iD = "0000000000000000"
	try:
		f = open('/proc/cpuinfo','r')
		for line in f:
			if line[0:6]=='Serial':
				iD = line[10:26]
		f.close()
	except:
		iD = "ERROR00000000000"
		f.close()
	return iD