def readtext():
    passwordList = []
    yourpassword = input("enter your passowrd to check if it has been comprismised")

    f = open("rockyou1000.txt","r")
    for line in f:
        if line != yourpassword:
            passwordList.append(line)
        else:
            print("your password has been found")
    f.close()
    return passwordList


def writepasswordlist(passwords):
    yourpassword = input("enter your passowrd to check if it has been comprismised")
    if yourpassword in passwordlist:
        print("your password has beeen found")
    
    '''
    f = open("newpasswords.txt", "w")
    for password in passwordlist:
        f.write(password)
    f.close()
    '''

def main():
    passwords = readtext()
    writepasswordlist(passwordlist)

if __name__ == "__main__":
    main()