from dicionary.functions import *

usuarios = {}

op = perguntar()
while op == 'I' or op == 'P' or op == 'E' or op == 'L':
    if op == 'I':
        inserir(usuarios)
    elif op == 'P':
        pesquisar(usuarios)
        #print(usuarios)
    elif op == 'E':
        excluir(usuarios)
    elif op == 'L':
        print(usuarios)
    op = perguntar()
