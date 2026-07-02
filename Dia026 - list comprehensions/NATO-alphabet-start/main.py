import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}

while True:
    try:
        word = input("Palavra: ").upper()
        output_list = [phonetic_dict[letter] for letter in word]
        print(output_list)
    except KeyError:
        print("Apenas letras podem ser digitadas.")

    
        
