#usuario vai digitar o username e a password

User = str("admin")
password = str("123456")

lUser = str(input("User: "))
lPassword = str(input("Password: "))

if lUser == User and lPassword == password:
    print("login efetuado com sucesso!")

else:
    print("usuario ou senha incorreto(s)")

