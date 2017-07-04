var dbAgent = function(amqp, worker) {
    this.amqp = amqp;
    this.worker = worker;

    this.amqp.connect('amqp://localhost', function(err, conn) {
        conn.createChannel((err, ch) => {
            var ex = 'jukeboxExchange';
            ch.assertExchange(ex, 'topic', {durable: false});
            ch.assertQueue('', {exclusive: true}, (err, q) => {
                ch.bindQueue(q.queue, ex, 'card');
                ch.consume(q.queue, (msg) => {
                    console.log(" [x] %s:'%s'", msg.fields.routingKey, msg.content.toString());
                    this.worker.retrieveAlbum(msg.content.toString());
                }, {noAck: true});
            });

            ch.assertQueue('', {exclusive: true}, (err, q) => {
                ch.bindQueue(q.queue, ex, 'command.save');
                ch.consume(q.queue, (msg) => {
                    console.log(" [x] %s:'%s'", msg.fields.routingKey, msg.content.toString());
                    var obj = JSON.parse(msg.content.toString());
                    this.worker.connectCardToMusic(obj.card,obj.uri);
                }, {noAck: true});
            });
        });
    });
}

module.exports = dbAgent;