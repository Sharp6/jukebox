"use strict";

var MopidyAgentWorker = function(mopidy) {
    this.mopidy = mopidy;
    this.doWork = function(message) {
        this.mopidy.play()
        return 'null';
    }.bind(this);

};

module.exports = MopidyAgentWorker;