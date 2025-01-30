def addition():
    while True:
        try:
            add = input("Please entrer your addition:")
            if any(a.isalpha() for a in add):
                raise ValueError
            if add == '=':
                break
            if '+' in add:
                num = add.split('+')
                total = 0
                for i in num:
                    total += float(i.strip())
                print(f"resultat:{total}")
        except ValueError:
            print("You made a mistake or mistakes. Check what you entered.")

        response = input("Do you want to continue? [Yes/No]: ")
        if response.lower() == 'no':
            break

def subtraction():
    while True:
        try:
            sub = input("Please input your subtraction:")
            if any(a.isalpha() for a in sub):
                raise ValueError
            if sub == '=':
                break
            if '-' in sub:
                num = sub.split('-')
                totalsub = float(num[0].strip())
                for i in num[1:]:
                    totalsub -= float(i.strip())
                print(f"resultat:{totalsub}")
        except ValueError:
            print("You made a mistake or mistakes. Check what you entered.")

        response = input("do you want to continue? [Yes/No]: ")
        if response.lower() == 'no':
            break

def multiplication():
    while True:
        try:
            mul = input("Please input your multiplication:")
            #cette ligne vérifie si il y'a une lettre et renvoie
            if any(a.isalpha() for a in mul):
                raise ValueError
            if mul == '=':
                break
            if '*' in mul:
                num = mul.split('*')
                totalmul = 1
                for i in num:
                    totalmul *= float(i.strip())
                print(f"resultat:{totalmul}")
        except ValueError:
            print("You made a mistake or mistakes. Check what you entered.")

        response = input("do you want to continue? [Yes/No]: ")
        if response.lower() == 'no':
            break

def division():
    while True:
        try:
            div = input("Please input your division:")
            #cette ligne vérifie si il y'a une lettre et renvoie
            #a.isalpha c'est pour la vérification de lettre
            if any(a.isalpha() for a in div):
                raise ValueError
            if div == '=':
                break
            if '/' in div:
                num = div.split('/')
                totaldiv = float(num[0].strip())
                for i in num[1:]:
                    totaldiv /= float(i.strip())
                print(f"resultat:{totaldiv}")
        except ValueError:
            print("You made a mistake or mistakes. Check what you entered.")
        reponse = input("do you want to continue? [Yes/No]: ")
        if reponse.lower() == 'no':
            break
#division()
#ce code permet de tout faire que ce soit +,-,/,*
def calcul():
    while True:
        try:
            calc = input("Please input your calculation:")
            if any(a.isalpha() for a in calc):
                raise ValueError
            if calc == '=':
                break
            operation = eval(calc)
            print(f"resultat:{operation}")
        except ValueError:
            print("You made a mistake or mistakes. Check what you entered.")
        response = input("do you want to continue? [Yes/No]: ")
        if response.lower() == 'no':
                break