import hashlib
import hmac
import base64
from flask import Flask, render_template, request, abort
import Registro_de_usuarios

app = Flask(__name__, template_folder='template')

SECRET_KEY = b'grupo_1'

@app.route('/')
def home():
    return render_template('home.html')

def check_hmac(data, hmac_header):
    digest = hmac.new(SECRET_KEY.encode('utf-8'), data, digestmod=hashlib.sha256).digest()
    compute_hmac = base64.b64encode(digest)

    return hmac.compare_digest(compute_hmac, hmac_header.encode('utf-8'))

@app.route('/hmac', methods=['POST'])
def handle_hmac():
    data = request.get_data()
    hmac=request.headers.get('Hmac-SHA256')
 
    hmacgerenerate = data.encode("utf-8")
    m = hashlib.sha256()
    m.update(hmacgerenerate)
    hashResult = m.digest()

    if hashResult!=hmac:
        abort(401)

@app.route('/register_user_route', methods=['POST', 'GET'])
def register_user():
    try:

        data = request.get_json()
        email = data['email']
        phone = data['phone']
        password = data['password']
        
        password_bytes = password.encode('utf-8')
        hmac_key = hmac.new(SECRET_KEY, password_bytes, hashlib.sha256).digest()
        hashed_password = hmac.new(hmac_key, password_bytes, hashlib.sha256).digest()
        hashed_password_base64 = base64.b64encode(hashed_password).decode('utf-8')
        
        user = {
            'external_id': 'none',
            'email': email,
            'phone': phone,
            'language': 'en-US',
            'create_user': 'python_script',
            'update_user': 'python_script',
            'password': hashed_password_base64,
            'intent': '1'
        }
        
        Registro_de_usuarios.create_User(user)
        return {'message': 'El usuario se registro correctamente'}
    except Exception as e:
        return {'message': f'Error registering user: {e}'}, 500

if __name__ == '__main__':
    app.run(debug=True)