"use strict";

var MopidyAgentWorker = function(mopidy, sender) {
    this.mopidy = mopidy;
    this.sender = sender;
    this.tracks;

    this.mopidy.on("state:online", () => {
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

};

module.exports = MopidyAgentWorker;
