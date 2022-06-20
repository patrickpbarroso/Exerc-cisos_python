import json

with open("dados.json", encoding='utf-8') as meu_json:
    dados = json.load(meu_json) #dados é uma LISTA DE DICIONÁRIOS

menor = dados[0] #Variável dicionário que captura o menor valor de faturamento
maior = dados[0] #Variável dicionário qeu captura o maior valor de faturamento
soma = 0 #Variável que captura a soma de todos os faturamentos (Será usada posteriormente no cálculo da média)
j = 0 #Iterador que conta quantos dias do mês foram registrados
dias = 0 #Variável que captura os dias em que o valor de faturamento foi maior que a média mensal

for var in dados: #For que calcula a soma de todos os faturamentos
    if var['valor']!=0:
        soma += var['valor']
        j+=1

media = soma/j #cálculo da média de faturamentos

for dado in dados: #For que calcula o menor faturamento, o maior faturamento e os dias em que o faturamento foi maior que a média
    if dado['valor']<menor['valor']:
        menor = dado
    if dado['valor']>maior['valor']:
        maior = dado
    if dado['valor']>media:
        dias += 1



print(f"O menor valor de faturamento ocorrido em um dia do mês foi {menor['valor']}. "
      f"\nO maior valor de faturamento occorido em um dia do mês foi {maior['valor']}."
      f"\nO valor de faturamento diário foi maior que a média mensal em {dias} dias. ")
