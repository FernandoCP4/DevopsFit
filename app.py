from flask import Flask, request, jsonify
import jwt
from functools import wraps

#API Key 
API_KEY = '2f5ae96c-b558-4c7b-a590-a501ae1c3f6c'

#Creando app con Flask
app = Flask(__name__)

#Creando secret key para acceso y verificacion
SECRET_KEY = '-----BEGIN PRIVATE KEY-----\nMIIEuwIBADANBgkqhkiG9w0BAQEFAASCBKUwggShAgEAAoIBAQDaL8wWN4WikrJy\nkRVRIt5ezYqdO3QbkdctIeZCrJfKi7fTSxBiVNsKXm1iUW1B0+AJ5PDnOx+/hBuy\n37RBEiyOuFQq04+uletVuHfeBLk8kWidXyj9sdtXTFds4SaAKE+1yxkwRUCE4n9b\nflnfLlfASplt4CH4VAfQQNa35Q9ygyT9InFODWLnZ+OxER392lFrBgool5xSdiYb\ni31gs+fntSUjS9dbao05yHhCtyArzOCZt7EzQsH1PdsljB1i0x61PahaN3ncmwu6\nAoaUZhHtEdBC7QnXMJZFiUv/o0nO42NAqe4YCj4Flj4Rah+i/rcYXd5pCuuM+w4q\nTCk0ZuhXAgMBAAECgf9KAZcNR3KMh4r/pou/JD9I6MRGO2RRSvvcKHjHJMOtGrcU\nyYvvzoMoK99DpLA/znNaPSLOoRSjtquugIfONTE9N53/k22o9NuzYl6bb/66DJhE\nyNeeiuAF5wnAZJ4qhNcvUom4qxoMo3GPbHa6EiixkJwk02FdBHj3VQbVBAe5TyHY\nVu2ykCey4ijcy8oN0U8YsbLqGVnrZllbyDwv9bPlAVwJmqp8qDuImEj6W8rBwcIU\nmg+8yw6lAlMMhI6RU5g/j6TRKSXaHkIcLG+GTC1a4MJpxMFpBeA6tcHWGSTSQ523\n04O6n3gh03hAuJD2/RRo8n9++QWsdjGt/XXDclECgYEA+VnuKGOmeEh99ycxCHJG\nwoYR2XnVbQY1WnfSJQ82D3sopSMVQMgIUiN7qVWCvvQ3uZgJ0JZeqxpc41qoLFZv\n9FKldgVjTy9nRyjKDLf7NxCN+9cS4uUNhHltJBebpEm/TYDbZBL1sQGf6WopTJVV\nqX8j+eofCns6v2mNpRiviNECgYEA4AEjQ2a91LhZ4X60ZZaQCAXdsxCk5wNIW1av\nPd/nUjhXqp+Flsxpcgx9fxxxftmWlQ9b5Ia3fT3wSqlzmVVz4mzx8VbhC67f6Tzo\nP8mMp80ew1kZCmk1Y5o6qP+M3Uf98XDeEXkgveQivo4fdCn/ZtWVjqy0TTqU911v\n+kVEKKcCgYAP0uwxNfm3gmo0CBGthosFBzsUwQ2RSKaUIix825VDsD4pFKvhm5Aj\nnkrXuSx978OljId67D//vcGNUBCCF84tBB2p+reNq+Vy95yy5+4SVYOdKs3xBjYw\nZQBPHQxshZ2VTosds7JR1FeQmYMbcBKqmf3vezMTGDTnNsydYI6rMQKBgGJ3HZEb\nMIa5IolEsPeW32knavSzdEk34C6GRDHmokA6FA8kYAyRfihr5R5i2mDwNIkBX1ts\n/GtJNr8bDX1xWqdFTHTRw8rm6/YSl+SyK+n2+HbWS3OQG6/Us8Rl0P3UD4R6IKN9\noy7VgZBR2PGvJF2HtV4p/HeWMLUrlXVlzTgxAoGBAJc0t0HJphQ+YWN8L4CkcalP\nLQon/6Ui4Bja1qXBb0kqyrj+jIftpQuxFSv3iYZUmkYrKP+vhMdrCMceyHLcGYxg\n/cY4fTzQbyUqWUUpu1aBYtMLi/j1TXBXJ07xzxQsLZdpYFy9wsTqWFUGYVEw3mMD\nw6pYaJGQyzX7GpmoH1PM\n-----END PRIVATE KEY-----\n'

#Funció que toma el user_id como input y genera un JWT con el ID como payload 
def generate_token(user_id):
    payload = {'user_id': user_id}
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    return token.decode('utf-8')

#Función para verificar el JWT y verificándola usando la secret key
def verify_token(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return payload['user_id']
    except jwt.exceptions.DecodeError:
        return None

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

#Creando authenticador con decorador authenticate
def authenticate(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return 'Unauthorized', 401
        user_id = verify_token(token)
        if not user_id:
            return 'Unauthorized', 401
        return func(user_id, *args, **kwargs)
    return wrapper

@app.route('/protected')
@authenticate
def protected_route(user_id):
    return f'Hello, user {user_id}!'

#Iniciando servidor
if __name__ == '__main__':
    app.run(debug=True)