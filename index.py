import time
import os
import json
import re

padraohorario = r'^([01]\d|2[0-3]):([0-5]\d)$'
padraodata = r'^(0[1-9]|[12]\d|3[01])/(0[1-9]|1[0-2])$'

def login():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("---------------------------------------------------------------------")
    print("BEM VINDO AO SISTEMA DE AGENDAMENTO DA BARBEARIA - MARCELO BARBEIRO")
    print("---------------------------------------------------------------------")
    cad = input("Já possui cadastro? (s/n): ")
    if cad == "s":
        print("Para começar, nos informe os seguintes dados abaixo:")
        nome = input("\nDigite seu nome: ")
        senha = input("Digite sua senha: ")
        with open('usuarios.json', 'r') as f:
            usuarios = json.load(f)
            for usuario in usuarios:
                if nome == usuario['nome'] and senha == usuario['senha']:
                    print("Login bem-sucedido!")
                    time.sleep(1.5)
                    return nome, senha
            else:
                print("Nome ou senha incorretos. Por favor, tente novamente.")
                time.sleep(1.5)
                return login()
    elif cad == "n":
        print("Para criar um novo cadastro, nos informe os seguintes dados abaixo:")
        nome = input("\nDigite seu nome: ")
        senha = input("Digite sua senha: ")
        try:
            with open('usuarios.json', 'r') as f:
                usuarios = json.load(f)
        except:
            usuarios = []
        for usuario in usuarios:
            if nome == usuario['nome']:
                print("Este usuário já existe. Por favor, tente novamente.")
                time.sleep(1.5)
                return login()
        usuarios.append({'nome': nome, 'senha': senha})
        with open('usuarios.json', 'w') as f:
            json.dump(usuarios, f, indent=4)
        print("Cadastro criado com sucesso! Agora você pode fazer login.")
        time.sleep(1)
        return login()
    else:
        print("Opção inválida. Por favor, tente novamente.")
        time.sleep(2)
        return login()
def main():
    nome, senha = login()
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"Bem-vindo, {nome}!")
    time.sleep(1.5)
    print("\nO que gostaria de agendar hoje?")
    def agendar():
        escolhadia = input("\nDigite o dia que deseja agendar (ex: 25/12): ")
        escolhahorario = input("Para qual horário deseja agendar? (ex: 14:00): ")
        if not re.match(padraohorario, escolhahorario):
            print("Formato de horário inválido. Por favor, tente novamente.")
            time.sleep(1.5)
            print("--------------------------------------------------")
            return agendar()
        elif not re.match(padraodata, escolhadia):
            print("Formato de data inválido. Por favor, tente novamente.")
            time.sleep(1.5)
            print("--------------------------------------------------")
            return agendar()
        try:
            with open('agendamentos.json', 'r') as f:
                agendamentos = json.load(f)
        except:
            agendamentos = []
        for agendamento in agendamentos:
            if escolhadia == agendamento['dia'] and escolhahorario == agendamento['horario']:
                print("Este horário já está agendado. Por favor, escolha outro horário.")
                time.sleep(1)
                print("--------------------------------------------------")
                return agendar()
        agendamentos.append({'nome': nome, 'horario': escolhahorario, 'dia': escolhadia})
        with open('agendamentos.json', 'w') as f:
            json.dump(agendamentos, f, indent=4)
        print("Certinho", nome,"Agendamento para o dia", escolhadia, "às", escolhahorario, "realizado com sucesso!")
        time.sleep(1.5)
    agendar()
main()