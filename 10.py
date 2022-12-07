#se chegou ate aqui ja deve saber o que é isso
#senao é so voltar as imagens dos programas anteriores 
num1=int(input("insira o numero inicial: "))
num2=int(input("insira o numero final: "))
#enquanto num2 for menor que num1, faça:
#isso aqui é pq o numero final nao pode ser
# menor que o inicial, daria muito errado kk! 
while num2<num1:
# só pra dizer que voce colocou errado e pedir novamente    
    print("o valor inicial deve ser menor que o valor final!\n")
    num1=int(input("insira o numero inicial: "))
    num2=int(input("insira o numero final: "))
#aqui onde ta a cereja do bolo
#senao:      
else:
# para cada "i" dentro do intervalo de num1 e num2 incremente 1:
# traduzindo do ingles range é algo como intervalo,faixa,alcance e etc.
# range funciona da seguinte forma
# range(numeroinicial, numerofinal, incremento) nesse caso aqui.
    for i in range(num1,num2,1):
#aqui vai ser impresso na tela todos o valores dentro do intervalo
# do range aí vai depender dos numeros que vc digitou         
        print(i)
