import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()
queue_name = "task_queue"
channel.queue_declare(queue=queue_name, durable=True)
message = " ".join(sys.argv[1:]) or "Hello World!"

channel.basic_publish(
    exchange="",
    routing_key=queue_name,
    body=message,
    properties=pika.BasicProperties(delivery_mode=pika.DeliveryMode.Persistent),
)
print(" [x] Sent 'Hello World!'")

connection.close()
