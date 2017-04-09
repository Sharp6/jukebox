#!/usr/bin/env python
import pika

class AlbumRetrieverRabbitSender:
    def __init__(self):
        self.exchange = 'jukeboxExchange'

    def publish(self, message):
        connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        channel = connection.channel()
        channel.exchange_declare(exchange=self.exchange, type='topic')
        routing_key = 'album'

        print(" [x] Sent %r:%r" % (routing_key, message))
        print(connection)
        channel.basic_publish(exchange=self.exchange, routing_key=routing_key, body=message)

        connection.close()
