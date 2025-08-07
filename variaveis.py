nome = "Arthur"
Idade = "16 anos"
ano_nascimento = 2009

print ("Nome:",nome)
print ("Idade:",Idade)
print ("Ola, eu me chamo", nome,"tenho", Idade,"e nasci em", ano_nascimento)

# Tipos de variaveis
nome = "Arthur"
idade = "16 anos"
altura = "1.61"
ativo = True


print("O tipo da variavel nome é:",type(nome))
print("O tipo da variavel altura é:",type(idade))
print("O tipo da variavel altura é:",type(altura))
print("O tipo da variavel ativo é:",type(ativo))


# operadores
num1 = 3
num2 = 4
divi_inteira= num1//num2 #divisao comum
soma = num1 + num2
divi = num1 /num2
mul = num1 * num2
sub = num1 - num2
expo = num1**num2
resto = num1 %2

print("Resultado da soma", num1, "+", num2, "=", soma)
print("Resultado da divisão", num1, "/", num2, "=", divi)
print("Resultado da multiplicação", num1, "*", num2, "=", mul)
print("Resultado da subtração", num1, "-", num2, "=", sub)
print("Resultado do resto de",num1, "=", resto)
print("Resultado do exponencial",num1, "=", expo)
print("Resultado da divisão inteira", num1, "=", divi_inteira)

print()
print(30*'-', 'operadores de comparação', 30* "-")
#operadores de comparação
num1 > num2
num1 < num2
num1 == num2
num1 >= num2
num1 <= num2
num1 != num2

ano = 2025
print("Ano atual:", ano)
ano += 1
print("Ano acrecido de +1:", ano)
ano -= 1
print("Ano decrecido de -1:", ano)

#operadores logicos
#AND, OR, NOT

print()
print (30*'-', 'entrada de dados', 30* "-")
nome_usuario = input("Digite seu nome:")
print('Seja bem-vindo ao sistema puthon', nome_usuario)

print()
print(30* "Calculadora", 30* '-')
numero1= float(input("Digite o primeiro numero:"))
numero2 = float(input("Digite o segundo numero:"))

soma = numero1 + numero2
divi = numero1 / numero2
sub = numero1 - numero2
mul = numero1 * numero2

print ("Resultado da soma", numero1, '+', numero2, "=", soma)
print ("Resultado da divisão", numero1, '/', numero2, "=", divi)
print ("Resultado da multiplicação", numero1, '*', numero2, "=", mul)
print ("Resultado da subtração", numero1, '-', numero2, "=", sub)

#tipos de dados
#float = numeros reais, ou seja, tem ",", exemplo: 5.2
#int = numeros inteiros, exemplo: 5
#str = texto, exemplo: "nome"
#bool = verdadeiro ou falso, exemplo: True ou False
print("Resultado da soma", numero1, '+', numero2, "=", soma)
print("Resultado da divisão", numero1, '/', numero2, "=", divi)
print("Resultado da multiplicação", numero1, '*', numero2, "=", mul)
print("Resultado da subtração", numero1, '-', numero2, "=", sub)

print()
print(30* '-', 'Convertendo tipos de dados', 30* '-')

ano_nascido = input("Digite seu ano de nascimento:")
print(type(ano_nascido))
#convertendo para inteiro
ano_nascido = int(ano_nascido)
print(type(ano_nascido))
cpf= input("Digite seu CPF")
telefone= input("Digite seu telefone:")
saudacao= input("Digite seu nome:")

print(20*'-', 'Dados pessoais,', 20*'-')
print('Nome:', saudacao)
print("CPF", cpf,'telefone', telefone)
print(50*'-')

