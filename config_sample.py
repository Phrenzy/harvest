# MQTT config
mqtt_broker = "mybrokerserver.com"

sensors = ["outside/celsius", "outside/humid", "outside/pressure"]

# database
conn = mysql.connector.connect(user='username', password='password', host='database.hostname', database='enviro')