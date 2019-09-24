import pika
import time
import pandas as pd
import json

credentials = pika.PlainCredentials('thinhle', 'meomeo')

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='171.244.51.228', port=5672, virtual_host='/', 
                                credentials=credentials))
channel = connection.channel()

channel.queue_declare(queue='demo_vnas', durable=True)
print(' [*] Waiting for messages. To exit press CTRL+C')


def callback(ch, method, properties, body):
    # print(x)
    print(body.decode())
    # time.sleep(body.count(b'.'))
    print(" [x] Done")
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='demo_vnas', on_message_callback=callback)

channel.start_consuming()

