import binascii
import sys

import Adafruit_PN532 as PN532

CS   = 16
MOSI = 23
MISO = 24
SCLK = 25

pn532 = PN532.PN532(cs=CS, sclk=SCLK, mosi=MOSI, miso=MISO)
pn532.begin()
ic, ver, rev, support = pn532.get_firmware_version()
print('Found PN532 with firmware version: {0}.{1}'.format(ver, rev))
pn532.SAM_configuration()

print('Waiting for MiFare card...')
while True:
    uid = pn532.read_passive_target()

    if uid is None:
        continue

    print('Found card with UID: 0x{0}'.format(binascii.hexlify(uid)))
    
