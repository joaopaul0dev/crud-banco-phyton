banco = {}

def gerarConta():
    print('\n-- CADASTRO DA CONTA --')

    id_conta = ''
    nome = ''
    saldo = -1
    
    while nome == '' or id_conta == '' or saldo < 0:
        id_conta = input('Digite o ID da conta: ').strip()        
        if id_conta in banco:
            print('[!] Erro: ID já existente. Escolha outro.')
            id_conta = '' 
            continue            
    
        nome = input('Digite o NOME da conta: ').strip()
        saldoInput = input('Digite o SALDO da conta: ').strip()
    
        if saldoInput.isdigit():
            saldo = int(saldoInput)
        else:
            print('[!] Saldo inválido! Digite apenas números positivos.')
            saldo = -1
    
    banco[id_conta] = {
        'nome': nome,
        'saldo': saldo
        }
    
    print(f'\nA conta de {nome} (ID: {id_conta}) foi criada com sucesso!')

def depositar():
    print('\n-- DEPOSITO  --')
    id = input('\nDigite o ID para deposito: ')
    
    if id not in banco:
        print('[!] ID não encontrado.')    
        return

    deposito = input('Digite o valor que deseja depositar R$: ').strip()
    
    if deposito.isdigit() and int(deposito) > 0:
        valor = int(deposito)
        banco[id]['saldo'] += valor

        print(f'\n[Sucesso] Deposito de R$ {valor} ralizado!')
        print(f'\nNovo saldo de {banco[id]['nome']}: R$ {banco[id]['saldo']}')
        
    else:
        print('\n[Erro] Valor de depósito inválido! Use apenas números positivos.')

def sacar():
    print('\n-- SAQUE --')
    id = input('\nDigite o ID para saque: ')
    
    if id not in banco:
        print('[!] ID não encontrado.')    
        return

    saque = input('Digite o valor que deseja sacar R$: ').strip()
    
    if saque.isdigit() and int(saque) > 0:
        valor = int(saque)
        banco[id]['saldo'] -= valor

        print(f'[Sucesso] saque de R$ {valor} ralizado!')

        if banco[id]['saldo'] < 0:
            print(f"\nAtenção, saldo de {banco[id]['nome']}: R$ {banco[id]['saldo']} negativo.")
            
        else:
            print(f"\nNovo saldo de {banco[id]['nome']}: R$ {banco[id]['saldo']}")
            
    else:
        print("\n[Erro] Valor de depósito inválido! Use apenas números positivos.")
        

def buscaConta():
    print('\n-- EXIBIR RELATÓRIO --')
    continuar = 'sim'

    while(continuar == 's' or continuar == 'sim'):
        id = input('Digite um id: ').strip()

        while (id == ''):
            print('\n[!] Todos os campos são obrigatórios.')
            id = input('Digite um nome: ').strip()
    
        encontrado = False

        for id_conta, dados in banco.items():
            if id_conta.lower() == id.lower():
                print(f'\nConta encontrada, ID {id}')
                print(f"Saldo de {dados['nome']}: R$ {dados['saldo']}")
                encontrado = True
                break

        if not encontrado:
            print('conta não encontrada.')        
        
        continuar = input('\nDeseja fazer uma nova busca? (s/n)').strip().lower()

def excluiConta():
    print('\n-- EXCLUIR CONTA --')
    continuar = 'sim'

    while (continuar == 'sim' or continuar == 's'):
        id_busca = input('Insira um ID: ').strip()

        while (id_busca == ''):
            print('\n[!] O campo precisa ser preenchido')
            id_busca = input('Insira um ID: ').strip()
        
        if id_busca in banco:
            nome_usuario = banco[id_busca]['nome']
            saldo_usuario = banco[id_busca]['saldo']
            
            confirmacao = input(f"Deseja realmente excluir a conta de {nome_usuario} (ID: {id_busca})? (s/n): ").strip().lower()
        
            if confirmacao == 'sim' or confirmacao == 's':
                del banco[id_busca] 
                print(f"Conta de {nome_usuario}: R$ {saldo_usuario} deletada com sucesso.")
        else:
            print('Conta não encontrada (ID inexistente).')                
        
        continuar = input('\nDeseja fazer uma nova exclusão? (s/n): ').strip().lower()


def excluirBanco():
    print('\n-- EXCLUSÃO DE CONTA --')
    continuar = 'sim'

    while (continuar  == 'sim' or continuar == 's'):
        confirmacao = input(f'Deseja excluir todas as conta? {len(banco)} contas serão excluidas. (s/n)')

        if (confirmacao == 'sim' or confirmacao == 's'):
            print(f'\n {len(banco)} contas forão excluidas.')        
            banco.clear()

        continuar = input('Deseja continuar? (s/n)')

def menu():
    opcao = 0

    while opcao != 7:
        print('\n')
        print('=' *25)
        print("     MENU DE OPÇÕES      ")
        print('=' *25)
        print("1. Cadastrar Usuário")
        print("2. Exibir Conta")
        print("3. Sacar valor")
        print('4. Depositar Valor')
        print('5. Excluir conta')
        print('6. Excluir todas as contas')
        print('7. Encerrando o programa')
        print('=' *25)

        try:
            opcao = int(input("Escolha uma opção (1-6): "))

            if opcao == 1:
                print("\nVocê escolheu: Cadastrar Usuário")
                gerarConta()

            elif opcao == 2:
                print("\nVocê escolheu: Exibir Conta")
                buscaConta()

            elif opcao == 3:
                print("\nVocê escolheu: Sacar Valor")
                sacar()         

            elif opcao == 4:
                print("\nVocê escolheu: Depositar Valor")
                depositar()

            elif opcao == 5:
                print("\nVocê escolheu: Excluir Conta")
                excluiConta()

            elif opcao == 6:
                print("\nVocê escolheu: Excluir todas as Conta")
                excluirBanco()

            elif opcao == 7:
                print("\nEncerrando o programa. Até logo!")

            else:
                print("\nOpção inválida! Digite um número entre 1 e 7.")

        except ValueError:
            print("\nEntrada inválida! Por favor, digite apenas números.")
menu()