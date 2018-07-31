import gps, time, json

from utility import *

# Create Service Bus object
client = connectIoTHub()

# Create ID for Raspberry Pi
iD = getId()

# Listen on port 2947 (gpsd) of localhost
session = gps.gps("localhost", "2947")
session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)

while True:
    try:
        report = session.next()
        # Wait for TPV (Time Position Velocity) Report
        # and save data
        if report['class'] == 'TPV':
            lat = report.lat
            lon = report.lon
            speed = report.speed
            dt = report.time

            # Create JSON message
            data = {
                'Device ID' : iD,
                'Time': time,
                'Latitude': lat,
                'Longitude': lon,
                'Speed': speed,
            }
            msg = json.dumps(data)

            # Print JSON Message for testing purposes
            print(msg)

            # Create IoT Hub Message
            iot_msg = IoTHubMessage(msg)

            # Send iot_msg to IoT Hub
            client.send_event_async(iot_msg)

            print("Message sent to IoT Hub")



