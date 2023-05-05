from gtts import  gTTS
import playsound

def voz_assistente(frase):
    filename = "assistente.mp3"

    gtts_object = gTTS(text=frase, lang='pt', slow=False)
    gtts_object.save(filename)

    playsound.playsound(filename)