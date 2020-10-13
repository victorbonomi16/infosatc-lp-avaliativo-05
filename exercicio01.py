def ValidateName():
    name=input("Informe seu nome : ")
    name_split = name.split()
    print(name_split)
    for x in name_split:        
        if len(x)>3:
            pass
        else:
            print("\nnome invalido:")
            continuar = int(input("1- Tentar novamente  2- Sair :"))
            if continuar==1:
                ValidateName()
            else:
                SystemExit(0)
    return name

def ValidatePassword():
    password=input("informe sua senha (deve conter um número e um caractere especial)  :" ) 
    if len(password)>5:
        for x in ["1","2","3","4","5","6","7","8","9"]:
            for i in password:
                if x==i:
                    if "@" or "_" or "-" or "*" or "#" or "$" in password:
                        return password
    print("\nsenha invalida:")
    continuar = int(input("1- Tentar novamente  2- Sair :"))
    if continuar==1:
        ValidatePassword()
    else:
        return False

def ValidateEmail():
    email=input("Informe seu email : ")
    if "@" in email:
        return email
    else:
        print("\nemail incorreto ou inválido. ")
    continuar = int(input("1- Tentar novamente  2- Sair :"))
    if continuar==1:
        ValidateEmail()
    else:
        return False

def Register():
    name=ValidateName()
    password=ValidatePassword()
    email=ValidateEmail()
    cpf=input("Informe seu cpf :")
    address=input("Informe seu endereço :")
    cell=input("Informe seu numero de celular:")
    if name==False or password==False or email==False:
        print("credenciais incoretas")
        SystemExit(0)
    else:
        list_name.append(name)
        list_password.append(password)
        list_email.append(email)
        list_address.append(address)
        list_cpf.append(cpf)
        list_cell.append(cell) 
        codigo=list_name.index(name)
        list_balance.append(0)


def Deposit(codigo):
    deposit=float(input("\nInforme a quantia que deseja depositar : "))
    if deposit>0:
        list_balance[codigo]+=deposit
    else:
        print("valor invalido")
        return

def Withdraw(codigo):
    withdraw=float(input("\nInforme a quantia que deseja sacar : "))
    if withdraw <list_balance[codigo]:
        list_balance[codigo]=(list_balance[codigo])-(withdraw)

def CheckBalance(codigo):
    print("\nseu saldo é:", list_balance[codigo], )

def Transfer(codigo):
    code_transfer=int(input("Qual conta voce deseja mandar :"))
    value_transfer=float(input("valor que deseja enviar ou digite 0 caso deseja cancelar :"))
    if value_transfer<=0:
        return
    elif value_transfer<=list_balance[codigo]:
        list_balance[codigo]+= -value_transfer
        list_balance[code_transfer]+=value_transfer
    else:
        print("\nValor inexistente !")
        return


def Login():
    login_email=input("\nInforme seu email :")
    login_password=input("Informe sua senha : ")
    if login_email in list_email:
        if (login_password in list_password) and (list_email.index(login_email)==list_password.index(login_password)):
                ChoiceAccount(list_email.index(login_email))
        else:
            print("Senha inválida, insira email e senha novamente:")
            Login()
    else:
        print("\neste email nao existe ou nao foi registrado  :")
        escolha=input("1-Tentar novamente  2-sair : ")
        if escolha =="1":
            Login()
        else:
            return

def ChoiceAccount(codigo):
    while True:
        print("\nInforme o numero correspondende a operacao que deseja:")
        print("1-Depositar")
        print("2-Sacar")
        print("3-conferir o saldo")
        print("4-Trasferir")
        print("5-Encerrar conta")
        escolha=int(input("-->"))
        if escolha==1:
            Deposit(codigo)
        elif escolha==2:
            Withdraw(codigo)
        elif escolha==3:
            CheckBalance(codigo)
        elif escolha==4:
            Transfer(codigo)
        elif escolha==5:
            return
        print(list_balance)
 
def Choice():
    while True:
        print("1-Logar 2-Cadastrar 3-sair ")
        choice = int(input(">"))
        if(choice==1):
            Login()
        elif(choice==2):
            Register() 
        if(choice==3):
            break
    return
 
list_name=[]
list_password=[]
list_email=[]
list_address=[]
list_cpf=[]
list_cell=[]
list_balance=[]
list_code=[] 
Choice()