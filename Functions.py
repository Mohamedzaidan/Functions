# #solve files
def new_file():
    name = input("please put your name :")
    age = input("please put your age :")
    adress = input("please put your email :")

    def function2():
        f1 = open("client.txt","w")
        f1.close()

        def function3():

            f1 = open("client.txt","w")
            f1.write(f"the client name is {name} , age is {age} and adress is {adress}")
            f1.close()
            while True:
                cont = input('Continue? (y/n): ')
                if cont.lower() == 'n':
                    break
            f1 = open("client.txt","r")
            content = f1.read()
            print(content)
            

        function3()
    function2()




new_file()



# solve 2

def long_alpha(s):
    max_substring = s[0]
    current_substring = s[0]
    for i in range(1, len(s)):
        if s[i] >= s[i-1]:
            current_substring += s[i]
            if len(current_substring) > len(max_substring):
                max_substring = current_substring
        else:
            current_substring = s[i]
    print(f'Longest substring in alphabetical order is: {max_substring}')

long_alpha("abdelrahman")