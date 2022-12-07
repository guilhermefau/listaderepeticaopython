# Mesmo programa anterior só que no final
# aqui ele vai somar os valores 
num1=int(input("insira o numero inicial: "))
num2=int(input("insira o numero final: "))
soma=0
while num2<num1:
    print("o valor inicial deve ser menor que o valor final!\n")
    num1=int(input("insira o numero inicial: "))
    num2=int(input("insira o numero final: "))
else:
    for i in range(num1,num2,1):
#soma dos valores de i no range do for
#         0  =  0 + i         
        soma = soma+i
print(soma)       
#nem eu entendi so sei que deu certo.
