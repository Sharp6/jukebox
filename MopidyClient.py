import pykka
from mopidy import core

class MopidyClient(pykka.ThreadingActor, core.CoreListener):
    def __init__(self, config, core):
        super(MopidyClient, self).__init__()
        self.core = core
        self.core.playback.play()

mc = MopidyClient()
