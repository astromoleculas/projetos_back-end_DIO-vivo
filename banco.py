saldo = [0]
limite = 0
contador = 0
contador2 = 0
iteracao = 0
opcao = 0

while iteracao == 0:
    
    def depositar(saldo, contador):
    
        while True:
            depositos = float(input('Digite o valor do depósito:\n\n=>'))
            if depositos > 0:
                saldo.append(depositos)
                print(f'\nDeposito de R$ {depositos:.2f} realisado')
                break
            else:
                print('\nValores negativos ou nulos não são permitidos')
    
        return

    def saque(saldo):
    
        if sum(saldo) > 0:
            while True:
                saques = float(input('Digite o valor do saque:\n\n=>'))
                if saques > 0 and saques <= 500.:
                    if sum(saldo) > saques:
                        saques1 = -saques
                        saldo.append(saques1)
                        print(f'\nSaque de R$ {saques:.2f} realizado')
                        break
                    if sum(saldo) < saques:
                        print('\nSaldo insuficiente')
                else:
                    print('\nLimite de valor de saque em R$ 500.00')
            else:
                print('Valores negativos ou nulos não são permitidos')
        elif sum(saldo) == 0:
            print('\nVocê não tem saldo para realizar o saque!')
        else:
            pass
    
        return

    def extrato(saldo):
        print(f'{40 * "*"}')
        for i in range(len(saldo)):
            if saldo[i] > 0:
                print(f'Deposito no valor de R$ {saldo[i]:.2f}\n')
            elif saldo[i] < 0:
                print(f'Saque no valor de R$ {saldo[i]:.2f}\n')
        print(f'Saldo total de R$ {sum(saldo):.2f}')
        print(f'{40 * "*"}')

        return

    def menu(iteracao, limite):
        contador3 = 0
        while contador3 == 0:
            menu = """
****************************************
*[1] Depositar                         *
*[2] Sacar                             *
*[3] Extrato                           *
*[4] Sair                              *
****************************************            
=>"""
            opcao = input(menu)
            try:
                opcao = int(opcao)
                if opcao == 1:
                    contador3 += 1
                    depositar(saldo, contador)
                elif opcao == 2:
                    contador3 += 1
                    limite += 1
                    historico = len(saldo)
                    if limite < 4:
                        saque(saldo)
                        if historico == len(saldo):
                            limite -= 1
                        else:
                            continue
                    else:
                        print(f'{40 * "*"}')
                        print('*   Limite diário de saque atingido!   *')
                        print(f'{40 * "*"}')
                elif opcao == 3:
                    contador3 += 1
                    extrato(saldo)
                elif opcao == 4:
                    print(f'{10* "*"}Operação Finalizada!{10*"*"}')
                    contador3 += 1
                    return (1, limite, 4)
                else:
                    print('Digite uma opção válida')
            except:
                print('Digite uma opção válida')
        return iteracao, limite, opcao
    
    def inicializacao(contador, contador2, iteracao, limite):
        
        if contador == 0 and iteracao == 0:
            iteracao, limite, opcao = menu(iteracao, limite)
            contador += 1
        if contador > 0:
            if opcao != 4:
                while contador2 == 0 and opcao != 4:
                    novas_operacoes = str(input(f'\n{40 * "*"}\nDeseja realizar uma nova operação? [s/n]\n{40 * "*"}\n\n=>'))
                    if novas_operacoes == 's':
                        if opcao == 4:
                            return (1, contador, 4)
                        else:
                            iteracao, limite, opcao = menu(iteracao, limite)
                    elif novas_operacoes == 'n':
                        print(f'{10* "*"}Operação Finalizada!{10*"*"}')
                        contador2 += 1
                        iteracao += 1
                    else:
                        print('Digite uma opção válido')
            else:
                return (1, contador, 4)
            
        return iteracao, contador, opcao
    
    if opcao != 4:
        iteracao, contador, opcao = inicializacao(contador, contador2, iteracao, limite)
