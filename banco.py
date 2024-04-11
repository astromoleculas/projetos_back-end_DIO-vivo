import random

limite = 0
contador = 0
contador2 = 0
iteracao = 0
opcao = 0
usuarios = {}
contas = {}
agencia = '0001'

def menuzinho(limite, contador, contador2, iteracao, opcao, usuarios, agencia, contas):
    count = 0
    
    while count == 0:
        count2 = 0
        
        cpf = str(input('Informe seu CPF ou digite [1] para voltar ao menu\n\n=>'))
        for n in usuarios:
            if usuarios[n][0] == cpf:
                for x in contas[cpf]:
                    chave = list(x.keys())[0]
                    print('Contas vinculadas:', chave)
        if cpf == '1':
            count += 1
            return iteracao, contador, opcao, usuarios
        
        else:
            for m in contas:
                if cpf == m:
                    count2 += 1
            if count2 == 0:
                print('\nUsuário não possui conta')
            else:
                conta = int(input('\nInforme o número da conta ou digite [1] para voltar ao menu\n\n=>'))
                if conta == 1:
                    count += 1
                    return iteracao, contador, usuarios
                else:
                    quantidade_de_contas = len(contas[cpf])
                    for k in range(quantidade_de_contas):
                        if list(contas[cpf][k].keys())[0] == conta:
                            conta_atual = k
                            count += 1
                    if count == 0:
                        print('\nConta não encontrada')
                    else:
                        continue
    
    while iteracao == 0:
    
        def depositar(contas, contador):
    
            while True:
                depositos = float(input('Digite o valor do depósito:\n\n=>'))
                if depositos > 0:
                    contas[cpf][conta_atual][conta].append(depositos)
                    print(f'\nDeposito de R$ {depositos:.2f} realisado')
                    break
                else:
                    print('\nValores negativos ou nulos não são permitidos')
    
            return

        def saque(contas):
    
            if sum(contas[cpf][conta_atual][conta]) > 0:
                while True:
                    saques = float(input('Digite o valor do saque:\n\n=>'))
                    if saques > 0 and saques <= 500.:
                        if sum(contas[cpf][conta_atual][conta]) > saques:
                            saques1 = -saques
                            contas[cpf][conta_atual][conta].append(saques1)
                            print(f'\nSaque de R$ {saques:.2f} realizado')
                            break
                        if sum(contas[cpf][conta_atual][conta]) < saques:
                            print('\nSaldo insuficiente')
                    else:
                        print('\nLimite de valor de saque em R$ 500.00')
                else:
                    print('Valores negativos ou nulos não são permitidos')
            elif sum(contas[cpf][conta_atual][conta]) == 0:
                print('\nVocê não tem saldo para realizar o saque!')
            else:
                pass
    
            return

        def extrato(contas):
            print(f'{40 * "*"}')
            for i in range(len(contas[cpf][conta_atual][conta])):
                if contas[cpf][conta_atual][conta][i] > 0:
                    print(f'Deposito no valor de R$ {contas[cpf][conta_atual][conta][i]:.2f}\n')
                elif contas[cpf][conta_atual][conta][i] < 0:
                    print(f'Saque no valor de R$ {contas[cpf][conta_atual][conta][i]:.2f}\n')
            print(f'Saldo total de R$ {sum(contas[cpf][conta_atual][conta]):.2f}')
            print(f'{40 * "*"}')

            return

        def menu(iteracao, limite, contas):
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
                        depositar(contas, contador)
                    elif opcao == 2:
                        contador3 += 1
                        limite += 1
                        historico = len(contas[cpf][conta_atual][conta])
                        if limite < 4:
                            saque(contas)
                            if historico == len(contas[cpf][conta_atual][conta]):
                                limite -= 1
                            else:
                                continue
                        else:
                            print(f'{40 * "*"}')
                            print('*   Limite diário de saque atingido!   *')
                            print(f'{40 * "*"}')
                    elif opcao == 3:
                        contador3 += 1
                        extrato(contas)
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
                iteracao, limite, opcao = menu(iteracao, limite, contas)
                contador += 1
            if contador > 0:
                if opcao != 4:
                    while contador2 == 0 and opcao != 4:
                        novas_operacoes = str(input(f'\n{40 * "*"}\nDeseja realizar uma nova operação? [s/n]\n{40 * "*"}\n\n=>'))
                        if novas_operacoes == 's':
                            if opcao == 4:
                                return (1, contador, 4)
                            else:
                                iteracao, limite, opcao = menu(iteracao, limite, contas)
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
            
def cadastro_usuario(usuarios):
    
    contador = 0
        
    print(f'\n{15* "*"}|Cadastro|{15*"*"}')
    nome = str.upper(input('Insira seu nome\n\n=>'))
    usuarios[nome] = [0 for i in range(4)]
    
    while contador == 0:
        cpf = input('\nInsira seu cpf no formato 12345\n\n=>')
        if len(cpf) == 5:      
            for i in usuarios:
                if usuarios[i][0] != cpf:          
                    usuarios[nome][0] = cpf
                    cidade = str(input('\nCidade:\n\n=>'))
                    usuarios[nome][1] = cidade
                    count = 0
                    while count == 0:
                        estado = str.upper(input('\nSigla do estado:\n\n=>'))
                        
                        estados1 = ['AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'ES', 'GO', 'MA']
                        estados2 = ['MG', 'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN', 'RS']
                        estados3 = ['SC', 'SP', 'SE', 'TO', 'DF', 'RR', 'MS', 'MT', 'RO']
                        estados_total = estados1 + estados2 + estados3
                        
                        for i in range(len(estados_total)):
                            if estados_total[i] == estado:
                                count += 1
                        if count > 0:
                            usuarios[nome][2] = estado
                        else:
                            print('\nInsira um estado válido')
                    endereco = str(input('\nEndereço:\n\n=>')) 
                    usuarios[nome][3] = endereco
                    print(f'\n{10* "*"}|Cadastro Realizado|{10*"*"}')
                    contador += 1
                    return usuarios
                else:
                    print('\nCPF já cadastrado!')
                    del usuarios[nome]
                    contador += 1
                    return usuarios
        else:
            print('\nCPF deve contar 5 dígitos')
    
    return usuarios

def cadastro_conta(usuarios, agencia):
    
    contador = 0
    count = 0
    
    while contador == 0:
        print(f'\n{10* "*"}|Cadastro de conta|{11*"*"}\n')
        cpf = str(input('Informe seu CPF ou digite [1] para voltar ao menu\n\n=>'))
        if cpf == '1':
            contador += 1
            return usuarios, contas
        else:
            for i in usuarios:
                if usuarios[i][0] == cpf:
                    for j in contas:
                        if j == usuarios[i][0]:
                            count += 1
                    if count > 0:
                        conta = random.randint(1000000000, 9999999999)
                        usuarios[i].append(conta)
                        contas[j].append({conta:[0]})
                        print(f'\n{13* "*"}|Conta criada|{13*"*"}')
                        print('Conta vinculada à',i)
                        print('Agência: ', agencia)
                        print(f'Conta: {conta}')
                        print(f'{40 * "*"}')
                        contador += 1
                    else:
                        conta = random.randint(1000000000, 9999999999)
                        usuarios[i].append(conta)
                        contas[cpf] = [{conta:[0]}]
                        print(f'\n{13* "*"}|Conta criada|{13*"*"}')
                        print('Conta vinculada à',i)
                        print('Agência: ', agencia)
                        print(f'Conta: {conta}')
                        print(f'{40 * "*"}')
                        contador += 1
            if contador == 0:
                print('\nUsuário não encontrado')
            else:
                continue
            
            
    return usuarios, contas

def menu_principal(usuarios, agencia, contas):
    contador = 0
    while contador == 0:
        print(f"""
{14 * '*'}|AstroBanco|{14 * '*'}""")
        menu = """    
****************************************
*[1] Entrar                            *
*[2] Cadastrar novo usuário            *
*[3] Cadastrar nova conta              *
*[4] Sair                              *
****************************************  

=>"""
        opcao_principal = (input(menu))
        try:
            opcao_principal = int(opcao_principal)
        except:
            print('Insira uma opção válida')
            continue
        if opcao_principal == 1:
            menuzinho(limite, contador, contador2, iteracao, opcao, usuarios, agencia, contas)
        elif opcao_principal == 2:
            usuarios = cadastro_usuario(usuarios)
        elif opcao_principal == 3:
            usuarios, contas = cadastro_conta(usuarios, agencia)
        elif opcao_principal == 4:
            contador += 1
            print(f'{10* "*"}Operação Finalizada!{10*"*"}')
        else:
            print('Insira uma opção válida')

    return usuarios, contas

usuarios, contas = menu_principal(usuarios, agencia, contas)
