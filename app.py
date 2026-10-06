from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def ingreso():
    return render_template("ingreso.html")

@app.route("/menu")
def menu():
    return render_template("index.html")

@app.route("/productos")
def productos():
    return render_template("productos.html")

@app.route("/registrar_producto")
def registrar_producto():
    return render_template("registrar_producto.html")

@app.route("/agregar_productos")
def agregar_productos():
    return render_template("agregar_productos.html")

@app.route("/editar_producto")
def editar_producto():
    return render_template("editar_producto.html")

@app.route("/eliminar_productos")
def eliminar_productos():
    return render_template("eliminar_productos.html")

@app.route("/consultar_inventarios")
def consultar_inventarios():
    return render_template("consultar_inventarios.html")

@app.route("/clientes")
def clientes():
    return render_template("clientes.html")

@app.route("/ventas")
def ventas():
    return render_template("ventas.html")

@app.route("/ingresar", methods=["POST"])
def ingresar():
    usuario = request.form["usuario"]
    contraseña = request.form["contraseña"]

    return redirect(url_for("menu"))

if __name__ == "__main__":
    app.run(debug=True)