import sqlite3
from datetime import datetime


def write_to_outside(celsius, humid, pressure):
    rightnow = datetime.now()
    timestamp = int(datetime.timestamp(rightnow))
    year = rightnow.year
    month = rightnow.month
    day = rightnow.day
    hour = rightnow.hour
    minute = rightnow.minute
    conn = sqlite3.connect('enviro.db')
    c = conn.cursor()
    c.execute("INSERT INTO outside VALUES (?,?,?,?,?,?,?,?,?)",
              (timestamp, year, month, day, hour, minute, celsius, humid, pressure))
    conn.commit()
    conn.close()
