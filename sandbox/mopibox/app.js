var Mopidy = require("mopidy");
var mopidy = new Mopidy();

mopidy.on(console.log.bind(console));

mopidy.on("state:online", function () {
    mopidy.library.browse("file:///home/pi/music")
        .then(result => {
            console.log(result);
        })
        .catch(console.error.bind(console))
        .done();
});