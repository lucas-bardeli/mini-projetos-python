
import re

def cadastrar_usuario():
    nome = input("\nDigite o nome: ")
    idade = int(input("Digite a idade: "))
    email = valida_email()
    cpf = valida_cpf()
    senha = input("Crie uma senha: ")
    confirma_senha = valida_senha(senha)

    with open("usuarios.txt", "a") as arquivo:
        arquivo.write(f"{nome},{idade},{email},{cpf},{confirma_senha}\n")

    print("\nUsuário cadastrado com sucesso!")


def listar_usuarios():
    try:
        with open("usuarios.txt", "r") as arquivo:
            print("\nLista de usuários:")
            for linha in arquivo:
                nome, idade, email, cpf, senha = linha.strip().split(",")
                print(f"Nome: {nome}; Idade: {idade}; Email: {email}; CPF: {cpf}; Senha: {senha}")
    
    except FileNotFoundError:
        print("\nO arquivo não foi criado, nenhum usuário cadastrado ainda.")


def valida_email():
    while True:
        valida_email = input("Digite o email: ")

        if (re.search(r"^[a-zA-Z0-9.]+@[a-zA-Z0-9]+\.[a-zA-Z.]+$", valida_email)):
            break
        else:
            print("Email fora do padrão, digite novamente!")

    return valida_email


def valida_cpf():
    while True:
        valida_cpf = input("Digite o cpf: ")

        if (re.search(r"^[0-9]{3}\.[0-9]{3}\.[0-9]{3}\-[0-9]{2}$", valida_cpf)):
            break
        else:
            print("Cpf fora do formato correto, digite novamente!")
    
    return valida_cpf


def valida_senha(senha):
    while True:
        confirma_senha = input("Confirme a senha: ")

        if (confirma_senha != senha):
            print("Confirmação de senha incorreta, digite novamente!")
        else: 
            break

    return confirma_senha


while True:
    print("\nMenu:")
    print("1 - Cadastrar usuário;")
    print("2 - Listar usuários;")
    print("3 - Sair")
    opcao = int(input("---> "))

    match opcao:
        case 1:
            cadastrar_usuario()
    
        case 2:
            listar_usuarios()
    
        case 3:
            print("\nVocê saiu!")
            print()
            break
    
        case _:
            print("\nOpção inválida!")