valores_depositados = []
valores_sacados = []
saldo_em_conta = 0
LIMITE_SAQUES = 3
quantidade_de_saques = 1

while True:
    print('---------- MENU ----------')
    print('')
    print('[d] Depositar')
    print('[s] Sacar')
    print('[e] Extrato')
    print('[x] Sair')
    print('')        
    menu = input('Selecione uma opção: ')
    print('')

    if menu == 'd':
        print('-------- DEPÓSITO --------')
        print('')     
        deposito = int(input('Insira um valor: '))
        while deposito < 0:
            print('Inserir valor superior a 0!')
            deposito = int(input('Insira um valor: '))
        valores_depositados.append(deposito)
        saldo_em_conta = saldo_em_conta + deposito
        print('')    
            
    elif menu == 's':  
        print('--------- SAQUE ----------')
        print('')
        if quantidade_de_saques > LIMITE_SAQUES:
            print('Não é possível realizar mais de 3 saques diários!')
            break
        if saldo_em_conta == 0:
            print('Você não tem recursos para saque!')
            break
        saque = int(input('Insira um valor: '))
        while saque > 500:
            print('')
            print('Não é possível sacar valor superior a R$500,00!')
            print('')
            saque = int(input('Insira um valor inferior a R$500,00: '))
        while saldo_em_conta < saque:
            print('Você não possui saldo em conta suficiente!')
            saque = int(input('Insira um valor menor: '))
        valores_sacados.append(saque)
        saldo_em_conta = saldo_em_conta - saque
        quantidade_de_saques += 1
        print('')

    elif menu == 'e': 
        print('-------- EXTRATO ----------')
        print('')
        indice_deposito = 1
        for cada_deposito in valores_depositados:
            print(f'{indice_deposito}º depósito: R${cada_deposito:.2f}')
            indice_deposito +=1
        indice_saque = 1
        print('')
        for cada_saque in valores_sacados:
            print(f'{indice_saque}º saque: R${cada_saque:.2f}')
            indice_saque +=1
        print('')
        print(f'Saldo em conta: R${saldo_em_conta:.2f}')        
        print('')

    elif menu == 'x':
        break 

    else:
        print('Insira uma opção válida!')
        print('')


    
   
            

        
        
       
        
        
    
