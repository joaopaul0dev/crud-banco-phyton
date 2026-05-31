dicionario = {}

def gerarNovaPessoa():
    nome = input('Digite o nome:')
    idade = input('Digite a idade: ')

    while nome == '' or idade == '':
        print('nome ou idade não podem estar vazios.')
        nome = input('Digite o nome:')
        idade = input('Digite a idade: ')

    dicionario[nome] = idade
    print(f'{nome} foi adicionado com sucesso"!')

continuar = 's'
while continuar == 's':    
    gerarNovaPessoa()
    continuar = input('deseja continuar? (s/n)')

ordenado = sorted(dicionario.items(), key=lambda item: item[1])

print('LISTA DE NOMES POR IDADE')
for nome, idade in ordenado:
    print(f'{nome} | {idade}')