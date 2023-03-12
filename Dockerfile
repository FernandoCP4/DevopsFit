#Configurando Dockerfile
FROM python:3.9-slim-buster
#Directorio de trabajo
WORKDIR /app
#Copiando la aplicacion dentro del contenedor
COPY requirements.txt requirements.txt
#Requerimientos del app
RUN pip install -r requirements.txt
#Exponiendo puerto indicado en el codigo
COPY . /app 
EXPOSE 5000
ENV FLASK_APP=app.py
CMD ["flask", "run", "--host=0.0.0.0"]

