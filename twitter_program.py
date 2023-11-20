'''
def main():
    print("")
    print("")
    print("")
    
    example_string = "i am an "
    number = input("enter option")

    if number == '1':
        word1 = "idiot"
        finished_string = example_string + word1
        print(finished_string)
    elif number == '2':
        word2 = "fud"
        finished_string = example_string + word2
        print(finished_string)
    else:
        word3 = "cretin"
        finished_string = example_string + word3
        print(finished_string)

'''

def main():
    print("")
    print("")
    print("")
    
    example_string = "i am a idiot"
    number = input("enter option")

    if number == '1':
        word1 = "total"
        finished_string = example_string[2] 
        print(finished_string)
    elif number == '2':
        word2 = "complete"
        finished_string = example_string + word2
        print(finished_string)
    else:
        word3 = ""
        finished_string = example_string + word3
        print(finished_string)
       




main()
