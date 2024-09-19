num1 = int(input('Digite o número inicial: '))
num2 = int(input('Digite o número final: '))
soma=0

for i in range(num1, num2):
    if i % 2  ==0:
        soma += i

print('A soma é: ', soma)