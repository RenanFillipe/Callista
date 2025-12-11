from .usuario import registrar_usuario, todos_usuarios, procurando_usuario, alterando_dados, excluir_usuario
from .demanda import registrar_demandas, exibir_demandas, consultar_demandas, alterar_demandas, excluir_demandas
import os, time

# para rodar: abrir terminal e escrever "python -m callista.main"

while True:
    escolha = input("""
=====
MENU
=====
(1) Criar usuário
(2) Apresentar todos os usuários
(3) Consultar usuário
(4) Alterar dados do usuário
(5) Excluir usuário
(6) Criar demanda
(7) Exibir demandas
(8) Consultar demandas                  
(9) Alterar demandas                   
(10) Excluir demandas
(0) Sair

Escolha uma das opções acima\n
""")

    if escolha == '0':
        break

    mapper = {
        '1': registrar_usuario,
        '2': todos_usuarios,
        '3': procurando_usuario,
        '4': alterando_dados,
        '5': excluir_usuario,
        '6': registrar_demandas,
        '7': exibir_demandas,
        '8': consultar_demandas,
        '9': alterar_demandas,
        '10': excluir_demandas
    }

    valor_resposta = mapper.get(escolha)
    if valor_resposta:
        valor_resposta()
    else:
        print('Valor errado, escolha um número valido no menu.')
        time.sleep(1.5)
        os.system('clear')
   