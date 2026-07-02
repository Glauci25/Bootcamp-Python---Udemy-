'''
with open("file.txt") as file:
    contents = file.read()
    print(contents)
'''

with open("../teste/file.txt", "r", encoding="utf-8") as file:
    contents = file.read()

print("CONTEÚDO DO ARQUIVO:")
print(contents)