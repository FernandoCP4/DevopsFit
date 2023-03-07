#Configurando Dockerfile
FROM python:3.9-slim-buster
WORKDIR /app
#Requerimientos del app
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt
#Copiando la aplicacion dentro del contenedor
COPY . .
#Exponiendo puerto indicado en el codigo
EXPOSE 5000
CMD ["python3","app.py"]

