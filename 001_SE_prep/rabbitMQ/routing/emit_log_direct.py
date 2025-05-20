import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()

exchange_name = "direct_logs"
channel.exchange_declare(exchange=exchange_name, exchange_type="direct")
severity = sys.argv[1] if len(sys.argv) > 1 else "info"
message = " ".join(sys.argv[2:]) or "Hello world"

channel.basic_publish(exchange=exchange_name, routing_key=severity, body=message)
print(f" [x] Sent {severity=}: '{message=}'")

connection.close()
