#!/usr/bin/env python
import pika
from albumRetrieverWorker import AlbumRetrieverWorker

class AlbumRetrieverRabbitListener:
    def __init__(self):
        ex = 'jukeboxExchange'
        self.albumRetriever = AlbumRetrieverWorker()

        connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        channel = connection.channel()
        channel.exchange_declare(exchange=ex, type='topic')

        result = channel.queue_declare(exclusive=True)
        queue_name = result.method.queue
        channel.queue_bind(exchange=ex, queue=queue_name, routing_key='card')

        print(' [*] Waiting for logs. To exit press CTRL+C')

        channel.basic_consume(self.callback, queue=queue_name, no_ack=True)
        channel.start_consuming()

    def callback(self, ch, method, properties, body):
        print("ALBUMRETRIEVER RABBIT LISTENER: Should now call albumRetriever worker")
        print(" [x] %r:%r" % (method.routing_key, body))
        self.albumRetriever.doWork(body)

if __name__ == '__main__':
    print("Running albumretriever rabbitlistener standalone")
    alrl = AlbumRetrieverRabbitListener()
