#Configurando Dockerfile
FROM python:3.8-slim-buster
#Directorio de trabajo
WORKDIR /app
#Copiando la aplicacion dentro del contenedor
COPY requirements.txt requirements.txt
#Requerimientos del app
RUN pip3 install -r requirements.txt
#Exponiendo puerto indicado en el codigo
COPY . .
EXPOSE 5000
CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]

