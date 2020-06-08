import paho.mqtt.client as mqtt
import time
import config as config
import re
from dbconnect import write_to_outside


# def on_log(client, userdata, level, buf):
# print('log: '+buf)


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        # print('connected OK')
        print()
    else:
        print("Bad connection, Returned code= ", rc)


def on_disconnect(client, userdata, flags, rc=0):
    print('Disconnected with code ' + str(rc))


def on_message(client, userdata, msg):
    # gather data from MQTT, remove unwanted data, convert from list to string
    collect_data = re.findall('[0-9.]{1,}', str(msg.payload))
    # convert collected data from string to rounded integer
    sensor_data = round(float(''.join(collect_data)))
    print(sensor_data)
    sensor_results[key] = sensor_data


sensors = config.sensors
broker = config.mqtt_broker
sensor_results = {}


client = mqtt.Client()

client.on_message = on_message
client.connect(broker)
client.loop_start()

for key in sensors:
    print(key)
    client.subscribe(sensors[key])
    time.sleep(.5)


client.loop_stop()
client.disconnect()

print(sensor_results)

celsius = int(10)
humid = int(55)
pressure = int(1234)

#write_to_outside(celsius, humid, pressure)

