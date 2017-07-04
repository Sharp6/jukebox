var express = require('express');
var app = express();
var server = require('http').Server(app);
var path = require('path');

var io = require('socket.io')(server);
var amqp = require('amqplib/callback_api');

var Sender = require('webserverRabbitSender');
var sender = new Sender(amqp);

app.use(express.static(path.join(__dirname,'public')));

server.listen(1804, function(){
  console.log("Listening on jb-webserver on port 1804");
});

io.on('connection', function (socket) {
  socket.emit('message', { system: 'Connected to socket.io server' });

  socket.on('command.save', function (data) {
    console.log(data);
    sender.send('command.save', JSON.stringify(data));
  });
});

amqp.connect('amqp://localhost', function(err, conn) {
  if(err) {
    return console.log(err);
  }

  conn.createChannel(function(err, ch) {
    var ex = 'jukeboxExchange';

    ch.assertExchange(ex, 'topic', {durable: false});
    ch.assertQueue('', {exclusive: true}, function(err, q) {
      ch.bindQueue(q.queue, ex, '#');

      ch.consume(q.queue, function(msg) {
        var message = {};
        message[msg.fields.routingKey] = msg.content.toString();
        io.sockets.emit('message', message);
      }, {noAck: true});
    });
  });
});
