from CardListener import CardListener

cardListener = CardListener()
#redisClient = RedisClient()
#mopidyClient = MopidyClient()

cachedCardId

while True:
    cardId = cardListener.checkCard()
    if cardId is None:
        # STOP MOPIDY PLAYBACK
        continue

    if cardId == cachedCardId:
        continue

    cachedCardId = cardId

    print('Got new card with UID: 0x{0}'.cardId)
    # Based on the card id, something can be fetched from REDIS
    #albumId = redisClient.retrieve(cardId)
    # Based on Redis output, mopidy can be called
    # I AM THE MASTER DEPLOYER
