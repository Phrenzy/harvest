from datetime import datetime
import config as config

def write_to_outside(celsius, humid, pressure):
    rightnow = datetime.now()
    timestamp = int(datetime.timestamp(rightnow))
    year = rightnow.year
    month = rightnow.month
    day = rightnow.day
    hour = rightnow.hour
    minute = rightnow.minute
    conn = config.conn
    sql_insert_query = """INSERT INTO outside (pk, year, month, day, hour, minute, celsius, humid, pressure)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
    data_tuple = (timestamp, year, month, day, hour, minute, celsius, humid, pressure)
    c = conn.cursor()
    c.execute(sql_insert_query, data_tuple)
    conn.commit()
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
    #conn.close()

