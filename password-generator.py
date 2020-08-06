from random import choice

class gerador():
       
    def gerador_senha(tamanho):
        caracteres = "0123456789abcdefghijklmnopqrstuwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ@!#$%&*()_+}{`^?;:>/-+.,"
        senha = ""
        for i in range(tamanho):
            senha += choice(caracteres)
        return senha


    def pergunta_arquivo(resposta):
        
        while resposta != "yes" and resposta != "not" and resposta != "no":
            resposta = input("Do you want to save to a file? yes/not: ")
        if resposta == "yes":
            nome_do_arquivo = input("File name: ")
            arquivo = open("{}.txt".format(nome_do_arquivo), "a")  # Creates a file in writing format (.txt)
            arquivo.write("USER NAME: {}\n".format(nome))  # Write to the file
            arquivo.write("PASSWORD: {}\n".format(senha))  # Write to the file
            arquivo.write("LINK: {}".format(link))  # Write to the file
            arquivo.close()  # Closes the file
            sair = input("Do you want to leave? yes/not: ")
            while sair == "not" or sair == "no":
                sair = input("Do you want to leave? yes/not: ")
        elif resposta == "not" or resposta == "no":
            print()
            print()
            print("+--------------------------")
            print("|User name: {}".format(nome))
            print("|Password: {}".format(senha))
            print("|Link: {}".format(link))
            print("+--------------------------")
            print()
            sair = input("Do you want to leave? yes/not: ")
            while sair == "not" or sair == "no":
                sair = input("Do you want to leave? yes/not: ")


    def pergunta_link(resposta):
        link = ""
        while resposta != "yes" and resposta != "not" and resposta != "no":
            resposta = input("Want to enter the website link? yes/not: ")
        if resposta == "yes":
            link = input("Enter the website link: ") 
        return resposta, link  # returns the value of two variables
                



# BODY OF THE DOCUMENT
print()
print("-------------------------")
print("PASSWORD GENERATOR")
print("-------------------------")
print("Info: This program will generate a password to be used in registrations and accounts!")
print()

nome = input("Enter username: ")
quantidade = int(input("Enter the number of characters you want in the password: "))
pergunta_link = input("Want to enter the website link? yes/not: ")
pergunta_link, link = gerador.pergunta_link(pergunta_link)  # uses two variables to save the two values returned by the function's return

senha = gerador.gerador_senha(quantidade)
print("YOUR PASSWORD IS: {}".format(senha))
print()
pergunta = input("Do you want to save to a file? yes/not: ")
pergunta = gerador.pergunta_arquivo(pergunta)
