import base64
import json
import hashlib
import hmac
from flask import Flask, render_template, request, abort, redirect
import Registro_de_usuarios

app = Flask(__name__, template_folder='template')
SECRET = ("secret")

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

    dbusername = ""
    dbhashpassword = ""
    attemps = 0

    if dbusername == username and dbhashpassword == hashResult:
        return {'message': 'Login Suscesfull'}
    elif dbusername != username and dbhashpassword != hashResult:
        attemps += 1
        if attemps == 3:
            return redirect('/')

    return ('/')

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
                'external_id': 'none',
                'email': email,
                'phone': phone,
                'username': username,
                'language': 'en-US',
                'create_user': 'python_script',
                'update_user': 'python_script',
                'password': hash_password,
                'intent': '1'
        }
        
        Registro_de_usuarios.create_User(user)
        return {'message': 'El usuario se registro correctamente'} 
    except Exception as e:
        return {'message': f'Error registering user: {e}'}, 500


if __name__ == '__main__':
    app.run(debug=True)

    
