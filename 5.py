#Mesmo programa anterior a unica mudança é que os valores serao
#inseridos pelo usuario.

#define a população país A como inteiro e pede que seja inserido
#o valor que será atribuido a ela.
popa=int(input("Insira a população do pais A: "))
#enquanto a População de A for menor que 0, faça:
while popa <0:
    print("Invalido")
#pede novamente ate que se cumpra a condição de ser maior que 0.    
    popa=int(input("Insira a população do pais A: "))

popb=int(input("Insira a população do pais B: "))
while popb <0:
    print("Invalido")
    popb=int(input("Insira a população do pais B: "))

txa=float(input("Insira a taxa de crescimento do pais A: "))
while txa <0:
    print("Invalido")
    txa=int(input("Insira taxa de crescimento do pais A: "))

txb=float(input("Insira a taxa de crescimento do pais B: "))
while txb <0:
    print("Invalido")
    txb=int(input("Insira taxa de crescimento do pais A: "))

ano=0

while popa <= popb:
    popa = popa + (popa*txa) 
    popb = popb + (popb*txb)
    ano = ano + 1
print("pais A ira ultrpassar ou igualar o pais b em",ano , "anos\n")
print(popa)
print(popb)