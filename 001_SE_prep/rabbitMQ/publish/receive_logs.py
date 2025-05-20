import pika

exchange_name = "logs"

connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
channel = connection.channel()

channel.exchange_declare(exchange=exchange_name, exchange_type="fanout")

result = channel.queue_declare(queue="", exclusive=True)
queue_name = result.method.queue
channel.queue_bind(exchange=exchange_name, queue=queue_name)


def callback(ch, method, properties, body):
    print(f" [x] {body}")


print(" [*] Waiting for messages. To exit press CTRL+C")
channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
channel.start_consuming()
