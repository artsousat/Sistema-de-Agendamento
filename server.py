from flask import Flask, request, send_from_directory
import os

app = Flask(__name__)

# Servir arquivos estáticos como index.html e styles.css
@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/<path:filename>')
def static_files(filename):
    return send_from_directory('.', filename)

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    # Verificação simples (substitua por banco de dados real)
    if username == 'admin' and password == '1234':
        return 'Login bem-sucedido! Bem-vindo, ' + username
    else:
        return 'Usuário ou senha inválidos.'

if __name__ == '__main__':
    app.run(debug=True)