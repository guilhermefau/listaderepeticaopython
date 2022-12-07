# define a variavel e pede que insira o valor que
# será atribuido a ela.
nome=str(input("Insira o nome: "))
#               validação
#   len retorna o numero de itens
# no caso len(nome) ira retornar o numero de caracteres
# que estao dentro da variavel "nome" 
# enquanto (tamanho(nome)for menor ou igual a 3), faça:
while (len(nome) <=3):
#exibe a mensagem informando.    
    print("Invalido")
#pede novamente até que se cumpra a condição.    
    nome=str(input("Insira o nome: "))

idade=int(input("Insira a idade: "))
while (idade < 0) or (idade > 150):
    print("Invalido")
    idade=int(input("Insira a idade: "))

salario=float(input("Insira o salario: "))
while salario < 0:
    print("Invalido")
    salario=float(input("Insira o salario: "))

sexo=str(input("Insira o sexo: "))
while sexo != "f" and sexo != "m":
    print("Invalido")
    sexo=str(input("Insira o sexo: "))

estadocivil=str(input("Insira o estado civil: "))
while estadocivil != "s" and estadocivil != "c" and estadocivil != "v" and estadocivil != "d" :
    print("Invalido")
    estadocivil=str(input("Insira o estado civil: "))

