import binascii
import sys

import Adafruit_PN532 as PN532

class CardListener:
    def __init__(self):
        CS   = 18
        MOSI = 23
        MISO = 24
        SCLK = 25

        self.pn532 = PN532.PN532(cs=CS, sclk=SCLK, mosi=MOSI, miso=MISO)
        self.pn532.begin()
        print('Found PN532')

        self.pn532.SAM_configuration()

    def checkCard(self):
        uid = self.pn532.read_passive_target()
        if uid is None:
            return None
        else:
            return format(binascii.hexlify(uid))
