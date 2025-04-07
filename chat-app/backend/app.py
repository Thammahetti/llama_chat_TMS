from flask import Flask, render_template
from flask_socketio import SocketIO, send
from flask_cors import CORS  # Importa CORS
import threading

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

def send_timed_message():
    socketio.emit('message', 'Messaggio inviato dal server dopo 5 secondi!')


@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def handle_connect():
    print('Client connesso')
    timer = threading.Timer(5.0, send_timed_message) # Invia il messaggio dopo 5 secondi
    timer.start()

@socketio.on('message')
def handle_message(msg):
    print(f"Messaggio ricevuto: {msg}")
    send(msg, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)
