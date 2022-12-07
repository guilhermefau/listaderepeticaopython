#define nota como variavel inteiro e pede a entrada de um valor.
#em portugol seria algo como:
# inteiro nota
# escreva("informe uma nota entre 0 e 10: ")
# leia(nota) 

nota=int(input("informe uma nota entre 0 e 10: "))

#enquanto (nota for menor que 0) ou (maior que 10), faça:
while (nota<0)or(nota>10):
#imprima a mensagem "valor invalido".
        print("valor invalido")
#pede novamente que o valor da nota seja inserido ate que se cumpra a condição
#e o programa seja finalizado.
        nota=int(input("informe uma nota entre 0 e 10: "))