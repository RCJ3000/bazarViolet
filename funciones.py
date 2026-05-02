def generar_codigo_qr(string_generador:str) -> None:
    import qrcode
    """
    PRE:String_generador tiene que estar definido.
    POST:Crea una imagen de código QR, respecto del string_generador recibido.
    """
    imagen:qrcode.make = qrcode.make(string_generador)
    imagen.save("qrcode.png")
    #generar_codigo_qr("https://wa.me/5491151465747?")

def agregar_productos_en_json() -> None:
    import json
    from collections import OrderedDict
    """
    PRE:nuevos_productos tiene que estar encerrado en corchetes y el archivo json
        tiene que estar en la misma carpeta que la función a usar o agregar ruta.
    POST:Agrega los nuevos productos al inicio del archivo productos.json.
    """
    # Diccionario de ejemplo de los Nuevos productos a insertar al inicio
    nuevos_productos_raw = [
        {
            "nombre": "Licuadora Kanji Home 2 en 1",
            "descripcion": "4 velocidades-600W",
            "precio": 47500.0,
            "imagen": "https://rcj3000.github.io/bazarViolet/im%C3%A1genes/LICUADORA-KANJI-HOME-3-VELOCIDADES-18PULGADAS.jpeg"
        },
        {
            "nombre": "Licuadora Yelmo",
            "descripcion": "1.5L - 750W",
            "precio": 83000.0,
            "imagen": "https://rcj3000.github.io/bazarViolet/im%C3%A1genes/LICUADORA-YELMO-CELESTE-3-EN-1-20PULGADAS.jpeg"
        },
        {
            "nombre": "Licuadora ULTRACOMB Profesional",
            "descripcion": "1.8L - 1200W",
            "precio": 110000.0,
            "imagen": "https://rcj3000.github.io/bazarViolet/im%C3%A1genes/LICUADORA-YELMO-CELESTE-3-EN-1-20PULGADAS.jpeg"
        }
    ]
    # Cargar productos existentes
    with open("productos.json", "r", encoding="utf-8") as f:
        productos_existentes_raw = json.load(f)
    # Combinar nuevos + existentes
    productos_combinados = nuevos_productos_raw + productos_existentes_raw
    # Reordenar cada producto con "id" primero
    productos_final = []
    for i, prod in enumerate(productos_combinados, start=1):
        ordenado = OrderedDict()
        ordenado["id"] = i
        for key in ["nombre", "descripcion", "precio", "imagen"]:
            ordenado[key] = prod[key]
        productos_final.append(ordenado)
    # Guardar el nuevo JSON
    with open("productos.json", "w", encoding="utf-8") as f:
        json.dump(productos_final, f, ensure_ascii=False, indent=4)
    print("✅ Productos actualizados con 'id' al inicio de cada sección.")

agregar_productos_en_json()


