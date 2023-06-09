import speech_recognition as sr

def captar_microfone():
    microfone = sr.Recognizer()

    with sr.Microphone() as source:
        
        microfone.adjust_for_ambient_noise(source) # reduzir ruidos
        print("Fale algo:")
        audio = microfone.listen(source)

    try:
        frase = microfone.recognize_google(audio, language='pt-BR')
        print("Você disse: "+ frase)

    except sr.UnknownValueError:
        print("Não entendi")
        return None
    
    return frase