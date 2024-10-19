
# import paho.mqtt.client as mqtt

# # MQTT setup
# MQTT_BROKER = "your_mqtt_broker_address"
# MQTT_PORT = 1883
# MQTT_TOPIC = "#"

# client = mqtt.Client()
# client.connect(MQTT_BROKER, MQTT_PORT, 60)

import json
import time

import mysql.connector
from django.db import connections
from django.db.utils import ProgrammingError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def check_db(self):
        try:
            conn = mysql.connector.connect(
                host='127.0.0.1',
                user='root',
                password='123456',
                database='db_xeye',
                port='3306'
            )
            print("Connected successfully to external database.")
            conn.close()

        except mysql.connector.Error as err:
            print("Error connecting to external database:", err)
            exit(1)

    def handle(self, *args, **kwargs):
        def Process(new_entries):
            if new_entries:
                for entry in new_entries:
                    # Construct the MQTT message
                    mqtt_message = {
                        "table": entry[1],
                        "data": json.loads(entry[2]),
                        "timestamp": str(entry[3])
                    }

                    print(mqtt_message)
                    # client.publish(MQTT_TOPIC, json.dumps(mqtt_message))

                    cursor.execute(f"UPDATE audit_log SET processed = TRUE WHERE id = {entry[0]}")
                    external_conn.commit()  # Commit the changes


        self.check_db()
        external_conn = connections['external_table']

        with external_conn.cursor() as cursor:
            # query = "SELECT * FROM audit_log WHERE inserted_at > NOW() - INTERVAL 1 MINUTE"
            query = "SELECT * FROM audit_log WHERE processed = FALSE"

            while True:
                try:
                    cursor.execute(query)
                except ProgrammingError as error: 
                    print(f"Error: {error} - Attempting to Try in 10 sec.")
                    time.sleep(10)
                    continue

                new_entries = cursor.fetchall()
                Process(new_entries)
                
                # Sleep for a short period before checking again (adjust as needed)
                time.sleep(1)
