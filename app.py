import json
import hashlib
from flask import Flask, render_template

app = Flask(__name__, template_folder='template')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/ProcessUserInfo/<string:username>/<string:password>', methods=['POST'])
def ProcessUserInfo(username, password):
    appUsername = json.loads(username)
    appPassword = json.loads(password)
    passHash = appPassword.encode("utf-8")
    m = hashlib.sha256()
    m.update(passHash)
    hashResult = m.digest()
    print(hashResult)
    return ('/') 

if __name__ == '__main__':
    app.run()

    
