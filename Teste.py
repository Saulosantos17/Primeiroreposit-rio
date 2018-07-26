from random import randint
# rafael # # # 
# Saulo  # # # #

def sorteia_10_numeros():
    """Sorteia 10 números e coloca-os na lista."""
    sorteados = []
    while len(sorteados) < 5:
        a = randint(0, 10)
        if a not in sorteados:
            sorteados.append(a)
    return sorteados

rafael = [2, 4, 7, 9, 6]
saulo =  [3, 5, 1, 8, 10]

cont_rafael = 0
cont_saulo = 0

sorteados = sorteia_10_numeros()

for item1 in sorteados:
    if item1 in rafael:
        cont_rafael += 1
    if item1 in saulo:
        cont_saulo += 1

print(f'Saulo acertou:  {cont_saulo} vezes')
print(f'Rafael acertou: {cont_rafael} vezes')

if cont_saulo > cont_rafael:
    vencedor = 'SAULO'
elif cont_rafael > cont_saulo:
    vencedor = 'RAFAEL'
elif cont_rafael == cont_saulo:
    vencedor = 'Os dois acertaram a mesma quantidade'

print(f'O vencedor foi: {vencedor}')