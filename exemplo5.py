#fatorial de um numero

numero = int(input('Digite um inteiro positivo: '))
fatorial = 1

for i in range(1,numero+1):
    fatorial = fatorial *i

print('O fatorial é: ', fatorial)