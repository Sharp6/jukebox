var amqp = require('amqplib/callback_api');
var redis = require('redis');
var Listener = require('./dbAgentRabbitListener');
var Worker = require('./daAgentWorker');
var Sender = require('./dbAgentRabbitSender');

var sender = new Sender(amqp);
var worker = new Worker(sender, redis);
var listener = new Listener(amqp, worker);