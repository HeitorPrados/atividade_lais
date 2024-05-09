from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/inverter', methods=['POST'])
def inverter():
    string1 = request.form['string1']
    string_invertida = (string1[::-1])
    mensagem = string_invertida

    return render_template('index.html', msg=mensagem)

if __name__ == "__main__":
    app.run(debug=True)
