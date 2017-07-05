"use strict";

var MopidyAgentWorker = function(mopidy, sender) {
    this.mopidy = mopidy;
    this.sender = sender;
    this.tracks;

    this.mopidy.on("state:online", () => {
        this.mopidy.mixer.setVolume(10);
        this.mopidy.tracklist.clear()
            .then(() => {
                return this.mopidy.library.browse("file:///home/pi/music");
            })    
            .then(result => {
                this.tracks = result.map(track => {
                    return {
                        name: track.name,
                        uri: track.uri
                    };
                });
                this.sender.send("tracklist", JSON.stringify(this.tracks));
            })
            .catch(console.error.bind(console))
            .done();
    });

    this.doWork = function(message) {
        this.mopidy.play()
        return 'null';
    }.bind(this);

    this.play = function(album) {
        if(!album || album.length === 0 || album.includes("No music")) {
            this.mopidy.playback.stop()
            .then(result => {
                return mopidy.tracklist.clear();
            })
            .catch(console.error.bind(console))
            .done();
        } else {
            this.mopidy.tracklist.clear()
                .then(result => {
                    return mopidy.tracklist.add(undefined,undefined,album);
                })
                .then(result => {
                    return mopidy.playback.play();
                })
                .catch(console.error.bind(console))
                .done();
        }
    }.bind(this);

    this.handleCommand = function(command) {
        if(command === "volumeUp") {
            this.mopidy.mixer.getVolume()
                .then(currentVolume => {
                    return Math.min(100, currentVolume + 10);
                })
                .then(newVolume => {
                    return this.mopidy.mixer.setVolume(newVolume);
                })
                .catch(console.error.bind(console))
                .done();
        }

        if(command === "volumeDown") {
            this.mopidy.mixer.getVolume()
                .then(currentVolume => {
                    return Math.max(0, currentVolume - 10);
                })
                .then(newVolume => {
                    return this.mopidy.mixer.setVolume(newVolume);
                })
                .catch(console.error.bind(console))
                .done();
        }
    }.bind(this);
};

module.exports = MopidyAgentWorker;
