import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()

exchange_name = "topic_logs"

channel.exchange_declare(exchange=exchange_name, exchange_type="topic")

result = channel.queue_declare(queue="", exclusive=True)
queue_name = result.method.queue

binding_keys = sys.argv[1:]

if not binding_keys:
    sys.stderr.write(f"Usage: {sys.argv[0]} ...\n")
    sys.exit(1)

print(f"{binding_keys=}")

for binding_key in binding_keys:
    channel.queue_bind(
        exchange=exchange_name, queue=queue_name, routing_key=binding_key
    )

print(" [*] Waiting for logs. To exit press CTRL+C")


def callback(ch, method, properties, body):
    print(f" [x] {method.routing_key=}:{body}")


channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
channel.start_consuming()
