import json

with open("dados2.json", encoding='utf-8') as meu_json:
    dados2 = json.load(meu_json) #leitura dos dados

soma = 0 #Variável que captura o total de faturamento de todos os estados

for var in dados2: #Cálculo do total de faturamento de todos os estados
    soma+=var["valor"]

print(f"-----Percentual de representação que cada estado teve dentro do valor total mensal da distribuidora------"
      f"\nSão Paulo (SP): {(dados2[0]['valor']/soma)*100}%"
      f"\nRio de Janeiro (RJ): {(dados2[1]['valor']/soma)*100}%"
      f"\nMinas Gerais (MG): {(dados2[2]['valor']/soma)*100}%"
      f"\nEspírito Santo (ES): {(dados2[3]['valor']/soma)*100}%"
      f"\nOutros: {(dados2[4]['valor']/soma)*100}%")
    #O cálculo da porcentagem é feito dividindo-se o= faturamento do estado pelo total de faturamento de todos os estados
    #Multiplica-se por 100 para obter o valor em porcentagem
