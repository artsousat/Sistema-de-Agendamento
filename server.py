#Importação da biblioteca Flask para criar o servidor web
from flask import Flask, request, send_from_directory

#Criação da váriavel flask
app = Flask(__name__)

#Rota para o index.html
@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

#Rota para os outros arquivos (CSS, JS.)
@app.route('/<filename>')
def static_files(filename):
    return send_from_directory('.', filename)

#Rota para o /login
@app.route('/login', methods=['POST'])
def login():
    nome = request.form.get('username')
    senha = request.form.get('password')

#Verificação se o nome e senha estão corretos
    if nome == 'admin' and senha == 'admin':
        return f'Bem-vindo, {nome}!'
    else:
        return 'Usuário ou senha incorretos!'

#Rodar o servidor
if __name__ == '__main__':
    app.run(port=5500)