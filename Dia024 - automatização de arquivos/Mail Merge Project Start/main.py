#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("/Users/glauc/OneDrive/Desktop/Udemy/Python - Bootcamp 100 dias/Dia024 - automatização de arquivos/Mail Merge Project Start/Input/Names/invited_names.txt", mode= "r") as name_file: #tendo um arquivo com o nome de todos aberto...
    lista = [name.strip() for name in name_file.readlines()] #tranformei cada item da linha em um item de uma lista

with open("/Users/glauc/OneDrive/Desktop/Udemy/Python - Bootcamp 100 dias/Dia024 - automatização de arquivos/Mail Merge Project Start/Input/Letters/starting_letter.txt", mode= "r+") as letter: #tendo um arquivo base para todas as cartas...
    content = letter.read() #o content vai ser igual ao conteúdo da carta base

for name in lista: #para todos os nomes na lista feita anteriormente...
    nova_carta = content.replace("[name]", name) #nova_carta vai receber um novo conteúdo, porém substituindo a parte [name] por cada nome da lista

    #ainda dentro do loop: o 'write' vai criar um arquivo para cada nome da lista no local que foi indicado no 'with open...'
    with open(f"/Users/glauc/OneDrive/Desktop/Udemy/Python - Bootcamp 100 dias/Dia024 - automatização de arquivos/Mail Merge Project Start/Output/ReadyToSend/{name}_file.txt", mode="w") as new_file:
        new_file.write(nova_carta)
