s_password="235382275"
while True:
    password=input("enter the password:")
    if password==s_password:
        print("access granted:")
        break
    else:
        print("access not granted, try again")