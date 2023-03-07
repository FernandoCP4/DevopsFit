from flask import Flask, request, jsonify

#Creando app con Flask
app = Flask(__name__)

#API Key 
API_KEY = '2f5ae96c-b558-4c7b-a590-a501ae1c3f6c'

#Creando ruta /DevOps para method POST
@app.route('/DevOps', methods=['POST'])
def send_message():
    #Validacion de API
    api_key = request.headers.get('APIKey')
    if api_key != API_KEY:
        return 'Unauthorized', 401
    
    payload = request.json
    
    #Extrayendo la informacion necesaria
    message = payload['message']
    to = payload['to']
    from_name = payload['from']
    ttl = payload['timeToLifeSec']
    
    #Respuesta al payload ingresado, considerando al usuario indicado en "to"
    response_payload = {
        "message": f"Hello {to} your message will be send"
    }
    
    #Usando jsonify para la serializacion de informacion en la respuesta
    return jsonify(response_payload)

#Creando ruta /DevOps que devuelva ERROR para otros methods
@app.route('/DevOps', methods=['GET', 'PUT', 'PATCH', 'DELETE'])
def error():
    return 'ERROR'

#Iniciando servidor
if __name__ == '__main__':
    app.run(debug=True)