import requests

class MopidyClient:
    def __init__(self):
        self.clearData = '{ "jsonrpc": "2.0", "id": 1, "method": "core.tracklist.clear" }'
        self.playData = '{ "jsonrpc": "2.0", "id": 1, "method": "core.playback.play" }'
        self.stopData = '{ "jsonrpc": "2.0", "id": 1, "method": "core.playback.stop" }'
        self.url = 'http://127.0.0.1:6680/mopidy/rpc'

    def play(self,id):
	print("playing" + id);
        print "MOPIDY PLAYING"
        loadData = '{ "jsonrpc": "2.0", "id": 1, "method": "core.tracklist.add", "params": { "uri": "' + id + '" } }'
        #requests.post(self.url, data=self.clearData)
        requests.post(self.url, data=loadData)
        requests.post(self.url, data=self.playData)

    def stop(self):
        print "MOPIDY STOPPING"
        requests.post(self.url, data=self.stopData)
        requests.post(self.url, data=self.clearData)
