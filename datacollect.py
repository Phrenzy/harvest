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
    # print(msg.topic + " " + str(msg.payload))
    # find name of collected data, remove rest of topic name
    topic_name = re.findall('[a-z]{1,}$', msg.topic)
    # convert from list to sting
    print(''.join(topic_name))
    # gather data from MQTT, remove unwanted data, convert from list to string
    collect_data = re.findall('[0-9.]{1,}', str(msg.payload))
    # convert collected data from string to rounded integer
    sensor_data = round(float(''.join(collect_data)))
    print(sensor_data)
    print(i)




sensors = config.sensors
broker = config.mqtt_broker

client = mqtt.Client()

#client.on_connect = on_connect
#client.on_disconnect = on_disconnect
# client.on_log=on_log
client.on_message = on_message

# print("connecting to broker, ", broker)
client.connect(broker)
client.loop_start()
for i in sensors:
    client.subscribe(i)


time.sleep(.5)
client.loop_stop()
client.disconnect()

celsius = int(10)
humid = int(55)
pressure = int(1234)

#write_to_outside(celsius, humid, pressure)

