from flask import Flask, render_template, jsonify
from flask_socketio import SocketIO
import thread

class ConfigServer():
    def __init__(self):
        self.app = Flask(__name__)
        self.app.config['SECRET_KEY'] = 'secret!'
        self.app.add_url_rule('/', 'main', self.main)

        self.socketio = SocketIO(self.app)

    def main(self):
        return render_template('index.html')

    def setCard(self, cardId):
        with self.app.app_context():
            with self.app.test_request_context():
                self.socketio.emit('setCard', jsonify({ cardId: cardId }))

    def flaskThread(self):
        self.socketio.run(self.app)

    def run(self):
        print("Starting")
        thread.start_new_thread(self.flaskThread,())

if __name__ == '__main__':
    print("Running standalone")
    myCS = ConfigServer()
    myCS.run()
    while True:
        continue
