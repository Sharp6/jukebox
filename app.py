from CardListener import CardListener
from RedisClient import RedisClient
from MopidyClient import MopidyClient

import logging
logger = logging.getLogger('jukebox')
hdlr = logging.FileHandler('./jukebox.log')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr)
logger.setLevel(logging.INFO)

cardListener = CardListener()
redisClient = RedisClient()
mopidyClient = MopidyClient()

cachedCardId = None

while True:
    cardId = cardListener.checkCard()
    if cardId is None:
        # STOP MOPIDY PLAYBACK
        cachedCardId = None
        mopidyClient.stop()
        continue

    if cardId == cachedCardId:
        continue

    cachedCardId = cardId

    logger.info('Got new card with UID: ' + cardId)
    # Based on the card id, something can be fetched from REDIS
    albumId = redisClient.retrieve(cardId)

    if albumId is None:
        logger.warning("No album to be found for card " + cardId)
        continue

    logger.info('Got album ' + albumId)
    print('Got album ' + albumId)
    mopidyClient.play(albumId)
