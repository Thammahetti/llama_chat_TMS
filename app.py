import ollama
import wikipediaapi

wiki_wiki = wikipediaapi.Wikipedia(
    user_agent="MyWikipediaBot/1.0 (https://it.wikipedia.org)",
    language="it"
)

TOPIC = "Anni di piombo"
page = wiki_wiki.page(TOPIC)

if not page.exists():
    print(f"Errore: La pagina Wikipedia su '{TOPIC}' non esiste.")
    exit()


wiki_content = page.summary 

print("##############")
print(f"Domande su: {TOPIC}")
print("##############")

while True:
    userinput = input("You: ").strip()

    if any(word in wiki_content.lower() for word in userinput.lower().split()):
        response = ollama.generate(
            model='gemma:2b',
            prompt=f"Rispondi alla seguente domanda usando solo queste informazioni:\n\n{wiki_content}\n\nDomanda: {userinput}\nRisposta:"
        )
        print("Ollama:", response['response'])
    else:
        print(f"Ollama: Posso rispondere solo a domande su '{TOPIC}'.")
