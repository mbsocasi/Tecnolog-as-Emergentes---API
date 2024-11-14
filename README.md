# API de Productos

Esta API permite gestionar productos mediante operaciones CRUD, utilizando Flask y MySQL. La aplicación se ejecuta completamente en contenedores Docker, facilitando su despliegue y configuración.

## Requisitos

- Docker y Docker Compose instalados en el sistema.

## Configuración e Instalación

1. **Clonar el repositorio y navegar al directorio del proyecto:**
   - Docker Hub
      ```bash
      docker pull msbgod/api-productos
      docker run -it msbgod/api-productos bash
      ```
   - Git Hub
      ```bash
      git clone https://github.com/mbsocasi/Tecnolog-as-Emergentes---API.git
      ```
2. **Configurar el entorno**

   Crear un archivo `.env` en el directorio principal con las variables necesarias para conectar a la base de datos:

   ```makefile
   MYSQL_USER=user
   MYSQL_PASSWORD=password
   MYSQL_DB=productos_db
   MYSQL_HOST=db
   MYSQL_PORT=3306 
   ```

3. **Instalar las dependencias de Python:**
   ```bash
   pip install -r requirements.txt
   ```

## Ejecución del Proyecto
### 1. Iniciar los contenedores con Docker Compose:
```bash
docker-compose up -d
```
Esto levantará dos servicios:
-db: Contenedor MySQL configurado en el puerto 3307.
-api: Servidor Flask que ejecuta la API en el puerto 5000.
## Verificar que los servicios están activos:

- API disponible en: [http://localhost:5000](http://localhost:5000)
- Base de datos disponible en el puerto `3307` de localhost.

## Endpoints de la API

### 1. Listar Productos
- **Descripción**: Obtiene todos los productos registrados.
- **URL**: /productos
- **Método**: GET
- **Respuesta**:
- **Código**: 200 OK
- **Cuerpo**:
```json
[
{
"id": 1,
"nombre": "Producto1",
"precio": 100.0
},
...
]
```
### 2. Agregar Producto
- **Descripción**: Registra un nuevo producto en la base de datos.
- **URL**: /productos
- **Método**: POST
- **Cuerpo**:
```json
{
   "nombre": "Producto Nuevo",
   "precio": 150.0
}
```
- **Respuesta**:
- **Código**: 200 OK
- **Cuerpo**:
```json
   {
      "mensaje": "Producto agregado"
   }
```
         
### Ejemplo de Petición
```bash
curl -X POST http://localhost:5000/productos \
-H "Content-Type: application/json" \
-d '{"nombre": "Producto Nuevo", "precio": 150.0}'
```
      
## Estructura de Archivos

- **app.py:** Archivo principal de la API.
- **config.py:** Configuración de la aplicación Flask y la conexión a la base de datos.
- **models.py:** Funciones de base de datos para operaciones de productos.
- **docker-compose.yml:** Archivo de configuración para ejecutar los servicios en Docker.
- **requirements.txt:** Dependencias de Python requeridas para el proyecto.-

## Pruebas
Realiza pruebas utilizando herramientas como curl, Postman o cualquier cliente HTTP.
   
### 1. Agregar Producto
```bash
curl -X GET http://localhost:5000/productos
```

### 2. Prueba de Creación de Producto:
```bash
curl -X POST http://localhost:5000/productos \
-H "Content-Type: application/json" \
-d '{"nombre": "Producto Prueba", "precio": 200.0}'
```

## Detener el Proyecto

Para detener y remover los contenedores, utiliza:
```bash
docker-compose down
```
