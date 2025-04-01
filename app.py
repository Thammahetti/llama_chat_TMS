import ollama
import pandas as pd
import requests
from bs4 import BeautifulSoup


file_excel = "link_fonti.xlsx"  
df = pd.read_excel(file_excel)


df.columns = df.columns.str.strip()


print("Colonne trovate:", df.columns)

links = df.iloc[:, 0].dropna().tolist()


def scarica_testo(url):
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status() 
        soup = BeautifulSoup(response.text, "html.parser")
        return " ".join([p.get_text() for p in soup.find_all("p")])  
    except Exception as e:
        print(f"Errore nel caricamento di {url}: {e}")
        return ""

testo_fonti = " ".join([scarica_testo(link) for link in links])[:10000]  

print("##############")
print("Domande su: Anni di piombo")
print("##############")

while True:

    userinput = input("You: ").strip()

    response = ollama.generate(
        model='llama3',
        prompt=f"Rispondi alla seguente domanda usando solo queste informazioni:\n\n{testo_fonti}\n\nDomanda: {userinput}\nRisposta:"
    )

    # Stampa la risposta generata da Ollama
    print("Ollama:", response['response'])
