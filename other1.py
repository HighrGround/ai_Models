def readtext():
    passwordList = []
    yourpassword = input("enter your passowrd to check if it has been comprismised")
    f = open("rockyou1000.txt","r")
    for line in f:
        passwordList.append(line)
    f.close()
    return yourpassword, passwordList


def writepasswordlist(userpassword, passwordlist):
    yourpassword = input("enter your passowrd to check if it has been comprismised")
    if userpassword in passwordlist:
        print("your password hhas beeen found")
    else:
        print("your password has not been found")
        passwordlist.append(userpassword)
    

    f = open("rockyou.txt", "w")
    for password in passwordlist:
        f.write(password)
    f.close()
    

def main():
    userpassword, passwords = readtext()
    writepasswordlist(userpassword, passwordlist)

if __name__ == "__main__":
    main()