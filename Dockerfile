# Utilizar una imagen base de Python
FROM python:3.9-slim

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar el código fuente al contenedor
COPY . .

# Instalar dependencias directamente usando pip
RUN pip install --no-cache-dir flask flask-restful mysql-connector-python pandas python-dateutil tzdata python-dotenv

# Exponer el puerto en el que Flask se ejecutará
EXPOSE 5000

# Comando para ejecutar la aplicación
CMD ["python", "app.py"]
