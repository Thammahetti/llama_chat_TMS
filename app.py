import ollama
import pandas as pd
import requests
from bs4 import BeautifulSoup

# Carica il file Excel con le parole chiave
file_excel_parole_chiave = "parole_chiave.xlsx"  # Cambia con il nome del tuo file Excel contenente le parole chiave
df_parole_chiave = pd.read_excel(file_excel_parole_chiave)

# Rimuovi eventuali spazi extra nei nomi delle colonne
df_parole_chiave.columns = df_parole_chiave.columns.str.strip()

# Verifica e stampa i nomi delle colonne
print("Colonne trovate nel file delle parole chiave:", df_parole_chiave.columns)

# Supponiamo che la colonna contenente le parole chiave si chiami 'ParoleChiave'
parole_chiave = df_parole_chiave['ParoleChiave'].dropna().tolist()

# Aggiungi parole chiave temporali per evitare concetti fuori contesto
parole_fuori_contesto = ["terrorismo 2001", "settembre 11", "attentato 2001"]

print("Parole chiave caricate:", parole_chiave)

print("##############")
print("Domande su: Anni di piombo")
print("##############")

while True:
   
    userinput = input("You: ").strip().lower()


    if any(parola in userinput for parola in parole_chiave):
  
        if any(parola_fuori_contesto in userinput for parola_fuori_contesto in parole_fuori_contesto):
            print("Ollama: Questa domanda non è correlata agli anni di piombo.")
        else:

            response = ollama.generate(
                model='llama3',
                prompt=f"Rispondi alla seguente domanda usando solo queste informazioni:\n\n{testo_fonti}\n\nDomanda: {userinput}\nRisposta:"
            )
            print("Ollama:", response['response'])
    else:

        print("Ollama: Posso rispondere solo a domande relative agli argomenti trattati nei link forniti.")
