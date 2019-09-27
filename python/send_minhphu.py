#!/usr/bin/env python
import pika

credentials = pika.PlainCredentials('aiacadmp', 'meomeo1012')

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='10.84.17.40', port=5672, virtual_host='/', credentials=credentials))
channel = connection.channel()

channel.queue_declare(queue='hello')

channel.basic_publish(exchange='', routing_key='hello', body='gaugau')
print(" [x] Sent 'gaugau'")
connection.close()
 