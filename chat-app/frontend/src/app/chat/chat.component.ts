import { Component, OnInit } from '@angular/core';
import { io } from 'socket.io-client';  // Importa io correttamente

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
    // Connessione al server Flask con Socket.IO (se necessario per la gestione in tempo reale)
    this.socket = io('https://5000-andrea1932734-realtime-yzlu2wvctoc.ws-eu118.gitpod.io');  // Modifica l'URL se necessario

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

      // Simula una risposta dal server dopo 5 secondi
      setTimeout(() => {
        this.receiveServerResponse();
      }, 5000);  // 5000 ms = 5 secondi
    }
  }

  // Metodo per gestire la risposta simulata del server
  receiveServerResponse() {
    // Aggiungi un messaggio di risposta simulata
    const serverMessage = "Server: Ciao, come posso aiutarti?";  // Puoi personalizzare questo messaggio

    // Aggiungi la risposta del server alla chat
    this.messages.push(serverMessage);

    // Nascondi l'indicatore di "scrittura" del server
    this.isTyping = false;
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
