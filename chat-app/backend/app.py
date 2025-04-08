from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import ollama

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('message')
def handle_message(msg):
    print(f"Received message: {msg}")

    # Logica per generare la risposta con Ollama
    response = ollama.chat(
        model='llama3',
        messages=[{
            "role": "user",
            "content": f" Rispondi alla seguente domanda usando solo informazioni relative agli Anni di Piombo se non centra niente allora non rispondere però rispondi a domande di presentazione dell'utente (com'è stai ? o ciao). Rispondi in breve, più veloce possibile:\n\nDomanda: {msg}\nRisposta:"
        }],
        stream=True
    )

    # Invio della risposta al frontend
    for chunk in response:
        emit('message', chunk['message']['content'])

if __name__ == '__main__':
    socketio.run(app, debug=True)
