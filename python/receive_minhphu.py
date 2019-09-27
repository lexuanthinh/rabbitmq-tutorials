#!/usr/bin/env python
import pika

credentials = pika.PlainCredentials('aiacadmp', 'meomeo1012')

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='10.84.17.40', port=5672, virtual_host='/', credentials=credentials))
channel = connection.channel()

channel.queue_declare(queue='hello')

## Write your code in callback function##
def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    print(body)


channel.basic_consume(
    queue='hello', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
