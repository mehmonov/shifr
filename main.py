from flask import Flask, request
from encryptor import Encryptor
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/encrypt")
def encrypt():
    key = request.args.get("key")
    text = request.args.get("text")
    encryptor = Encryptor(key)
    encrypted_text = encryptor.encrypt(text)
    return encrypted_text

@app.route("/decrypt")
def decrypt():
    key = request.args.get("key")
    encrypted_text = request.args.get("encrypted_text")
    encryptor = Encryptor(key)
    decrypted_text = encryptor.decrypt(encrypted_text.encode())
    return decrypted_text

if __name__ == "__main__":
    app.run()