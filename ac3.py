#Exercício 1: triângulos
"""Desenvolva uma função determina_tipo_triangulo que recebe três lados de um
triângulo e retorna uma string, "Escaleno", "Isósceles" ou "Equilátero", conforme
o tipo do triângulo. A função deve retornar "Não é um triângulo" se os três lados
não formarem um triângulo. """

def determina_tipo_triangulo(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        if a == b == c:
            return "Equilátero"
        elif a == b or a == c or b == c:
            return "Isósceles"
        else:
            return "Escaleno"
    else:
        return "Não é um triângulo"

tipo_triangulo = determina_tipo_triangulo(5, 5, 5)
print((tipo_triangulo))

#Exercício 2: dia da semana
"""Desenvolva uma função dia_semana que recebe um número inteiro e retorna uma
string indicando o dia da semana equivalente, considerando que o dia da semana
igual a 1 é o domingo, 2 é segunda-feira, etc. A função deve retornar uma string
vazia caso o número seja inválido. Use a função abaixo como teste:"""

def dia_semana(num):
    dias_semana = ["Domingo", "Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado"]
    if 1 <= num <= 7:
        return dias_semana[num - 1]
    else:
        return ""

num_dia = 5
nome_dia = dia_semana(num_dia)

if nome_dia:
    print((nome_dia))
else:
    print("")

#Exercício 3: calculadora simples
"""Desenvolva funções de operações aritméticas soma, subtracao, multiplicacao e
divisao, que recebem dois números cada uma e retornam o resultado da operação indicada.
Em seguida, crie uma função que elabora uma interface por linha de comando (CLI), que lê
dois números e uma operação e exibe na tela o valor do resultado, ou exibe "operação
inválida" se o usuário inserir uma mensagem diferente das quatro operações."""

def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "Divisão por zero"

def escolher_operacao(a, b, operacao):
    if operacao == "+":
        return soma(a, b)
    elif operacao == "-":
        return subtracao(a, b)
    elif operacao == "*":
        return multiplicacao(a, b)
    elif operacao == "/":
        return divisao(a, b)
    else:
        return "Operação inválida"

def calculadora():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    operacao = input("Escolha a operação: ").lower()

    resultado = escolher_operacao(num1, num2, operacao)
    if resultado != "Operação inválida":
        print(f"Resultado da operação ", (operacao), ":", (resultado))
    else:
        print("Operação inválida")

calculadora()
