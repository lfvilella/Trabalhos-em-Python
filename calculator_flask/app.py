from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def main(sum=sum):
    if request.method == 'GET':
        return render_template('index.html')

    elif request.method == 'POST':
        expression = request.form.get('textview')
        sum = eval(expression)
        return render_template('index.html', sum=sum)


if __name__ == '__main__':
    app.run(debug=True)