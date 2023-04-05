import base64
import json
import hashlib
import hmac
from flask import Flask, render_template, request, abort
import sys

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
        print("Login Suscesfull")
    elif dbusername != username and dbhashpassword != hashResult:
        attemps += 1
        if attemps == 3:
            print("login Unsucesfull")

    return ('/')

if __name__ == '__main__':
    app.run(debug=True)

    
