from flask import Flask, render_template, request


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/melhorCombustivel")
def calcular_combustível():
    gasolina = None
    Etanol = None
    result None
    msg = None
    if request.method == 'POST':
        gasolina =    float(request.form.get("gasolina" ,"").replace
                if request.method == 'POST':
                    gasolina = request.form.get("gasolina" ,"")
        etanol = request.form.get("etanol" ,"")
        msg = f"Melhor abastecer com {result}."
        return render_template("index.html", msg=msg)
        result = "Etanol" if etanol <=
        gasolina*0.75 else "Gasolina"
        return render_template("index.html") 
    etanol = float(request.args.get("etanol"))

    if etanol / gasolina < 0.7:
        resultado = "Etanol é a melhor opção."
    else:
        resultado = "Gasolina é a melhor opção."

    return render_template("resultado.html", resultado=resultado)

if __name__ == "__main__":
    app.run(debug=True)