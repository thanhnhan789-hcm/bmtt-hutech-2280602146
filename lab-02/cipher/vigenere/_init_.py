from .vigenere_cipher import VigenerCipher
vigenere_cipher = VigenerCipher()
@app.route('/api/vigenere/encrypt', methods=['POST'])
def vigenere_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = data['key']
    encrypted_text = vigenere_cipher.vigenere_encrypt(plain_text,key)
    return jsonify({'encrypted_text': encrypted_text})
@app.route('/api/vigenere/decrypt', methods=['POST'] )    
def vigenere_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = data['key']
    decrypted_text = vigenere_cipher.vigenere_decrypt(cipher_text,key)
    return jsonify({'decrypted_text': decrypted_text})