#!/usr/bin/env python
import pika
from mopidyAgentWorker import MopidyAgentWorker

class MopidyAgentRabbitListener:
    def __init__(self):
        ex = 'jukeboxExchange'
        self.mopidyAgent = MopidyAgentWorker()

        connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        channel = connection.channel()
        channel.exchange_declare(exchange=ex, type='topic')

        result = channel.queue_declare(exclusive=True)
        queue_name = result.method.queue
        channel.queue_bind(exchange=ex, queue=queue_name, routing_key='album')

        print(' [*] Waiting for logs. To exit press CTRL+C')

        channel.basic_consume(self.callback, queue=queue_name, no_ack=True)
        channel.start_consuming()

    def callback(self, ch, method, properties, body):
        print("ALBUMRETRIEVER MOPIDY AGENT: Should now call mopidyAgent worker")
        print(" [x] %r:%r" % (method.routing_key, body))
        self.mopidyAgent.doWork(body)

if __name__ == '__main__':
    print("Running mopidyAgent rabbitlistener standalone")
    marl = MopidyAgentRabbitListener()
