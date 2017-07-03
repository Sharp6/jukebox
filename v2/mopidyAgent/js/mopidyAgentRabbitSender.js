var sender = function(ampq) {
    this.ampq = ampq;

    this.send = function(key, msg) {
        amqp.connect('amqp://localhost', function(err, conn) {
            conn.createChannel(function(err, ch) {
                var ex = 'jukeboxExchange';

                ch.assertExchange(ex, 'topic', {durable: false});
                ch.publish(ex, key, new Buffer(msg));
                console.log(" [x] Sent %s:'%s'", key, msg);
            });

            setTimeout(function() { conn.close(); }, 500);
        });
    }.bind(this);
}