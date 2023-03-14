import json
import hashlib
from flask import Flask, render_template, request
import sys

app = Flask(__name__, template_folder='template')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/ProcessUserInfo/<string:userInfo>', methods=['POST'])
def ProcessUserInfo(userInfo):
    userInfo=json.loads(userInfo)
    username = userInfo['username']
    appPassword = userInfo['password']
    passHash = appPassword.encode("utf-8")
    m = hashlib.sha256()
    m.update(passHash)
    hashResult = m.digest()
    print(username)
    print()
    print(appPassword)
    print()
    print(hashResult)

    return ('/')

if __name__ == '__main__':
    app.run(debug=True)

    
