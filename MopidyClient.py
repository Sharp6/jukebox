import requests

class MopidyClient:
    def __init__(self):
        self.clearData = '{ "jsonrpc": "2.0", "id": 1, "method": "core.tracklist.clear" }'
        self.playData = '{ "jsonrpc": "2.0", "id": 1, "method": "core.playback.play" }'
        self.stopData = '{ "jsonrpc": "2.0", "id": 1, "method": "core.playback.stop" }'
        self.setVolume = '{ "jsonrpc": "2.0", "id": 1, "method": "core.mixer.set_volume", "params": { "volume": 10} }'
        self.url = 'http://127.0.0.1:6680/mopidy/rpc'

        requests.post(self.url, data=self.setVolume)

    def play(self,uri):
        print "MOPIDY PLAYING " + uri
        requests.post(self.url, data=self.clearData)

        type = uri.split(":")[0]

        if type == "file":
            print "Loading file"
            loadUri = uri

        # Currently only loads the first track of a playlist
        if type == "m3u":
            print "Loading M3U"
            getTracks = '{ "jsonrpc": "2.0", "id": 1, "method": "core.playlists.lookup", "params": { "uri": "' + uri + '" } }'
            r = requests.post(self.url, data=getTracks)
            j = r.json()
            loadUri = j['result']['tracks'][0]['uri']

        requests.post(self.url, data=self.clearData)
        loadData = '{ "jsonrpc": "2.0", "id": 1, "method": "core.tracklist.add", "params": { "uri": "' + loadUri + '" } }'
        requests.post(self.url, data=loadData)
        requests.post(self.url, data=self.playData)

    def stop(self):
        print "MOPIDY STOPPING"
        requests.post(self.url, data=self.stopData)
        requests.post(self.url, data=self.clearData)
