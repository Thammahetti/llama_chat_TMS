import ollama

TOPIC = "Anni di piombo"


print("##############")
print(f"Domande su: {TOPIC}")
print("##############")

while True:
    userinput = input("You: ").strip().lower()
    response = ollama.generate(
            model='llama3',
            prompt=f"Rispondi alla seguente domanda usando solo informazioni relative agli Anni di Piombo se non centra niente allora non rispondere però rispondi a domande di presetazione del utente (com'è stai ? o ciao):\n\nDomanda: {userinput}\nRisposta:"
        )
    print("Ollama:", response['response'])
