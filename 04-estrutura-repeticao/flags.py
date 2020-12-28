prompt = "\nNome da cidade: "
prompt += "\nEnter ou 'quit' para sair\n"

while True:
    cidade = input(prompt)

    if cidade == 'quit':
        break
    else:
        print("Eu amo essa cidade" + cidade.title() + "!")