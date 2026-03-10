# Importa a classe Flask e a função render_template
from flask import Flask, render_template

# Cria a aplicação Flask
app = Flask(__name__)

# Rota principal do site
@app.route("/")
def pagina_inicial():
    # Abre o ficheiro index.html da pasta templates
    return render_template("index.html")

# Mantém a aplicação a correr
if __name__ == "__main__":
    app.run(debug=True)