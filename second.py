import mysql.connector
from datetime import datetime



def write_to_living_room(celsius, humid):
    rightnow = datetime.now()
    timestamp = int(datetime.timestamp(rightnow))
    year = rightnow.year
    month = rightnow.month
    day = rightnow.day
    hour = rightnow.hour
    minute = rightnow.minute
    conn = sqlite3.connect('enviro.db')
    c = conn.cursor()
    c.execute("INSERT INTO living_room VALUES (?,?,?,?,?,?,?,?)",
              (timestamp, year, month, day, hour, minute, celsius, humid))
    conn.commit()
    conn.close()










conn = mysql.connector.connect(user='fprefect', password='N3CxVYZj%FKJ6*',
                              host='dbtest.phrenzy.xyz',
                              database='enviro')

rightnow = datetime.now()
timestamp = int(datetime.timestamp(rightnow))
print(timestamp)
c = conn.cursor()


mySql_insert_query = """INSERT INTO test (one, two) 
                        VALUES (%s, %s) """

testtuple = (timestamp, 7)
c.execute(mySql_insert_query, testtuple)


conn.commit()
conn.close()
