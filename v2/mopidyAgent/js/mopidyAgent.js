var Worker = require('./mopidyAgentWorker');
var Mopidy = require("mopidy");
var amqp = require('amqplib/callback_api');
var RabbitSender = require('./mopidyAgentRabbitSender');


var mopidy = new Mopidy({
	webSocketUrl: "ws://localhost:6680/mopidy/ws/"
});

var sender = new RabbitSender(ampq);
var worker = new Worker(mopidy, sender);