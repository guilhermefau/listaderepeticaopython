#define a variavel num como inteiro e com
#  o valor de "0"
num=int=0
#enquanto num for menor ou igual a 49, faça:
#por que 49 e nao 50? 
while num<=49:
#atualiza a variavel somando + 1    
    num = num+1
#se o resto da divisão por dois for diferente de 0
# isso significa que esse numero será impar.  
    if num%2 != 0:
#imprime de acordo com a condição do if(se)
# ou seja somente os numeros impares.        
        print(num)
