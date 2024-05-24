#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random

class Variaveis:
    
    def __init__(self):
        self.usuarios = {}
        self.contas = {}
        self.agencia = '0001'
        self.senhas = {}

class Cadastro_usuario(Variaveis):
    
    def __init__(self):
        super().__init__()
        self.count = 0
        self.estados = ['AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'ES', 'GO', 'MA',
                        'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN', 'RS',
                        'SC', 'SP', 'SE', 'TO', 'DF', 'RR', 'MS', 'MT', 'RO']
    
    def cadastrando_usuario(self):
        
        self.contador = 0
        print(f'\n{15* "*"}|Cadastro|{15*"*"}')
        
        while True:
            
            self.nome = input('Insira seu nome\n\n=>').upper()
            self.nome_valido = True
            for caractere in self.nome:
                if caractere.isdigit():
                    self.nome_valido = False
                    break
            if self.nome_valido:
                self.usuarios[self.nome] = [0 for i in range(4)]
                break
            else:
                print('Nome não pode conter números')
    
        while True:
            try:
                self.cpf_valido = True
                self.cpf = int(input('\nInsira seu CPF no formato 12345\n\n=>'))
                self.cpf = str(self.cpf)
                if len(self.cpf) == 5:      
                    for i in self.usuarios:
                        if self.usuarios[i][0] == self.cpf:
                            self.cpf_valido = False
                    if self.cpf_valido:
                        self.usuarios[self.nome][0] = self.cpf
                        break
                    else:
                        print('\nCPF já cadastrado!')
                        break
                else:
                    print('\nCPF deve contar 5 dígitos')
            except:
                print('Insira um CPF válido')
        
        self.cidade = str(input('\nCidade:\n\n=>'))
        self.usuarios[self.nome][1] = self.cidade
        
        while True:
            self.estado_valido = False
            self.estado = str.upper(input('\nSigla do estado:\n\n=>'))
            for i in range(len(self.estados)):
                if self.estados[i] == self.estado:
                    self.usuarios[self.nome][2] = self.estado
                    self.estado_valido = True
                    break
            if self.estado_valido:
                break
                
            else:
                print('\nInsira um estado válido')
                
                    
        self.endereco = str(input('\nEndereço:\n\n=>')) 
        self.usuarios[self.nome][3] = self.endereco
        print(f'\n{10* "*"}|Cadastro Realizado|{10*"*"}')
        
class Cadastro_conta(Variaveis):
    
    def __init__(self, usuarios):
        super().__init__()
        self.usuarios = usuarios
        self.count = 0
        self.contador = 0
        self.voltar_ao_menu = False

    def cadastrando_conta(self):

        while True:
            self.usuario_valido = True
            print(f'\n{10* "*"}|Cadastro de conta|{11*"*"}\n')
            self.cpf = str(input('Informe seu CPF ou digite [1] para voltar ao menu\n\n=>'))
            if self.cpf == '1':
                self.voltar_ao_menu = True
            break
                
            
        if self.voltar_ao_menu == False:
            
            while True:
                self.senha_valida = True
                self.senha = input('Cre uma senha de 4 dígitos\n\n=>')
                
                if len(self.senha) == 4:
                    for i in self.senha:
                        if not i.isdigit() or int(i) < 0:
                            self.senha_valida = False
                            break
                    if self.senha_valida:
                        break
                    else:
                        pass
                else:
                    print('A senhe deve conter 4 díditos')
                    
            self.count = 0
            while True:
                for i in self.usuarios:
                    if self.usuarios[i][0] == self.cpf:
                        for j in self.contas:
                            if j == self.usuarios[i][0]:
                                self.count += 1
                        if self.count > 0:
                            self.conta = random.randint(1000000000, 9999999999)
                            self.usuarios[i].append(self.conta)
                            self.contas[j].append({self.conta:[0]})
                            self.senhas[self.conta] = self.senha
                            self.iteracoes[self.conta] = [0]
                            print(f'\n{13* "*"}|Conta criada|{13*"*"}')
                            print('Conta vinculada à',i)
                            print('Agência: ', self.agencia)
                            print(f'Conta: {self.conta}')
                            print(f'Senha: {self.senha}')
                            print(f'{40 * "*"}')
                            self.contador += 1
                            print(self.contas[self.cpf])
                            break
                        else:
                            self.conta = random.randint(1000000000, 9999999999)
                            self.usuarios[i].append(self.conta)
                            self.contas[self.cpf] = [{self.conta:[0]}]
                            self.senhas[self.conta] = self.senha
                            self.iteracoes[self.conta] = [0]
                            print(f'\n{13* "*"}|Conta criada|{13*"*"}')
                            print('Conta vinculada à',i)
                            print('Agência: ', self.agencia)
                            print(f'Conta: {self.conta}')
                            print(f'Senha: {self.senha}')
                            print(f'{40 * "*"}')
                            self.contador += 1
                            print(self.contas[self.cpf])
                            break
                if self.contador == 0:
                    print('\nUsuário não encontrado')
                    break
                else:
                    break
                    
class Exibir_contas(Variaveis):
    
    def __init__(self, usuarios, contas):
        super().__init__()
        self.usuarios = usuarios
        self.contas = contas
    
    def exibindo_contas(self):
        
        self.cpf = str(input('\nInforme seu CPF\n\n=>'))
        if self.cpf in self.contas:
            print(self.contas[self.cpf])
        else:
            print('Nenhuma conta encontrada para este CPF.')
                    
class Menu(Variaveis):
    
    def __init__(self):
        super().__init__()
        self.usuarios = Cadastro_usuario()
        self.contas = Cadastro_conta(self.usuarios.usuarios)
        self.exibindo_contas = Exibir_contas(self.usuarios.usuarios, self.contas.contas)
        self.entrar = Menuzinho(self.usuarios.usuarios, self.contas.contas)
    
    def exibir_menu(self):

        while True:
            print(f"""
{14 * '*'}|AstroBanco|{14 * '*'}""")
            menu = """    
****************************************
*[1] Entrar                            *
*[2] Cadastrar novo usuário            *
*[3] Cadastrar nova conta              *
*[4] Exibir Contas                     *
*[5] Sair                              *
****************************************  

=>"""
            try:
                opcao_principal = int((input(menu)))     
            except ValueError:
                print('Insira uma opção válida')
                
            if 1 <= opcao_principal <= 5:
                
                if opcao_principal == 1:
                    self.entrar.entrar()
                elif opcao_principal == 2:
                    self.usuarios.cadastrando_usuario()
                elif opcao_principal == 3:
                    self.contas.cadastrando_conta()
                elif opcao_principal == 4:
                    self.exibindo_contas.exibindo_contas()
                elif opcao_principal == 5:
                    print(f'{10* "*"}Operação Finalizada!{10*"*"}')
                    break
            else:
                print('Insira uma opção válida')
                
class Menuzinho(Variaveis):
    
    def __init__(self, usuarios, contas):
        super().__init__()
        self.count = 0
        self.usuarios = usuarios
        self.contas = contas
        self.saques_diarios = {}
        
    def depositar(self):
    
            while True:
                self.depositos = float(input('Digite o valor do depósito:\n\n=>'))
                if self.depositos > 0:
                    self.contas[self.cpf][self.conta_atual][self.conta].append(self.depositos)
                    print(f'\nDeposito de R$ {self.depositos:.2f} realisado')
                    break
                else:
                    print('\nValores negativos ou nulos não são permitidos')
                    
    def saque(self):
    
            if sum(self.contas[self.cpf][self.conta_atual][self.conta]) > 0:
                while True:
                    self.saques = float(input('Digite o valor do saque:\n\n=>'))
                    if self.saques > 0 and self.saques <= 500.:
                        if sum(self.contas[self.cpf][self.conta_atual][self.conta]) > self.saques:
                            self.saques1 = -self.saques
                            self.contas[self.cpf][self.conta_atual][self.conta].append(self.saques1)
                            print(f'\nSaque de R$ {self.saques:.2f} realizado')
                            break
                        if sum(self.contas[self.cpf][self.conta_atual][self.conta]) < self.saques:
                            print('\nSaldo insuficiente')
                    else:
                        print('\nLimite de valor de saque em R$ 500.00')
                else:
                    print('Valores negativos ou nulos não são permitidos')
            elif sum(self.contas[self.cpf][self.conta_atual][self.conta]) == 0:
                print('\nVocê não tem saldo para realizar o saque!')
            else:
                pass
            
    def extrato(self):
        print(f'{40 * "*"}')
        for i in range(len(self.contas[self.cpf][self.conta_atual][self.conta])):
            if self.contas[self.cpf][self.conta_atual][self.conta][i] > 0:
                print(f'Deposito no valor de R$ {self.contas[self.cpf][self.conta_atual][self.conta][i]:.2f}\n')
            elif self.contas[self.cpf][self.conta_atual][self.conta][i] < 0:
                print(f'Saque no valor de R$ {self.contas[self.cpf][self.conta_atual][self.conta][i]:.2f}\n')
        print(f'Saldo total de R$ {sum(self.contas[self.cpf][self.conta_atual][self.conta]):.2f}')
        print(f'{40 * "*"}')
        
    def entrar(self):
        
        while True:
            self.conta_nao_entontrada = True
            self.count2 = 0
            self.nao_possui_conta = True
            self.cpf = str(input('Informe seu CPF ou digite [1] para voltar ao menu\n\n=>'))
            for n in self.usuarios:
                if self.usuarios[n][0] == self.cpf:
                    for x in self.contas[self.cpf]:
                        self.chave = list(x.keys())[0]
                        print('Contas vinculadas:', self.chave)
            if self.cpf == '1':
                break
            else:
                for m in self.contas:
                    if self.cpf == m:
                        self.nao_possui_conta = False
                if self.nao_possui_conta:
                    print('\nUsuário não existe')
                else:
                    self.conta = int(input('\nInforme o número da conta ou digite [1] para voltar ao menu\n\n=>'))
                    if self.conta == 1:
                        break
                    else:
                        self.quantidade_de_contas = len(self.contas[self.cpf])
                        for k in range(self.quantidade_de_contas):
                            if list(self.contas[self.cpf][k].keys())[0] == self.conta:
                                self.conta_atual = k
                                self.conta_nao_encontrada = False
                                break
                        if self.conta_nao_encontrada:
                            print('\nConta não encontrada')
                        else:
                            break
                            
        if self.cpf != '1':
            self.saques_diarios[self.conta] = 0
            while True:
                self.menu = """
****************************************
*[1] Depositar                         *
*[2] Sacar                             *
*[3] Extrato                           *
*[4] Sair                              *
****************************************  

=>"""
                self.opcao = input(self.menu)
                
                if 1 <= int(self.opcao) <= 4:
                    self.opcao = int(self.opcao)
                    if self.opcao == 1:
                        self.depositar()
                    elif self.opcao == 2:
                        if self.saques_diarios[self.conta] < 3:
                            self.saque()
                            self.saques_diarios[self.conta] += 1
                        else:
                            print(f'{40 * "*"}')
                            print('*  Limite diário de saque atingido!  *')
                            print(f'{40 * "*"}')
                    elif self.opcao == 3:
                        self.extrato()
                    elif self.opcao == 4:
                        print(f'{10* "*"}Operação Finalizada!{10*"*"}')
                        break
                    else:
                        print('Digite uma opção válida')
                else:
                    print('Digite uma opção válida')
                    
astrobanco = Menu()
astrobanco.exibir_menu()


# In[ ]:




