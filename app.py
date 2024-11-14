from flask import Flask, request, jsonify
from config import create_app, get_db_connection

app = create_app()

@app.route('/productos', methods=['GET'])
def listar_productos():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM productos")
    productos = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(productos), 200

@app.route('/productos', methods=['POST'])
def agregar_producto():
    data = request.json
    if not data or 'nombre' not in data or 'precio' not in data:
        return jsonify({'error': 'Datos faltantes'}), 400

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO productos (nombre, precio) VALUES (%s, %s)", (data['nombre'], data['precio']))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({'mensaje': 'Producto agregado'}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)