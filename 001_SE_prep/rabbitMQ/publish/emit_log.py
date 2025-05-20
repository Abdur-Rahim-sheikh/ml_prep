import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()

exchange_name = "logs"
channel.exchange_declare(exchange=exchange_name, exchange_type="fanout")

message = " ".join(sys.argv[1:]) or "Hello World!"

channel.basic_publish(exchange=exchange_name, routing_key="", body=message)
print(" [x] Sent 'Hello World!'")

connection.close()
