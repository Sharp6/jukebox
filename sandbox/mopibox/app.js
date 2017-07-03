var Mopidy = require("mopidy");
var mopidy = new Mopidy({
	webSocketUrl: "ws://localhost:6680/mopidy/ws/"
});

//mopidy.on(console.log.bind(console));

mopidy.on("state:online", function () {
    mopidy.library.browse("file:///home/pi/music")
        .then(result => {
            console.log(result);
	    return mopidy.playback.play
        })
        .catch(console.error.bind(console))
        .done();
});
