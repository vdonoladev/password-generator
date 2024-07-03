from random import choice


class generator():

    def password_generator(size):
        characters = "0123456789abcdefghijklmnopqrstuwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ@!#$%&*()_+}{`^?;:>/-+.,"
        password = ""
        for i in range(size):
            password += choice(characters)
        return password

    def file_question(answer):

        while answer != "yes" and answer != "not" and answer != "no":
            answer = input("Você quer salvar em um arquivo? yes/not: ")
        if answer == "yes":
            file_name = input("Nome do arquivo: ")
            # Cria um arquivo em formato de escrita (.txt)
            file = open("{}.txt".format(file_name), "a")
            file.write("NOME DE USUÁRIO: {}\n".format(name))  # Escrever no arquivo
            file.write("SENHA: {}\n".format(password))  # Escrever no arquivo
            file.write("LINK: {}".format(link))  # Escrever no arquivo
            file.close()  # Fecha o arquivo
            exit = input("Voce quer ir embora? yes/not: ")
            while exit == "not" or exit == "no":
                exit = input("Voce quer ir embora? yes/not: ")
        elif answer == "not" or answer == "no":
            print()
            print()
            print("+--------------------------")
            print("|Nome de usuário: {}".format(name))
            print("|Senha: {}".format(password))
            print("|Link: {}".format(link))
            print("+--------------------------")
            print()
            exit = input("Voce quer ir embora? yes/not: ")
            while exit == "not" or exit == "no":
                exit = input("Voce quer ir embora? yes/not: ")

    def question_link(answer):
        link = ""
        while answer != "yes" and answer != "not" and answer != "no":
            answer = input("Quer inserir o link do site? yes/not: ")
        if answer == "yes":
            link = input("Insira o link do site: ")
        return answer, link  # retorna o valor de duas variáveis


# CORPO DO DOCUMENTO
print()
print("-------------------------")
print("GERADOR DE SENHAS")
print("-------------------------")
print("Informação: Este programa irá gerar uma senha para ser usada em registros e contas!")
print()

name = input("Insira nome de usuário: ")
quantity = int(
    input("Digite o número de caracteres que você deseja na senha: "))
question_link = input("Quer inserir o link do site? yes/not: ")
# usa duas variáveis para salvar os dois valores retornados pelo return da função
question_link, link = generator.question_link(question_link)

password = generator.password_generator(quantity)
print("SUA SENHA É: {}".format(password))
print()
question = input("Você quer salvar em um arquivo? yes/not: ")
question = generator.file_question(question)
