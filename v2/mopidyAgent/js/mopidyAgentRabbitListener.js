var Listener = function(amqp, worker) {
    this.amqp = amqp;
    this.worker = worker;

    this.amqp.connect('amqp://localhost', (err, conn) => {
        conn.createChannel((err, ch) => {
            var ex = 'jukeboxExchange';
            ch.assertExchange(ex, 'topic', {durable: false});

            ch.assertQueue('', {exclusive: true}, (err, q) => {
                ch.bindQueue(q.queue, ex, 'album');
                ch.consume(q.queue, (msg) => {
                    console.log("MopidyAgentRabbitListener %s:'%s'", msg.fields.routingKey, msg.content.toString());
                    this.worker.play(msg.content.toString());
                }, {noAck: true});
            });

            ch.assertQueue('', {exclusive: true}, (err, q) => {
                ch.bindQueue(q.queue, ex, 'command.mopidy');
                ch.consume(q.queue, (msg) => {
                    console.log("MopidyAgentRabbitListener %s:'%s'", msg.fields.routingKey, msg.content.toString());
                    this.worker.handleCommand(msg.content.toString());
                }, {noAck: true});
            });
        });
    });
}

module.exports = Listener;
