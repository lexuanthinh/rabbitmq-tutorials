#!/usr/bin/env python
import pika

credentials = pika.PlainCredentials('thinhle', 'meomeo')

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='171.244.51.228', port=5672, virtual_host='/', credentials=credentials))
channel = connection.channel()

channel.queue_declare(queue='hello')

channel.basic_publish(exchange='', routing_key='hello', body='meomeo')
print(" [x] Sent 'Hello World!'")
connection.close()
 