from basic_clases.basic_seller import Seller
from basic_clases.basic_manager import Manager
from basic_clases.basic_admin import Admin
from basic_clases.basic_user import User

try:
    accounts = User.reader('accounts')
    i = 0
    for el in accounts:
        print(f"{i} -- {el[f'first_name']} {el['last_name']}")
        i += 1

    print("ex - exit")
    inp = input("Choose your account: ")
    inp = int(inp)

    try:
        a = accounts[inp]
        for i in range(3):
            in_password = str(input("Insert password: "))

            if in_password == a['password']:
                if a['position'] == 'admin':
                    user = Admin(accounts[inp])
                elif a['position'] == 'seller':
                    user = Seller(accounts[inp])
                elif a['position'] == 'manager':
                    user = Manager(accounts[inp])

                company = user.doing()
                print(company)
                break
            elif in_password == 'ex':
                break
            else:
                print("nope")
    except:
        print("fuck")
except:
    print("not int")
