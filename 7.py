#varivel contador
cont = 0
#variaveis "maior e menor" ambas com o valor 0
maior = menor = 0
#enquanto o contador for menor que 5, faça:
while cont < 5:
#define a variavel num e pede que insira um valor
# que será atribuido a ela     
    num = int(input("Insira um numero:\n"))
# atualiza o contador    
    cont = cont + 1
# se o contador for equivalente/igual a 1.
# isso so vai acontecer uma vez.    
    if cont == 1:
#nesse caso se só um numero fosse digitado
# ele seria o maior e tambem o menor         
        maior = menor = num
#senão        
    else:
#se numero for maior que "maior"        
        if num > maior:
#a variavel maior ira receber o maior numero digitado           
            maior = num
# imprime o maior valor            
print("o maior numero é: ",maior)     
