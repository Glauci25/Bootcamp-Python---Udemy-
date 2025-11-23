alphabet  = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def code(text, shift_number):
    decrypted_text = ''
    for letter in text:
        if letter not in alphabet:
            new_letter = letter
        else:
            idx = alphabet.index(letter.lower())
            new_idx = (idx + shift_number) % 26
            new_letter = alphabet[new_idx]
        decrypted_text += new_letter
    print(f'Aqui está o seu resultado codificado: {decrypted_text}')

def decode(decrypted_text, shift_number):
    decoded_text = ''
    for letter in decrypted_text:
        if letter not in alphabet:
            new_letter = letter
        else:
            idx = alphabet.index(letter.lower())
            new_idx = idx - shift_number
            new_letter = alphabet[new_idx]
        decoded_text += new_letter
    print(f'Aqui está o seu resultado decodificado: {decoded_text}')

print ('''
,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88 ''')

print('''  88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88''')

continuar = 'yes'
while continuar == 'yes':
    code_or_decode = input("Digite 'code' caso queira codificar ou 'decode' caso queira decodificar: ")
    if code_or_decode == 'code':
        orig_text = input('Digite um texto para codificar: ')
        shift = int(input('Digite um número shift: '))
        code(orig_text, shift)

    elif code_or_decode == 'decode':
        decoded_text = input('Digite a mensagem codificada: ')
        shift = int(input('Digite o número shift: '))
        decode(decoded_text, shift)
    continuar = input("Digite 'yes' para continuar e 'no' se quiser parar: ").lower()
else:
    print('Espero que tenha curtido!')