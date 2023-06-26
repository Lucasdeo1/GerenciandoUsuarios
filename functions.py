def perguntar ():
    return input('O que deseja realizar?\n'+
           'I - Inserir;\n'+
           'P - Pesquisar;\n'+
           'E - Excluir;\n' +
           'L - Listar um usuario;\n').upper() # qualquer letra digitada seja minusculas mas que seja de acordo com as opcao sera maiuscula

def inserir (dicionario):
    dicionario[input('Digite o login: ').upper()] = [
                                                    input('Digite o nome: ').upper(),
                                                    input('Digite a útima data de acesso: ').upper(),
                                                    input('Digite a última estação acessada: ').upper()
    ]
    salvar(dicionario)

def salvar ( dicionario ):
    with open ('bd.txt', 'a') as arquivo:
        for chave, valor in dicionario.items():
            arquivo.write(chave + ':' + str(valor))


def pesquisar(dicionario):
    b = input('Digite o nome buscado: ').upper()

    for chave, valor in dicionario.items():
        if b.upper() == valor[0]:
            print('Nome:', valor[0])
            print('Data de último acesso:', valor[1])
            print('Última estação acessada:', valor[2])

def excluir(dicionario):
    d = input('Digite o nome do usuário a ser excluído: ').upper()

    if d in dicionario:
        del dicionario[d]
        print('Usuário removido com sucesso.')
        salvar(dicionario)
    else:
        print('Usuário não encontrado.')

