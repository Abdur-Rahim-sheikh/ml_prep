import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()

exchange_name = "topic_logs"

channel.exchange_declare(exchange=exchange_name, exchange_type="topic")
routing_key = sys.argv[1] if len(sys.argv) > 1 else "anonymous.info"
message = " ".join(sys.argv[2:]) or "Hello World!"
channel.basic_publish(exchange=exchange_name, routing_key=routing_key, body=message)

print(f" [x] Sent {routing_key}:{message}")
connection.close()
