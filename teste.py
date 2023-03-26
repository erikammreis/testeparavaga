
n = 13

fibonacci = [0, 1]
while fibonacci[-1] < n:
    fibonacci.append(fibonacci[-1] + fibonacci[-2])

if numero in fibonacci:
    print(f"{n} pertence à sequência de Fibonacci: {fibonacci}")
else:
    print(f"{n} não pertence à sequência de Fibonacci: {fibonacci}")
import json


with open('faturamento.json') as f:
    faturamento_mensal = json.load(f)

menor_faturamento = min(faturamento_mensal.values())
maior_faturamento = max(faturamento_mensal.values())


dias_no_mes = len(faturamento_mensal)
soma_faturamento = sum([v for v in faturamento_mensal.values() if v > 0])
media_mensal = soma_faturamento / dias_no_mes


dias_acima_da_media = len([v for v in faturamento_mensal.values() if v > media_mensal])


print(f"Menor faturamento: R${menor_faturamento:.2f}")
print(f"Maior faturamento: R${maior_faturamento:.2f}")
print(f"Número de dias com faturamento acima da média mensal: {dias_acima_da_media}")

faturamento_por_estado = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53,
}

faturamento_total = sum(faturamento_por_estado.values())

percentuais_por_estado = {}
for estado, faturamento in faturamento_por_estado.items():
    percentual = faturamento / faturamento_total * 100
    percentuais_por_estado[estado] = percentual

for estado, percentual in percentuais_por_estado.items():
    print(f"{estado}: {percentual:.2f}%")
texto = "hello world"

texto_invertido = ""
for i in range(len(texto)-1, -1, -1):
    texto_invertido += texto[i]

print(texto_invertido)
