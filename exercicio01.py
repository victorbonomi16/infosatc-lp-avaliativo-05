#criar um sistema bancario
#cadastro de usuarios
#funcoes bancarias
 
for i in range(0,6):  
    nome = input("Informe seu nome:")
    sobrenome = input("Informe seu Sobrenome :")
    cpf = input("Informe seu CPF (11 DIGITOS):")
    endereco = input("Informe seu Endereco :")
    telefone = input("Informe seu telefone :")
    senha = input("Informe sua senha:") 

    #Perguntando ao usuario suas informacoes e verificando se estao nos requisitos
    while(len(nome)<3):
        print("Nome inválido,mínimo de tres letras")    
        nome = input("Informe seu nome novamente :") 

    while(len(sobrenome)<3):
        print("Sobrenome inválido,mínimo de tres letras")
        sobrenome = input("Informe seu Sobrenome novamente :") 

    while(len(cpf)<11):
        print("O seu CPF está incorreto")
        cpf = input("Informe seu CPF novamente (11 DIGITOS) :") 
 
    while((len(senha)<5) or (senha.isalnum()==True or senha.isalpha()==True)):
             print("A senha nao atende aos requisitos (Deve conter pelo menos 1 numero e caracter especial")
             senha = input("Informe sua senha: ) ")
    email = input("Informe seu email (Deve conter este formato (email@email) :")
    
    #verificando se contem @ no email
    for i in email:
        if("@" in email):
            break
    else:
        email = input("seu email esta incorreto, por favor insira novamente com este formato (email@email)"  )
    clientes={"nome:{}" .format(nome+" "+sobrenome),"Endereço:{}".format(endereco),"Senha:{}".format(senha),"Email:{}".format(email),"celular:{}".format(telefone),"cpf:{}".format(cpf)}
    print("Os dados da conta cadastrados -",clientes)
    print("----------") 
   
    todos=0
    todos=todos+1

    if(todos==1):
        contaprincipal={}
        contasecundaria=clientes.copy()
        print("Parabens, agora voce esta na sua Conta Principal")
    elif(todos==2):
        contasecundaria=clientes.copy()
        del clientes
        print("Parabens, agora voce esta na sua Conta Secundaria")
     
    saldoTotal=0
    depositar=0
    sacar=0
    def encerrar():
        if(todos==1):           
           print(contaprincipal)
           contaprincipal.clear()
        elif(todos==2):
           print(contasecundaria)
           contasecundaria.clear()
    print("----------")        
         
    encerrar()
      
    def menu():  
        saldo=0
        for i in range(0,9):                       
            menu = int(input("Olá o que voce deseja? \n1-Depositar\n2-Sacar\n3-Conferir Saldo\n4-Transferir\n5-Encerrar Conta\n")) 
            if(menu==1):
                deposito=float(input("Insira a quantia que deseje depositar:"))
                saldo=saldo+deposito
                print("Saldo:",saldo)
                while(deposito<0):
                     deposito=float(input("Impossivel depositar valor negativo, por favor insira um valor valido:"))
                     if(deposito>=0):
                        saldo=saldo+deposito
                        print("Saldo:",saldo)
                     else:
                         pass
            elif(menu==2):
                sacar=float(input("Insira a quantia quer deseja sacar :"))
                saldo=saldo-sacar  
                while(sacar>saldo):
                      sacar=float(input("Saldo insuficiente,impossivel efetuar o saque"))
                      saldo=saldo-sacar
            elif(menu==3):
                       print("Seu saldo no momento:",saldo)
            elif(menu==4):
                    transferir = float(input("Insira o valor que deseja transferir:"))
                    saldo=saldo-transferir
            elif(menu==5):
                     encerrar=input("Deseja mesmo encerrar? Digite sim caso queira.")
                     if(encerrar=="sim"):
                         encerrar()
                     else:
                         pass
            else:
                 pass

    menu() 
     