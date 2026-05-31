# Desenvolva um sistema de banco em python. Você deve exibir 6 menus:

#     Criar nova conta. Uma nova conta deve conter ID, NOME e SALDO
#     Adicionar dinheiro a conta. Adiciona uma quantia (dita pelo usuário) a conta de um ID especifico, mostra quando ficou o saldo final.
#     Remover dinheiro da conta. Remove uma quantia (dita pelo usuário) a conta de um ID especifico, mostra quanto ficou o saldo final. Emitir um alerta caso o saldo tenha ficado negativo.
#     Mostrar saldo de um nome dado
#     Apagar uma conta (apaga todos os dados de um determinado ID)
#     Apagar todas as contas

# ps: lembre-se de tratar exceções, caso o menu selecionado, ID ou nome sugerido não exista imprimir uma alerta avisando que não existe.

banco = {}

def gerarConta():
    print('\n-- CADASTRO DA CONTA --')
    id = ''
    nome = ''
    saldo = -1

    while (nome == '' or id == '' or saldo < 0):
        print('\n [!] Todos os campos são obrigatórios, Preencha novamente: ')
        id = input('Digite o ID da conta: ').strip()
        nome = input('Digite o NOME da conta: ').strip()
        saldoInput = input('Digite o SALDO da conta: ')

    if id in banco:
        print('[!] Erro, id já existente')
        id = ''        

    if saldoInput.isdigit():
        saldo = int(saldoInput)
    else:
        saldo = -1

    banco[id] = {
        'nome' : nome,
        'saldo' : saldo
    }
    print(f'A conta {nome} (ID:{id}) foi criada com sucesso! ')

def depositar():
    id = input('Digite o ID para deposito: ')
    
    if id not in banco:
        print('[!] ID não encontrado.')    
        

    deposito = input('Digite o valor que deseja depositar R$: ').strip()
    
    if deposito.isdigit() and int(deposito) > 0:
        int(deposito)
        banco[id]['saldo'] += deposito

        print(f'[Sucesso] Deposito de R$ {deposito} ralizado!')
        print(f"Novo saldo de {banco[id]['nome']}: R$ {banco[id]['saldo']}")
    else:
        print("[Erro] Valor de depósito inválido! Use apenas números positivos.")

def depositar():
    id = input('Digite o ID para deposito: ')
    
    if id not in banco:
        print('[!] ID não encontrado.')    
        

    saque = input('Digite o valor que deseja sacar R$: ').strip()
    
    if saque.isdigit() and int(saque) > 0:
        int(saque)
        banco[id]['saldo'] -= saque

        print(f'[Sucesso] saque de R$ {saque} ralizado!')

        if banco[id]['saldo'] < 0:
            print(f"Atenção, saldo de {banco[id]['nome']}: R$ {banco[id]['saldo']}")
        else:
            print(f"Novo saldo de {banco[id]['nome']}: R$ {banco[id]['saldo']}")
    else:
        print("[Erro] Valor de depósito inválido! Use apenas números positivos.")

def buscaConta():
    continuar = 'sim'

    while(continuar == 's' or continuar == 'sim'):
        nome = input('Digite um nome: ').strip()

    while (nome == ''):
        print('[!] Todos os campos são obrigatórios.')
        nome = input('Digite um nome: ').strip()
    
    encontrado = False

    for id, dados in banco.items():
        if dados['nome'] == nome.lower():
            print(f'Conta encontrada, ID {id}')
            print(f"Saldo de {dados['nome']}: R$ {dados['saldo']}")
            break

    if not encontrado:
        print('conta não encontrada.')        
        
    continuar = input('Deseja fazer uma nova busca? (s/n)')                
            
def excluiConta():
    continuar = 'sim'

    while(continuar == 'sim' or continuar == 's'):
        
