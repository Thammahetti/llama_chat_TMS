import ollama
import pandas as pd
import requests
from bs4 import BeautifulSoup

# 🔹 Carica il file Excel
file_excel = "link_fonti.xlsx"  
df = pd.read_excel(file_excel)

# 🔹 Rimuovi eventuali spazi extra nei nomi delle colonne
df.columns = df.columns.str.strip()

# 🔹 Verifica e stampa i nomi delle colonne per confermare
print("Colonne trovate:", df.columns)

# 🔹 Se il file ha solo una colonna con i link, accediamo alla prima colonna (senza nome specifico)
links = df.iloc[:, 0].dropna().tolist()  # Prende la prima colonna (senza nome)

# 🔹 Funzione per scaricare il testo da una pagina web
def scarica_testo(url):
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()  # Verifica che la richiesta sia andata a buon fine
        soup = BeautifulSoup(response.text, "html.parser")
        return " ".join([p.get_text() for p in soup.find_all("p")])  # Estrai solo i paragrafi
    except Exception as e:
        print(f"Errore nel caricamento di {url}: {e}")
        return ""  # Se c'è un errore, ritorna una stringa vuota

# 🔹 Scarica il contenuto di tutte le pagine web
testo_fonti = " ".join([scarica_testo(link) for link in links])[:10000]  # Limitiamo a 10000 caratteri per velocità

print("##############")
print("Domande su: Anni di piombo")
print("##############")

while True:
    # Prendi l'input dell'utente
    userinput = input("You: ").strip()

    # 🔹 Genera la risposta utilizzando Ollama e il testo scaricato
    response = ollama.generate(
        model='llama3',
        prompt=f"Rispondi alla seguente domanda usando solo queste informazioni:\n\n{testo_fonti}\n\nDomanda: {userinput}\nRisposta:"
    )

    # Stampa la risposta generata da Ollama
    print("Ollama:", response['response'])
