# This will be dependent on Redis
from albumRetrieverRabbitSender import AlbumRetrieverRabbitSender

class AlbumRetrieverWorker:
    def __init__(self):
        self.rabbitSender = AlbumRetrieverRabbitSender()

    def doWork(self, message):
        message = message + "albumRetrieved"
        self.rabbitSender.publish(message)
