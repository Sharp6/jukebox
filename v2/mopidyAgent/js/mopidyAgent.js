var Worker = require('./mopidyAgentWorker');
var Mopidy = require("mopidy");
var amqp = require('amqplib/callback_api');
var RabbitSender = require('./mopidyAgentRabbitSender');
var RabbitListener = require('./mopidyAgentRabbitListener');

var mopidy = new Mopidy({
	webSocketUrl: "ws://localhost:6680/mopidy/ws/"
});

var sender = new RabbitSender(amqp);
var worker = new Worker(mopidy, sender);
var listener = new RabbitListener(amqp, worker);
