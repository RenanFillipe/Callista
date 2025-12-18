import os, time
import json
import re

#na linha de baixo, a variavel arquivo vai Lê o arquivo
arquivo = open("db.json","r")#não sei se está correto, mas pesquisei melhor no chatgpt e ele disse que toda vez de inicio devo iniciar com "r" para ler o conteudo existente.
db = json.load(arquivo) #Traduz o JSON para python
arquivo.close()

usuarios = db["usuarios"]#antes essa variavel era (usuarios=[]), conforme informado no arquivo passado pelo Marcelo, ele vai ser (usuarios=db["usuarios"])
id_usuario = max([u['id'] for u in usuarios], default=0) #antes tava id_usuarios = 0, chatgpt recomendou usar essa nova forma pois se no arquivo db.json ja tiver usuarios cadastrados, o contador vai resear pra 0 toda vez que rodar o programa, e vai duplicar o id

#Função para validar email
def validar_email_regex(validar_email):
    # Regex para formato comum de email
    regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(regex, validar_email):
        return True
    return False

def registrar_usuario():
    global id_usuario
    user_id = id_usuario + 1

    nome = str(input('Nome: '))
    #validar email
    while True:
        email = str(input('Email: '))
        if validar_email_regex(email):
            break
        else:
            print("ERRO!, esse email é inválido, sigo o exemplo que de ser a seguir:")
            print("exemplo@domínio_de_email.com")
            time.sleep(2.0) 
            
    #validar senha
    while True:            
        senha = str(input('Senha: '))
        erros = []#vai armazenar regras de senhas que não foram atendidas

        if len(senha) < 8:
            erros.append("A senha deve ter pelo menos 8 caracteres.")

        if not any(c.isupper() for c in senha): # esses laços que estão dentro, servem pra percorrer se possuem mais de um erro de validação
            erros.append("A senha deve ter pelo menos uma letra maiúscula.")

        if not any(c.isdigit() for c in senha):
            erros.append("A senha deve ter pelo menos um número.")

        if not any(c in "!@#$%^&*()-_+=<>?/.,:;" for c in senha):
            erros.append("A senha deve ter pelo menos um símbolo.")

        if erros:
            print("Senha inválida:")
            for erro in erros:
                print("-", erro)
        else:
            break

    novo_usuario = {
        'id': user_id,
        'nome': nome,
        'email': email,
        'senha': senha
    }
    usuarios.append(novo_usuario)
    id_usuario += 1
    
    #A partir daqui, ele vai salvar os dados dentro do db.json
    arquivo = open("db.json", "w") 
    json.dump(db, arquivo, indent=4)
    arquivo.close()

    print('USUÁRIO REGISTRADO COM SUCESSO!')
    time.sleep(1.5)
    os.system('clear')

def todos_usuarios():

    arquivo = open("db.json", "r") # verifica se existe algum usuário no db.json, para entrar em umas das condições a seguir
    db = json.load(arquivo)
    arquivo.close()
    usuarios = db["usuarios"]

    if not usuarios:  # verifica se a lista está vazia
        print('A LISTA ESTÁ VAZIA') 
        time.sleep(1.4)
        os.system('clear')
    else:
        #função nova, agora o usuário pode escrever o que quer deseja buscar.
        while True:
            buscar = str(input("Deseja buscar por qual campo?[nome][email][senha]:"))
            buscar_em_minusculo = buscar.lower()
            if buscar_em_minusculo not in ("nome","email","senha"):
                print(f'ERRO!, o valor {buscar_em_minusculo} não existe dentro do campo usuário, verifique-se se digitou correto.')
                continue
            else:
                if buscar_em_minusculo == "nome":
                    print("-" * 25)
                    for usuario in usuarios:
                        print(f"id:{usuario["id"]}-nome:{usuario["nome"]}")
                        print("-" * 25)
                elif buscar_em_minusculo == "email":
                    print("-" * 45)
                    for usuario in usuarios:
                        print(f"id:{usuario["id"]}-nome:{usuario["nome"]}-email:{usuario["email"]}")
                        print("-" * 45)
                elif buscar_em_minusculo == "senha":
                    print("-" * 65)
                    for usuario in usuarios:
                        print(f"id:{usuario["id"]}-nome:{usuario["nome"]}-email:{usuario["email"]}-senha:{usuario["senha"]}")
                        print("-" * 60)
            
            print()#pulando liinha
            resposta = str(input("Deseja continuar?[S/N]:"))
            if resposta in 'Nn':
                print("Saindo na busca de usuários!")
                time.sleep(1.5)
                os.system('clear')
                break        

def procurando_usuario(user_id=None): 

    arquivo = open("db.json", "r")
    db = json.load(arquivo)
    arquivo.close()

    usuarios = db["usuarios"]
    
    if user_id is None:
        printa = True
        user_id = int(input('Informe o id do usuário: '))
    else:
        printa = False
    for usuario in usuarios:
        if usuario['id'] == user_id:
            if printa:
                print(usuario) # está linha é o que faz a função exibir_demanda() apresenta as informações dos usuarios cadastrado, como se eu quisesse consultar o usuário
            return usuario
        arquivo.close()
    else:
        print('ERRO! O USUÁRIO NÃO FOI ENCONTRADO.')
        time.sleep(1.4)
        os.system('clear')
        return None

def alterando_dados():

    for usuario in usuarios:
        print(usuario)

    user_id = int(input('Infome o id do usuário para alterar os dados:'))
    for usuario in usuarios:
        if usuario['id'] == user_id:
                usuario['nome'] = input("Digite o novo nome:")

                while True:
                    usuario['email'] = input("Digite o novo email:")
                    if validar_email_regex(usuario['email']):
                        break
                    else:
                        print("ERRO!, esse email é inválido, sigo o exemplo que de ser a seguir:")
                        print("exemplo@domínio_de_email.com")
                        time.sleep(2.0) 

                #Aplicando a mesma regra de validação de senha aqui
                while True:            
                    erros = []#vai armazenar regras de senhas que não foram atendidas
                    usuario['senha'] = input("Digite a nova senha:")
                    if len(usuario['senha']) < 8:
                        erros.append("A senha deve ter pelo menos 8 caracteres.")

                    if not any(c.isupper() for c in usuario['senha']): # esses laços que estão dentro, servem pra percorrer se possuem mais de um erro de validação
                        erros.append("A senha deve ter pelo menos uma letra maiúscula.")

                    if not any(c.isdigit() for c in usuario['senha']):
                        erros.append("A senha deve ter pelo menos um número.")

                    if not any(c in "!@#$%^&*()-_+=<>?/.,:;" for c in usuario['senha']):
                        erros.append("A senha deve ter pelo menos um símbolo.")

                    if erros:
                        print("Senha inválida:")
                        for erro in erros:
                            print("-", erro)
                    else:
                        break
                
                arquivo = open("db.json", "w") 
                json.dump(db, arquivo, indent=4)
                arquivo.close()

                print(f'ALTERAÇÃO NO USUARIO DO ID({user_id}) FOI REALIZADA COM SUCESSO!')
                time.sleep(1.5)
                os.system('clear')
                break
    
    else:
        print('ERRO! NÃO FOI POSSIVEL ALTERAR O USUÁRIO')
        time.sleep(1.5)
        os.system('clear')

def excluir_usuario(): #(NOTA SUGESTÃO), essa permição só deve ser válida para o criador do programa, mas disponibilizar para o usuário se eles deseja excluir a sua propria conta. perguntando o id e perguntar se ele realmente deseja excluir sua conta.
    for usuario in usuarios:
        print(usuario)
        
    user_id = int(input('Informe o id do usuário para excluir:'))
    for usuario in usuarios:
        if usuario['id'] == user_id:
            usuarios.remove(usuario)

            #abre o arquivo do json
            arquivo = open("db.json", "w") 
            json.dump(db, arquivo, indent=4)
            arquivo.close()

            print('USUÁRIO EXCLUIDO COM SUCESSO')
            time.sleep(1.4)
            os.system('clear')
            break
    else:
        print("ERRO! USUÁRIO NÃO ENCONTRADO PARA EXCLUSÃO.")
        time.sleep(1.4)
        os.system('clear')

