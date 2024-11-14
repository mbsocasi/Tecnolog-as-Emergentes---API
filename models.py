from config import mysql

def create_product(data):
    conn = mysql.connection
    cursor = conn.cursor()
    query = "INSERT INTO productos (nombre, precio) VALUES (%s, %s)"
    cursor.execute(query, (data['nombre'], data['precio']))
    conn.commit()
    cursor.close()

def get_all_products():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM productos")
    products = cursor.fetchall()
    cursor.close()
    return products
