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
        #requests.post(self.url, data=self.clearData)
        getTracks = '{ "jsonrpc": "2.0", "id": 1, "method": "core.playlists.lookup", "params": { "uri": "m3u:handjesdraaien.m3u8" } }'

        requests.post(self.url, data=self.clearData)
        r = requests.post(self.url, data=getTracks)
        j = r.json()
        print "GOT JSON"
        print j

        tracks = j.result.tracks[0].uri

        loadData = '{ "jsonrpc": "2.0", "id": 1, "method": "core.tracklist.add", "params": { "uri": "' + track + '" } }'
        requests.post(self.url, data=loadData)
        requests.post(self.url, data=self.playData)

    def stop(self):
        print "MOPIDY STOPPING"
        requests.post(self.url, data=self.stopData)
        requests.post(self.url, data=self.clearData)
