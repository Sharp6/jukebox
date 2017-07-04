var worker = function(sender, redis) {
    this.sender = sender;
    this.client = redis.createClient();

    this.client.on('connected', () => {
        console.log("DbAgentWorker: Redis client connected.");
    });

    this.retrieveAlbum = function(card) {
        this.client.get(card, (err, reply) => {
            if(err) {
                return console.log(err);
            } else if(!reply || reply.length === 0) {
                this.sender.send("album", "No music for the current card.");
                return console.log("No music found for current card");
            } else {
                this.sender.send("album", reply);
            }            
        });
    }.bind(this);

    this.connectCardToMusic = function(card,uri) {
        this.client.set(card, uri, (err,reply) => {
            if(err) { 
                console.log(err);
            } else {
                console.log(reply);
            } 
        });
    }.bind(this);
    
};

module.exports = worker;
