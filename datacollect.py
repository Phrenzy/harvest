import paho.mqtt.client as mqtt
import time
import config as config
import re
from datetime import datetime


def on_connect(rc):
    if rc == 0:
        # print('connected OK')
        print()
    else:
        print("Bad connection, Returned code= ", rc)


def on_disconnect(rc=0):
    print('Disconnected with code ' + str(rc))


def on_message(client, userdata, msg):
    # gather data from MQTT, remove unwanted data, convert from list to string
    collect_data = re.findall('[0-9.]{1,}', str(msg.payload))
    # convert collected data from string to rounded integer
    sensor_data = round(float(''.join(collect_data)))
    # print(sensor_data)
    sensor_results[key] = sensor_data


def write_to_outside(celsius, humid, pressure):
    rightnow = datetime.now()
    timestamp = int(datetime.timestamp(rightnow))
    year = rightnow.year
    month = rightnow.month
    day = rightnow.day
    hour = rightnow.hour
    minute = rightnow.minute
    connection = config.conn
    sql_insert_query = """INSERT INTO outside (pk, year, month, day, hour, minute, celsius, humid, pressure)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
    data_tuple = (timestamp, year, month, day, hour, minute, celsius, humid, pressure)
    c = connection.cursor()
    c.execute(sql_insert_query, data_tuple)
    connection.commit()


# conn.close()

def write_to_living_room(celsius, humid):
    rightnow = datetime.now()
    timestamp = int(datetime.timestamp(rightnow))
    year = rightnow.year
    month = rightnow.month
    day = rightnow.day
    hour = rightnow.hour
    minute = rightnow.minute
    conn = config.conn
    sql_insert_query = """INSERT INTO living_room (pk, year, month, day, hour, minute, celsius, humid)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
    data_tuple = (timestamp, year, month, day, hour, minute, celsius, humid)
    c = conn.cursor()
    c.execute(sql_insert_query, data_tuple)
    conn.commit()
    # conn.close()


sensors = config.sensors
broker = config.mqtt_broker
sensor_results = {}

client = mqtt.Client()
client.on_message = on_message
client.connect(broker)
client.loop_start()

# loop through sensors
for key in sensors:
    # print(key)
    client.subscribe(sensors[key])
    time.sleep(.5)

client.loop_stop()
client.disconnect()

# write results to database
write_to_outside(sensor_results['outside_celsius'], sensor_results['outside_humid'], sensor_results['outside_pressure'])
write_to_living_room(sensor_results['living_celsius'], sensor_results['living_humid'])

# close database connection
conn = config.conn
conn.close()
