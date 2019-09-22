#!/usr/bin/env python
import pika
def publish_test(testcase):
    print('*****************', testcase)
    user = "admin"
    password = "admin"
    credentials = pika.PlainCredentials(user, password)
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='192.168.226.130', credentials=credentials))
    channel = connection.channel()

    channel.queue_declare(queue='hello')

    channel.basic_publish(exchange='', routing_key='hello', body=testcase)
    # print(" [x] Sent 'Hello World!'")
    connection.close()