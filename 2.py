# define user como uma variavel string(cadeia de caracteres) 
# e pede que entre com o valor que será atribuido a ela.
user=str(input("Insira o nome de usuario: "))
# define passwd como uma variavel string(cadeia de caracteres) 
# e pede que entre com o valor que será atribuido a ela.
passwd=str(input("Insira a senha: "))

#enquanto user for equivalente(igual, a mesma coisa) a passwd, faça:
while user == passwd:
#exibe a mensagem informando.
    print("A senha nao pode ser igual o nome de usuario")
#pede que insira novamente a senha até que cumpra a condição.    
    passwd=str(input("Insira a senha: "))
    