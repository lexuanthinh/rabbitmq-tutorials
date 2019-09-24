import pika
import json
import os
import sys
import pandas as pd
import json_lines
import time

credentials = pika.PlainCredentials('thinhle', 'meomeo')

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='171.244.51.228', port=5672, virtual_host='/', 
                        credentials=credentials))
channel = connection.channel()

# channel.exchange_declare(exchange='logs', exchange_type='fanout')

channel.queue_declare(queue='demo_vnas', durable=True)

with open('nguoiduatin_phapluat.json', 'rb') as f:
    for message in json_lines.reader(f):
        channel.basic_publish(
            exchange='',
            routing_key='demo_vnas',
            body=json.dumps(message, ensure_ascii=False).encode('utf-8'),
            # properties=pika.BasicProperties(
            #     delivery_mode=2,
            )
        
        time.sleep(5)
        print(message['content'])

connection.close()
