import speech_recognition as sr

r = sr.Recognizer()
mic = sr.Microphone()
with mic as source:
    print("Diga alguma coisa: ")
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)

    try:
        frase = r.recognize_google(audio,language='pt-BR')
        print("Você disse: " + frase)

    except:
        print("Não entendi")
        
    # except sr.UnkownValueError:
    #     print("Não entendi")

    # except sr.RequestError as error:
    #     print("ERROR!")