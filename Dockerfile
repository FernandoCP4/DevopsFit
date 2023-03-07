#Configurando Dockerfile
FROM python:3.8-slim-buster
#Directorio de trabajo
WORKDIR /app
#Copiando la aplicacion dentro del contenedor
COPY . /app
#Requerimientos del app
RUN pip3 install -r requirements.txt
#Exponiendo puerto indicado en el codigo
EXPOSE 5000
CMD ["python","app.py"]

