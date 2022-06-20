n = int(input("Digite o número para gerar a sequência de Fibonacci: "))
n1=0 #Primeiro fibonacci
n2=1 #Segundo fibonacci

print(n1, end=" ")
print(n2, end=" ")

while n2<n: #Estrutura de repetição que escreve todos os fibonacci menores ou iguais ao valor inserido
    aux = n1
    n1 = n2
    n2 = aux+n1
    if n2<=n:
        print(n2, end=" ")

if n2==n: #Estrutura de decisão que diz se o número inserido pertence ou não à sequência de fibonacci
    print("\nO número pertence a sequência de Fibonacci.")
else:
    print("\nO número não pertence a sequência de Fibonacci. ")
