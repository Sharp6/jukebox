from flask import Flask
import thread

class ConfigServer():
    def __init__(self):
        self.data = 'foo'
        self.app = Flask(__name__)
        self.app.add_url_rule('/', 'main', self.main)

    def main(self):
        return self.data

    def flaskThread(self):
        self.app.run()

    def run(self):
        print("Starting")
        thread.start_new_thread(self.flaskThread,())
