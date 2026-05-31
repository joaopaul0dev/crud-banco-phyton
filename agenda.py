# 3. Escreva um programa para armazenar uma agenda de telefones em um dicionário.
# Cada pessoa pode ter um ou mais telefones e a chave do dicionário é o nome da
# pessoa.
agenda = {}

def adicionar():
    nome = input('\nDigite o nome do contato: ')
    telefones = []

    while True:
        nums = input('Insira o número (Ou aperte Enter sem digitar nada para parar): ')
        if nums == '':
            break
        telefones.append(nums)

    if telefones:
        agenda[nome] = telefones
        print(f'O contato {nome} foi salvo com sucesso! ')

continuar = 'sim'
while continuar.lower() == 'sim':
    adicionar()
    continuar = input('\nDeseja adicionar mais algum contato? (sim/não): ')

print('=== AGENDA DE CONTATOS ===')
if not agenda:
    print('Agenda vazia.')
else:
    for nomes, contato in agenda.items():
        telefonesBg = ", ".join(contato)
        print(f'{nomes} : {telefonesBg}')        