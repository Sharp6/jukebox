# This will be dependent on Mopidy

class MopidyAgentWorker():
    def __init__(self):
        print("Init MopidyAgentWorker")

    def doWork(self, message):
        message = message + " played in Mopidy"
        print("MOPIDYAGENT: " + message)
