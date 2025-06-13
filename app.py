from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    resultado = ""
    expressao = ""

    if request.method == "POST":
        expressao = request.form.get("expressao", "")
        try:
            # Avalia a expressão com segurança
            resultado = str(eval(expressao, {"__builtins__": None}, {}))
        except:
            resultado = "Erro"

    return render_template("index.html", resultado=resultado, expressao=expressao)

if __name__ == "__main__":
    app.run(debug=True)
