import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
channel = connection.channel()
queue_name = "rpc_queue"

channel.queue_declare(queue=queue_name)


def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


def on_request(ch, method, properties, body):
    n = int(body)
    print(f" [.] fib({n})")
    response = fib(n)

    ch.basic_publish(
        exchange="",
        routing_key=properties.reply_to,
        properties=pika.BasicProperties(correlation_id=properties.correlation_id),
        body=str(response),
    )
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue=queue_name, on_message_callback=on_request)
print(" [x] Awaiting RPC requests")
channel.start_consuming()
