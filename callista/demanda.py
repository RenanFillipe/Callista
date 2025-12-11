from .usuario import procurando_usuario, usuarios
import os, time
import json

#lendo o arquivo do json na parte de demandas
def ler_db():
    arquivo = open("db.json", "r")
    db = json.load(arquivo)
    arquivo.close()
    return db

db = ler_db()
demandas = db["demandas"]
id_demanda = 0

def registrar_demandas():
    global usuarios
    db = ler_db()
    
    if not usuarios:
        print("NÃO É POSSIVEL REGISTRAR A DEMANDA COM NENHUM USÚARIO.")
        time.sleep(3)
        os.system('clear')
        return
    elif len(usuarios) == 1: #verificar se dentro da lista usuario tem apenas um usuario
        print("NÃO É POSSIVEL REGISTRA A DEMANDA COM APENAS 1 (UM) USÚARIO")
        time.sleep(3)
        os.system('clear')
        return
    else:
        demandas = db["demandas"]
        id_demandas = int(input('id da demanda:'))
        
        #Entra em um loop infinito se o id que o usuário registra for menor ou igual a zero
        while id_demandas <= 0:
            id_demandas = int(input("Digite um ID válido, que não seja menor ou igual a 0(zero):")) 

        #verifica se tem algum id existente da demanda, caso o usuário registre um id que já.
        #se não existise esse comando da linha 41 até 46, iri criar uma nova demanda, com os mesmos ID.
        for id_demanda in demandas:
            if id_demanda['id'] == id_demandas:
                id_demandas = int(input('ERRO, esse id já existe, escreva um novo ID:'))
                continue
            else:
                break

        texto = str(input('Texto:'))
        origem = str(input('Origem do texto:'))
        data_chegada = str(input('Data texto(31/12/2025):'))

    while True:
        # Apresenta uma lista de dicionarios de todos os usuários, para que a pessoa possa saber qual id do usuário ela quer selecionar
        lista_usuarios = db["usuarios"]

        for usuario in lista_usuarios:
            print(usuario)
        # Cria uma lista "ids" contendo todos os ids cadastrados no sistema
        ids = [usuario["id"] for usuario in usuarios]
    
        # Pede o id do relator
        id_relator = int(input('Informe o id do usuário que vai ser o relator:'))
        # Enquanto o id informado não estiver na lista de ids, informa o erro e pede de novo
        while id_relator not in ids:
            print('Esse id de usuário não existe.')
            id_relator = int(input('Informe o id do usuário que vai ser o relator:'))
        
        # Pede o id do revisor
        id_revisor = int(input('Informe o id do usuário que vai ser o revisor:'))
        # Enquanto o id informado não estiver na lista de ids, informa o erro e pede de novo
        while id_revisor not in ids:
            print('Esse id de usuário não existe.')
            id_revisor = int(input('Informe o id do usuário que vai ser o revisor:'))

        if id_relator == id_revisor:
            print('ERRO! O RELATOR NÃO PODE SER AO MESMO TEMPO O REVISOR, ASSIM COMO O REVISOR NÃO PODE SER O RELATOR')
        else:
            break
    status = 'pendente de resposta'
    nova_demanda = {
        'id': id_demandas,
        'texto': texto,
        'origem': origem,
        'data_chegada': data_chegada,
        'id_relator': id_relator,
        'id_revisor': id_revisor,
        'status': status
    }
    db["demandas"].append(nova_demanda)

    arquivo = open("db.json", "w")
    json.dump(db, arquivo, indent=4)
    arquivo.close()

    #registrando a demanda no arquivo 
    print('DEMANDA REGISTRADA COM SUCESSO!')
    time.sleep(3)
    os.system('clear')

def exibir_demandas(): #GERANDO BASTANTE PROBLEMAS, DEVIDO O FATO DE PEGAR A FUNÇÃO procurando_usuario

    arquivo = open("db.json", "r")
    db = json.load(arquivo)
    #fechar o arquivo aqui
    demandas = db["demandas"]

    if not demandas:
        arquivo.close()
        print('ERRO! NENHUMA DEMANDA FOI CADASTRADA')
        time.sleep(3)
        os.system('clear')
        return
    for demanda in demandas: #POR ALGUM MOTIVO, QUANDO ELE CHEGA NESSA LINHA, AO INVÉS DE APRESENTAR APENAS A DEMANDA, ELE APRESENTA TAMBÉM O OS USUARIOS QUE FAZ PARTE DESSA DEMANDA
        relator = procurando_usuario(demanda['id_relator']) #PODE SER QUE SEJA ESSAS DUAS LINHAS QUE ESTÃO FAZENDO ISSO
        revisor = procurando_usuario(demanda['id_revisor'])
        
        print("\n===== DEMANDA =====")
        print(f"ID DEMANDA: {demanda['id']}")
        print(f"TEXTO: {demanda['texto']}")
        print(f"ORIGEM DO TEXTO: {demanda['origem']}")
        print(f"DATA_TEXTO: {demanda['data_chegada']}")
        print(f"RELATOR: {relator['nome'] if relator else 'NÃO ENCONTRADO'}")
        print(f"REVISOR: {revisor['nome'] if relator else 'NÃO ENCONTRADO'}")
        print(f"STATUS: {demanda['status']}")
        print(f"=============================\n")
        arquivo.close()


def consultar_demandas():
    arquivo = open("db.json", "r")
    db = json.load(arquivo)
    demandas = db["demandas"]

    buscar_demanda = int(input("Informe o id pra procurar uma demanda:"))

    demanda_encontrada = None

    for demanda in demandas:
        if demanda['id'] == buscar_demanda:
            demanda_encontrada = demanda
            break

    
    if not demanda_encontrada:
        print("ERRO: demanda não existe ou foi excluída")
        arquivo.close()
        time.sleep(3)
        os.system('clear')
        return

    relator = procurando_usuario(demanda_encontrada['id_relator']) #PODE SER QUE SEJA ESSAS DUAS LINHAS QUE ESTÃO FAZENDO ISSO
    revisor = procurando_usuario(demanda_encontrada['id_revisor'])
        
    print("\n===== DEMANDA =====")
    print(f"ID DEMANDA: {demanda_encontrada['id']}")
    print(f"TEXTO: { demanda_encontrada['texto']}")
    print(f"ORIGEM DO TEXTO: {demanda_encontrada['origem']}")
    print(f"DATA_TEXTO: {demanda_encontrada['data_chegada']}")
    print(f"RELATOR: {relator['nome'] if relator else 'NÃO ENCONTRADO'}")
    print(f"REVISOR: {revisor['nome'] if relator else 'NÃO ENCONTRADO'}")
    print(f"STATUS: {demanda_encontrada['status']}")
    print(f"=============================\n")
    arquivo.close()

def alterar_demandas():
    arquivo = open("db.json", "r")
    db = json.load(arquivo)
    arquivo.close()
    demandas = db["demandas"]

    for demanda in demandas:
        relator = procurando_usuario(demanda['id_relator']) #PODE SER QUE SEJA ESSAS DUAS LINHAS QUE ESTÃO FAZENDO ISSO
        revisor = procurando_usuario(demanda['id_revisor'])
        print("===== DEMANDA =====")
        print(f"ID DEMANDA: {demanda['id']}")
        print(f"TEXTO: { demanda['texto']}")
        print(f"ORIGEM DO TEXTO: {demanda['origem']}")
        print(f"DATA_TEXTO: {demanda['data_chegada']}")
        print(f"RELATOR: {relator['nome'] if relator else 'NÃO ENCONTRADO'}")
        print(f"REVISOR: {revisor['nome'] if relator else 'NÃO ENCONTRADO'}")
        print(f"STATUS: {demanda['status']}")
        
    id_demanda = int(input("Informe o id da demanda para alteração:"))
    for demanda in demandas:
        if demanda['id'] == id_demanda:
            demanda['texto'] = input("Novo texto:")
            demanda['origem'] = input("Nova origem:")
            demanda['data_chegada'] = input("Nova data:")
            while True:

                lista_usuarios = db["usuarios"]

                for usuario in lista_usuarios:
                    print(usuario)
  
                ids = [usuario["id"] for usuario in lista_usuarios]
    
                # Pede o id do relator
                id_relator = int(input("Informe o id do novo relator:"))
                # Enquanto o id informado não estiver na lista de ids, informa o erro e pede de novo
                while id_relator not in ids:
                    print('Esse id de usuário não existe.')
                    id_relator = int(input('Informe o id do novo relator:'))

                demanda['id_relator'] = id_relator
                # Pede o id do revisor
                id_revisor = int(input("Informe o id do novo revisor:"))
                # Enquanto o id informado não estiver na lista de ids, informa o erro e pede de novo
                while id_revisor not in ids:
                    print('Esse id de usuário não existe.')
                    id_revisor = int(input("Informe o id do novo revisor:"))

                demanda['id_revisor'] = id_revisor

                if id_relator == id_revisor:
                    print('ERRO! O RELATOR NÃO PODE SER AO MESMO TEMPO O REVISOR, ASSIM COMO O REVISOR NÃO PODE SER O RELATOR')
                else:
                    break        
            
            arquivo = open("db.json", "w")
            json.dump(db, arquivo, indent=4)
            arquivo.close()

            print('DEMANDA ALTERADA COM SUCESSO!')
            time.sleep(3)
            os.system('clear')
            return
    
    print("ERRO, essa demanda não existe, digite o id corretamente.")  
    time.sleep(3)
    os.system('clear')

def excluir_demandas():
    db = ler_db()
    demandas = db['demandas']

    for demanda in demandas:
        relator = procurando_usuario(demanda['id_relator']) #PODE SER QUE SEJA ESSAS DUAS LINHAS QUE ESTÃO FAZENDO ISSO
        revisor = procurando_usuario(demanda['id_revisor'])
        print("===== DEMANDA =====")
        print(f"ID DEMANDA: {demanda['id']}")
        print(f"TEXTO: { demanda['texto']}")
        print(f"ORIGEM DO TEXTO: {demanda['origem']}")
        print(f"DATA_TEXTO: {demanda['data_chegada']}")
        print(f"RELATOR: {relator['nome'] if relator else 'NÃO ENCONTRADO'}")
        print(f"REVISOR: {revisor['nome'] if relator else 'NÃO ENCONTRADO'}")
        print(f"STATUS: {demanda['status']}")
        
    print("===================")
    id_demanda = int(input("Informe o id da demanda para excluir:"))
    for demanda in demandas:
        if demanda['id'] == id_demanda:
            demandas.remove(demanda)

            arquivo = open("db.json", "w")
            json.dump(db, arquivo, indent=4)
            arquivo.close()

            print("DEMANDA EXCLUIDA COM SUCESSO")
            time.sleep(1.4)
            os.system('clear')
            break
    else:
        print("ERRO! DEMANDA NÃO FOI ENCONTRADA PARA EXCLUSÃO")
        time.sleep(1.4)
        os.system('clear')
    