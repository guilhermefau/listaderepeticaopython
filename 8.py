#  Mesmo Programa anterior com alterações no final
cont = 0
soma = 0

while cont < 5:
    num = int(input("Insira um numero:\n"))
# atualiza a variavel soma
# realizando a soma do valor digitado com
# a variavel. exemplo do primeiro loop:
#     0  =  0   + valor digitado 
    soma = soma + num
# atualiza o contador, quando se repetir 5x
# cumpre a condição do while e o programa é finalizado    
    cont = cont + 1
#finalização do programa    
print("a soma dos numeros eh",soma) 
print("a media eh ",soma/5)
