import paho.mqtt.client as mqtt
import time
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
    print(msg.topic + " " + str(msg.payload))


broker = "axis.phrenzy.xyz"

client = mqtt.Client()

client.on_connect = on_connect
client.on_disconnect = on_disconnect
# client.on_log=on_log
client.on_message = on_message

# print("connecting to broker, ", broker)
client.connect(broker)
client.loop_start()
client.subscribe("outside/#")
client.subscribe("shellies/living/temp/01/sensor/humidity")
client.subscribe("shellies/living/temp/01/sensor/temperature")

time.sleep(.5)
client.loop_stop()
client.disconnect()

celsius = int(10)
humid = int(55)
pressure = int(1234)

write_to_outside(celsius, humid, pressure)
