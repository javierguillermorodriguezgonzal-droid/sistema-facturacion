from flask import Flask, render_template, request, redirect, url_for, session
import mysql.connector


app = Flask(__name__)
app.secret_key = "brasas_de_oro_clave_local"

conexion =  mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456",
    database="sistema_facturacion_flask"
)

print("CONEXION A MYSQL EXITOSA")
cursor = conexion.cursor()

cursor.execute("SHOW TABLES")

for tabla in cursor:
    print(tabla)

@app.route("/")
def ingreso():
    return render_template("ingreso.html")

@app.route("/menu")
def menu():
    return render_template("index.html")

@app.route("/productos")
def productos():
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM products")
    productos = cursor.fetchall()
    return render_template("productos.html", productos=productos)


@app.route("/registrar_producto", methods=["GET", "POST"])
def registrar_producto():

    if request.method == "POST":

        codigo = request.form["Product_code"]
        nombre = request.form["name"]
        descripcion = request.form["Description"]
        categoria = request.form["Id_Categoria"]
        precio_compra = request.form["Purchase_price"]
        precio_venta = request.form["Selling_price"]
        stock = request.form["Stock"]

        sql = """
            INSERT INTO products
            (Id_Categoria, Product_code, name, Description,
             Purchase_price, Selling_price, Stock)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """

        valores = (
            categoria,
            codigo,
            nombre,
            descripcion,
            precio_compra,
            precio_venta,
            stock
        )

        cursor = conexion.cursor()

        try:
            cursor.execute(sql, valores)
            conexion.commit()
        except Exception:
            conexion.rollback()
            raise
        finally:
            cursor.close()

        return redirect(url_for("productos"))

    return render_template("registrar_producto.html")

@app.route("/agregar_productos", methods=["GET", "POST"])
def agregar_productos():
    if request.method == "POST":

        codigo = request.form["Product_code"]
        accion = request.form["accion"]

        # Buscar un producto por su código
        if accion == "buscar":
            cursor = conexion.cursor()
            cursor.execute(
                "SELECT * FROM products WHERE Product_code = %s",
                (codigo,)
            )
            producto = cursor.fetchone()
            cursor.close()

            return render_template(
                "agregar_productos.html",
                producto=producto
            )

        # Aumentar las unidades existentes en el inventario
        cantidad = int(request.form["cantidad_agregar"])

        cursor = conexion.cursor()
        cursor.execute(
            "SELECT Stock FROM products WHERE Product_code = %s",
            (codigo,)
        )
        producto = cursor.fetchone()

        if producto is None:
            cursor.close()
            return render_template(
                "agregar_productos.html",
                producto=None,
                error="No se encontró el producto."
            )

        stock_actual = producto[0]
        nuevo_stock = stock_actual + cantidad

        sql = """
            UPDATE products
            SET Stock = %s
            WHERE Product_code = %s
        """
        valores = (nuevo_stock, codigo)

        cursor.execute(sql, valores)
        conexion.commit()
        cursor.close()

        return redirect(url_for("productos"))

    return render_template("agregar_productos.html")

@app.route("/editar_producto", methods=["GET", "POST"])
def editar_producto():
    
    if request.method == "POST":

        codigo = request.form["Product_code"]
        accion = request.form["accion"]

        if accion == "buscar":
            cursor = conexion.cursor()
            cursor.execute(
                "SELECT * FROM products WHERE product_code = %s",
                (codigo,)
            )
            producto = cursor.fetchone()
            return render_template(
                "editar_producto.html",
                producto=producto
            )
        nombre = request.form["name"]
        categoria = request.form["Id_Categoria"]
        precio_compra = request.form["Purchase_price"]
        precio_venta = request.form["Selling_price"]

        sql = """
            UPDATE products
            SET Product_code = %s,
                name = %s,
                Id_categoria = %s,
                Purchase_price = %s,
                Selling_price = %s
            WHERE Product_code = %s
        """
        valores = (
            codigo,
            nombre,
            categoria,
            precio_compra,
            precio_venta,
            codigo
            )

        cursor = conexion.cursor()
        cursor.execute(sql, valores)
        conexion.commit()
        return redirect(url_for("productos"))
    
    return render_template("editar_producto.html")

@app.route("/eliminar_productos")
def eliminar_productos():
    return render_template("eliminar_productos.html")

@app.route("/consultar_inventarios")
def consultar_inventarios():
    return render_template("consultar_inventarios.html")

@app.route("/mesas")
def mesas():
    return render_template("mesas.html")

@app.route("/piso1")
def piso1():
    estados_mesas = {}
    for numero in range(1,8):
        clave_pedido = f"pedido_PISO 1_{numero}"
        pedido = session.get(clave_pedido,[])

        estados_mesas[str(numero)] = "ocupada" if pedido else "disponible"

    return render_template(
        "piso1.html",
        estados_mesas=estados_mesas
        )

@app.route("/piso2")
def piso2():
    estados_mesas = {}
    for numero in range(8,23):
        clave_pedido = f"pedido_PISO 2_{numero}"
        pedido = session.get(clave_pedido,[])
    
        estados_mesas[str(numero)] = "ocupada" if pedido else "disponible"
    
    return render_template(
            "piso2.html",
            estados_mesas=estados_mesas
            )

@app.route("/piso3")
def piso3():
    estados_mesas = {}
    for numero in range(23,30):
        clave_pedido = f"pedido_PISO 3_{numero}"
        pedido = session.get(clave_pedido,[])
    
        estados_mesas[str(numero)] = "ocupada" if pedido else "disponible"
    
    return render_template(
            "piso3.html",
            estados_mesas=estados_mesas
            )

@app.route("/piso4")
def piso4():
    estados_mesas = {}
    for numero in range(30,41):
        clave_pedido = f"pedido_PISO 4_{numero}"
        pedido = session.get(clave_pedido,[])
    
        estados_mesas[str(numero)] = "ocupada" if pedido else "disponible"
    
    return render_template(
            "piso4.html",
            estados_mesas=estados_mesas
            )

@app.route("/rokola")
def rokola():
    estados_mesas = {}
    for numero in range(50,57):
        clave_pedido = f"pedido_ROKOLA_{numero}"
        pedido = session.get(clave_pedido,[])
    
        estados_mesas[str(numero)] = "ocupada" if pedido else "disponible"
    
    return render_template(
            "rokola.html",
            estados_mesas=estados_mesas
            )

@app.route("/pedido/<zona>/<mesa>", methods=["GET", "POST"])
def agregar_producto_venta(zona, mesa):
    cursor = conexion.cursor()

    # Cada mesa tendrá su propio pedido
    clave_pedido = f"pedido_{zona}_{mesa}"
    pedido = session.get(clave_pedido, [])

    clave_pendiente = f"pedido_pendiente_{zona}_{mesa}"
    pendientes = session.get(clave_pendiente, [])

    categoria_seleccionada = request.values.get("categoria", "")
    
#eliminar unidades que sigue pendientes de cocina
    if request.method == "POST" and request.form.get("eliminar_producto"):
        try:
            indice_eliminar = int(request.form.get("indice_eliminar"))

            if 0 <= indice_eliminar < len(pedido):
                articulo = pedido[indice_eliminar]
                articulo_pendiente_encontrado = None

                for articulo_pendiente in pendientes:
                    if(
                        articulo_pendiente["id"] == articulo["id"]
                        and articulo_pendiente.get("observaciones", "")
                        == articulo.get("observaciones", "")
                    ):
                        articulo_pendiente_encontrado = articulo_pendiente
                        break
                if articulo_pendiente_encontrado:
                    cantidad_a_quitar = min(
                        articulo["cantidad"],
                        articulo_pendiente_encontrado["cantidad"]
                    )

                    articulo["cantidad"] -= cantidad_a_quitar
                    articulo_pendiente_encontrado["cantidad"] -= cantidad_a_quitar

                    if articulo_pendiente_encontrado["cantidad"] <= 0:
                        pendientes.remove(articulo_pendiente_encontrado)

                    if articulo["cantidad"] <= 0:
                        pedido.pop(indice_eliminar)

                    session[clave_pedido] = pedido
                    session[clave_pendiente] = pendientes
                    session.modified = True

                    print("unidades pendientes eliminadas", cantidad_a_quitar)
                else:
                    print("producto enviado a cocina: requiere autorizacion.")
            else:
                print("Error: posicion fuera del pedido")
        except (ValueError, TypeError):
            print("Error: posicion no valida.")



    # Si se pulsa un producto, lo agregamos al pedido
    if request.method == "POST" and request.form.get("product_id"):
        try:
            cantidad = int(request.form.get("Cantidad", 1))
        except (ValueError, TypeError):
            cantidad = 0

        if cantidad > 0:
            id_producto = request.form.get("product_id")
            observaciones = request.form.get("observaciones", "").strip() 

            cursor.execute(
                """
                SELECT Id_product, name, Selling_price
                FROM products
                WHERE Id_product = %s
                """,
                (id_producto,)
            )
            producto = cursor.fetchone()

            if producto:
                encontrado = False

                for articulo in pedido:
                    if (
                        articulo["id"] == producto[0]
                        and articulo.get("observaciones", "") == observaciones
                    ):
                        articulo["cantidad"] += cantidad
                        encontrado = True
                        break

                if not encontrado:
                    pedido.append({
                        "id": producto[0],
                        "nombre": producto[1],
                        "precio": float(producto[2]),
                        "cantidad": cantidad,
                        "observaciones": observaciones
                    })

                #guardar el pedido completo de la mesa
                session[clave_pedido] = pedido

                #registrar las unidades nuevas para cocina
                pendiente_encontrado = False

                for articulo_pendiente in pendientes:
                    if (
                        articulo_pendiente["id"] == producto[0]
                        and articulo_pendiente.get("observaciones", "") == observaciones
                    ):
                        articulo_pendiente["cantidad"] += cantidad
                        pendiente_encontrado = True
                        break

                if not pendiente_encontrado:
                    pendientes.append({
                        "id": producto[0],
                        "nombre": producto[1],
                        "cantidad": cantidad,
                        "observaciones": observaciones
                    })
                session[clave_pendiente] = pendientes
                session.modified = True

    # Consultar las categorías
    cursor.execute(
        "SELECT * FROM category ORDER BY Id_Category"
    )
    categorias = cursor.fetchall()

    # Consultar los productos de la categoría elegida
    productos = []

    if categoria_seleccionada:
        cursor.execute(
            """
            SELECT Id_product, name, Selling_price
            FROM products
            WHERE Id_Categoria = %s
            ORDER BY name
            """,
            (categoria_seleccionada,)
        )
        productos = cursor.fetchall()

    cursor.close()

    # Calcular el total del pedido
    total = sum(
        articulo["precio"] * articulo["cantidad"]
        for articulo in pedido
    )

    return render_template(
        "agregar_producto_venta.html",
        zona=zona,
        mesa=mesa,
        categorias=categorias,
        productos=productos,
        categoria_seleccionada=categoria_seleccionada,
        pedido=pedido,
        total=total
    )
@app.route("/clientes")
def clientes():
    return render_template("clientes.html")

@app.route("/registrar_cliente")
def registrar_cliente():
    return render_template("registrar_cliente.html")

@app.route("/consultar_cliente")
def consultar_cliente():
    return render_template("consultar_cliente.html")

@app.route("/editar_cliente")
def editar_cliente():
    return render_template("editar_cliente.html")

@app.route("/eliminar_cliente")
def eliminar_cliente():
    return render_template("eliminar_cliente.html")

@app.route("/ventas")
def ventas():
    return render_template("ventas.html")

@app.route("/nueva_venta")
def nueva_venta():
    return render_template("nueva_venta.html")

@app.route("/consultar_ventas")
def consultar_ventas():
    return render_template("consultar_ventas.html")

@app.route("/anular_venta")
def anular_venta():
    return render_template("anular_venta.html")

@app.route("/ingresar", methods=["POST"])
def ingresar():
    usuario = request.form["usuario"]
    contraseña = request.form["contraseña"]

    return redirect(url_for("menu"))

from datetime import datetime

@app.route("/comanda/<zona>/<mesa>")
def comanda_cocina(zona,mesa):
    #recuperar el pedido de las mesa selecionada
    clave_pedido = f"pedido_{zona}_{mesa}"
    pedido = session.get(clave_pedido, [])
    #recuperar los productos pendientes de la mesa 
    clave_pendiente = f"pedido_pendiente_{zona}_{mesa}"
    pendientes = session.get(clave_pendiente, [])

    #evita generar una comanda vacia
    if not pendientes:
        return "No hay productos en el pedido de esta mesa.", 400
    cursor = conexion.cursor()

    #Agrupae los productos por caategoria 
    categorias = {}
    for articulo in pendientes:
        cursor.execute(
            """
            SELECT Id_Categoria
            FROM products
            WHERE Id_product = %s
            """,
            (articulo["id"],)
        )
        resultado = cursor.fetchone()
        if resultado:
            id_categoria = resultado[0]
            cursor.execute(
                """
                SELECT *
                FROM category
                WHERE Id_Category = %s
                """,
                (id_categoria,)
            )
            categoria = cursor.fetchone()
            nombre_categoria = (
                categoria[1] if categoria else "OTROS"
            )
            if nombre_categoria not in categorias:
                categorias[nombre_categoria] = []

            categorias[nombre_categoria].append({
                "nombre": articulo["nombre"],
                "cantidad": articulo["cantidad"],
                "observaciones": articulo.get("observaciones", "") 
            })

    cursor.close()

    ahora = datetime.now()
    comanda_html = render_template(
        "comanda_cocina.html",
        fecha=ahora.strftime("%d/%m/%Y"),
        hora=ahora.strftime("%I:%M %p"),
        mesa=mesa,
        zona=zona,
        numero_comanda=ahora.strftime("%Y%m%d%H%M%S"),
        categorias=categorias
    )
    #marca los productos pendientes como enviados
    session[clave_pendiente] = []
    session.modified = True

    return comanda_html
    

if __name__ == "__main__":
    app.run(debug=True)