# Indicamos la versión de python que utiliza el proyecto
FROM python:3.10

# Indicamos la carpeta donde estará el contenedor
WORKDIR /app
# Copiamos el archivo local de las dependencias (izquierda) hacia el nuevo archivo del contenedor (derecha)
COPY requirements.txt /app/requirements.txt

# Instalamos las dependencias
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

# Copia todo el codigo en la carpeta app
COPY . app/

# Comando para mantener en ejecución el contendor
CMD bash -c "while true; do sleep 1; done"