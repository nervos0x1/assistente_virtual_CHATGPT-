import scripts.assistente as assistente
import scripts.chatGPT as chatGPT
import scripts.microfone as microfone


while True:

    frase = microfone.captar_microfone()

    if frase == None:
        continue

    if "Fechar programa" in frase:
        break

    
    resposta = chatGPT.chat_gpt(frase)


    assistente.voz_assistente(frase)

print('Programa finalizado')