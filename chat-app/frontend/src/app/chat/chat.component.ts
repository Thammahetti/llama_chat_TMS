import { Component, OnInit } from '@angular/core';
import { io } from 'socket.io-client';

@Component({
  selector: 'app-chat',
  templateUrl: './chat.component.html',
  styleUrls: ['./chat.component.css']
})
export class ChatComponent implements OnInit {
  socket: any;
  message: string = '';
  messages: string[] = [];
  chatOpen: boolean = false;
  isTyping: boolean = false;  // Nuova variabile per gestire lo stato di "scrittura" del server

  ngOnInit() {
    // Connessione al server Flask con Socket.IO (usa l'URL corretto)
    this.socket = io('http://localhost:5000');  // Cambia l'URL a quello del tuo server Flask

    // Ascolta i messaggi ricevuti dal server
    this.socket.on('message', (msg: string) => {
      this.messages.push(msg);
    });
  }

  sendMessage(message: HTMLInputElement) {
    this.message = message.value;
    if (this.message.trim()) {
      // Aggiungi il messaggio dell'utente alla chat
      this.messages.push(`Tu: ${this.message}`);
      message.value = '';  // Pulisce la casella di testo

      // Indica che il server sta scrivendo
      this.isTyping = true;

      // Invia il messaggio al server tramite WebSocket
      this.socket.emit('message', this.message);

      // Imposta il timeout per simulare un ritardo nella risposta
      setTimeout(() => {
        this.isTyping = false;
      }, 5000);  // 5000 ms = 5 secondi
    }
  }

  // Metodo per aprire il popup della chat
  openChat(): void {
    this.chatOpen = true;
  }

  // Metodo per chiudere il popup della chat
  closeChat(): void {
    this.chatOpen = false;
  }

  // Metodo per gestire la pressione di un tasto (Enter)
  onKeydown(event: KeyboardEvent, message: HTMLInputElement): void {
    if (event.key === 'Enter') {
      this.sendMessage(message);
    }
  }
}
