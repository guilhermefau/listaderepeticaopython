num=int(input("Insira um numero entre 1 e 10\npara ver a tabuada:\n"))
print("tabuada de ",num,"\n")
# para cada i no alcance de 11
# (11 pq de 0 a 10 são 11 numeros)
for i in range(11):
# imprime a tabuada 
#         numero X i = (numero*i) 
    print(num," x ", i, " = ", (num*i))
# essa ultima foi mais facil que o resto.    