'use strict'

const Worker = require('./mopidyAgentWorker');

const chai = require('chai');
const expect = chai.expect;
const sinon = require('sinon');
chai.use(require('sinon-chai'));

describe('Mopidy module', () => {  
  describe('as general feature', () => {
    it('should export a function', () => {
      expect(Worker).to.be.a('function');
    });
  });

  var worker;
  var mopidyMock = {
          play: function() {
              console.log("PLAY");
          }
      }

  function init() {
      worker = new Worker(mopidyMock);
  }
  function cleanup() {
      worker = undefined;
  }

  before(init);
  after(cleanup);

  describe('after init', () => {
      it('should expose a doWork method', () => {
          expect(worker.doWork).to.be.a('function');
      });
  });

  describe('when given an album message', () => {
      var message = {};
      message.fields = {};
      message.fields.routingKey = 'album';
      message.content = 'Olivia';

      it('should call play method on mopidy', () => {
          sinon.stub(worker.mopidy, 'play');
          worker.doWork(message);
          expect(worker.mopidy.play).to.have.been.calledOnce;
          worker.mopidy.play.restore();
      });

  });
});