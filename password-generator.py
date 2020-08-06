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
            answer = input("Do you want to save to a file? yes/not: ")
        if answer == "yes":
            file_name = input("File name: ")
            file = open("{}.txt".format(file_name), "a")  # Creates a file in writing format (.txt)
            file.write("USER NAME: {}\n".format(name))  # Write to the file
            file.write("PASSWORD: {}\n".format(password))  # Write to the file
            file.write("LINK: {}".format(link))  # Write to the file
            file.close()  # Closes the file
            exit = input("Do you want to leave? yes/not: ")
            while exit == "not" or exit == "no":
                exit = input("Do you want to leave? yes/not: ")
        elif answer == "not" or answer == "no":
            print()
            print()
            print("+--------------------------")
            print("|User name: {}".format(name))
            print("|Password: {}".format(password))
            print("|Link: {}".format(link))
            print("+--------------------------")
            print()
            exit = input("Do you want to leave? yes/not: ")
            while exit == "not" or exit == "no":
                exit = input("Do you want to leave? yes/not: ")


    def question_link(answer):
        link = ""
        while answer != "yes" and answer != "not" and answer != "no":
            answer = input("Want to enter the website link? yes/not: ")
        if answer == "yes":
            link = input("Enter the website link: ") 
        return answer, link  # returns the value of two variables
                



# BODY OF THE DOCUMENT
print()
print("-------------------------")
print("PASSWORD GENERATOR")
print("-------------------------")
print("Info: This program will generate a password to be used in registrations and accounts!")
print()

name = input("Enter username: ")
quantity = int(input("Enter the number of characters you want in the password: "))
question_link = input("Want to enter the website link? yes/not: ")
question_link, link = generator.question_link(question_link)  # uses two variables to save the two values returned by the function's return

password = generator.password_generator(quantity)
print("YOUR PASSWORD IS: {}".format(password))
print()
question = input("Do you want to save to a file? yes/not: ")
question = generator.file_question(question)
