#!/usr/bin/env python
import pika
import utils

# credentials = pika.PlainCredentials(user, password)
#         connection = pika.BlockingConnection(pika.ConnectionParameters(host=broker,
#
#                                                                        credentials=credentials))
def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)

user = "admin"
password = "admin"
credentials = pika.PlainCredentials(user, password)
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='192.168.226.130', credentials=credentials))
channel = connection.channel()


channel.queue_declare(queue='hello')
channel.basic_qos(prefetch_count=1)
channel.basic_consume(consumer_callback=callback, queue='hello')


print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
