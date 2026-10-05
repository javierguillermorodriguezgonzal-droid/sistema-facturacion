from flask import Flask

app = Flask(__name__)

@app.route("/")
def inicio():
    return "Sistema de facturación Brasas de Oro"

if __name__ == "__main__":
    app.run(debug=True)