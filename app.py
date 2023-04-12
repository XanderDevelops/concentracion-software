import base64
import json
import hashlib
import hmac
from flask import Flask, render_template, request, abort, redirect
import Registro_de_usuarios

app = Flask(__name__, template_folder='template')
SECRET = ("secret")
max_attemps = 3
attempsIpMap = {}

def check_hmac(data, hmac_header):
    digest = hmac.new(SECRET.encode('utf-8'), data, digestmod=hashlib.sha256).digest()
    compute_hmac = base64.b64encode(digest)

    return hmac.compare_digest(compute_hmac, hmac_header.encode('utf-8'))

@app.route('/')
def home():
    return render_template('home.html')


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


@app.route('/ProcessUserInfo/<string:userInfo>', methods=['POST'])
def ProcessUserInfo(userInfo):

    userInfo=json.loads(userInfo)

    username = userInfo['username']
    appPassword = userInfo['password']

    passHash = appPassword.encode("utf-8")
    m = hashlib.sha256()
    m.update(passHash)
    hashResult = m.digest()
    
    dbhashpassword = Registro_de_usuarios.get_password(username)
    status = Registro_de_usuarios.get_status(username)

    ip_add = request.remote_addr
    attemps = attempsIpMap.get(ip_add, 0)

    if attemps >= max_attemps:
        status = 1
        return 429, {'message': 'Login Unsuscesfull'}
        
    if hashResult != dbhashpassword:
        attempsIpMap[ip_add] = attemps + 1
        return 401
    else:
        attempsIpMap.pop(ip_add, None)
        return render_template("student.html"), {'message': 'Login Suscesfull'}


@app.route('/RegisterUserInfo/<string:signInfo>', methods=['POST'])
def RegisterUserInfo(signInfo):

    signInfo = json.loads(signInfo)

    email = signInfo['email']
    phone = signInfo['phone']
    username = signInfo['usernameR']
    password = signInfo['passwordR']
    password_hash = password.encode("utf-8")
    p = hashlib.sha256()
    p.update(password_hash)
    hash_password = p.digest()

    try:
        user = {
                'email': email,                
                'username': username,
                'phone': phone,
                'language': 'en-US',
                'create_user': 'python_script',
                'update_user': 'python_script',
                'password': hash_password,
                'intent': '1',
                'estado': '0'
        }
        
        Registro_de_usuarios.create_User(user)
        return {'message': 'El usuario se registro correctamente'} 
    except Exception as e:
        return {'message': f'Error registering user: {e}'}, 500

if __name__ == '__main__':
    app.run(debug=True)

    
