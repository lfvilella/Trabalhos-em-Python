from flask import Flask, request, render_template
import speech_recognition as sr

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def main(sum=sum):
    if request.method == 'GET':
        return render_template('index.html')

    elif request.method == 'POST':
        try:
            frase = microphone()
            sum = eval(frase)
            return render_template('index.html', sum=sum, frase=frase)
    
        except:
            return render_template('index.html', sum="TryAgain")

    # elif request.method == 'POST':
    #     expression = request.form.get('textview')
    #     sum = eval(expression)
    #     return render_template('index.html', sum=sum)

def microphone():
    r = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        print("Diga alguma coisa: ")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

        try:
            frase = r.recognize_google(audio,language='pt-BR')
            # print("Você disse: " + frase)
            return frase

        except:
            # print("Não entendi")
            return "Não entendi"


if __name__ == '__main__':
    app.run(debug=True)