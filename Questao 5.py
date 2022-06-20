palavra = input("Digite a string que deseja inverter: ")
tamanho = 0 #variável que conta quantos caracteres a palavra tem
caracteres = [] #lista que armazena cada caracter da palavra
inversa = [] #lista que armazena os caracteres da palavra na ordem inversa
palavra_invertida = "" #resultado. a palavra invertida

for caractere in palavra: #preenchimento da lista com cada caracter da palavra
    caracteres.append(caractere)
    tamanho += 1

for i in range (0,tamanho): #preenchimento da lista com cada caracter da palavra na ordem inversa
    inversa.append(caracteres[tamanho-(1+i)])

for car in inversa: #construção do resultado (a palavra na ordem invertida)
    palavra_invertida = palavra_invertida + car

print(f"A palavra inserida, mas com os caracteres invertidos, é: {palavra_invertida}")
