def generar_codigo_qr(string_generador:str) -> None:
    import qrcode
    """
    PRE:String_generador tiene que estar definido.
    POST:Crea una imagen de código QR, respecto del string_generador recibido.
    """
    imagen:qrcode.make = qrcode.make(string_generador)
    imagen.save("qrcode.png")
    #generar_codigo_qr("https://wa.me/5491151465747?")

def agregar_productos_en_json(nuevos_productos:dict) -> None:
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
            "nombre": "Ventilador Oryx",
            "descripcion": "3 velocidades- 18 pulgadas",
            "precio": 65000.0,
            "imagen": "https://rcj3000.github.io/bazarViolet/im%C3%A1genes/VENTILADOR-ORIX-3-EN-1-18PULGADAS.jpeg"
        },
        {
            "nombre": "Ventilador Martin & Martin",
            "descripcion": "3 en 1 - 20 pulgadas",
            "precio": 92000.0,
            "imagen": "https://rcj3000.github.io/bazarViolet/im%C3%A1genes/VENTILADOR-MARTIN-&-MARTIN-3-EN-1-20PULAGADAS-PIE-PESADO.jpeg"
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


