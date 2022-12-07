#define a população país A como inteiro e atribui o valor de 8000 habitantes.
popa=int=8000
#define a população país B como inteiro e atribui o valor de 20.000 habitantes.
popb=int=20000
#define a taxa de crescimento do país A como sendo 3% ou 0.030 ou 30/100.
txa=float=0.030
#define a taxa de crescimento do país A como sendo 1.5% ou 0.015 ou 15/100.
txb=float=0.015
#variavel que ira contar os anos ate que se cumpra a condição
ano=0
#enquanto a população de A for menor ou igual a população de B, faça:
while popa <= popb:
# pop de A = pop de A + pop de A multiplicado pela taxa de crescimento de A
# AQUI A VARIAVEL ESTÁ SENDO ATUALIZADA.
    popa = popa + (popa*txa)
# pop de B = pop de B + pop de B multiplicado pela taxa de crescimento de B    
# AQUI A VARIAVEL ESTÁ SENDO ATUALIZADA.
    popb = popb + (popb*txb)
# Atualiza a variavel "ano" adicionando 1 cada vez que o loop do while é
# executado   
    ano = ano + 1
#por fim o programa exibe a mensagem informando que em tantos anos bla bla bla.    
print("pais A ira ultrpassar ou igualar o pais b em",ano , "anos\n")
#desconsiderar esses dois ultimos 
print(popa)
print(popb)