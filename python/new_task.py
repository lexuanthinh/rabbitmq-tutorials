#!/usr/bin/env python
import pika
import sys

credentials = pika.PlainCredentials('thinhle', 'meomeo')

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='171.244.51.228', port=5672, virtual_host='/', credentials=credentials))
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)

message = ' '.join(sys.argv[1:]) or "Hello World!"
print(message)

channel.basic_publish(
    exchange='',
    routing_key='task_queue',
    body=message,
    properties=pika.BasicProperties(
        delivery_mode=2,  # make message persistent
    ))
print(" [x] Sent %r" % message)
connection.close()
