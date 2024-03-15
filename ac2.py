#AC2 - EXERCÍCIO 1 - revisite a AC1
"""
Exercício 1: revisite a AC1
Desenvolva duas funções em Python:
1)eq_seg_grau(a, b, c), que recebe três valores reais e retorna as raízes de uma equação de segundo grau no formato ax² + bx + c = 0,
supondo as raízes sempre reais;
"""
def eq_seg_grau(a, b, c):
    delta = b * b - (4 * a * c)
    raiz1 = (-b + (delta ** 0.5) ) / (2*a)
    raiz2 = (-b - (delta ** 0.5) ) / (2*a)
    return raiz1, raiz2

print("Equaçao do 2o grau da forma: ax² + bx + c")
a = float( input("Informe o coeficiente a: ") )
b = float( input("Informe o coeficiente b: ") )
c = float( input("Informe o coeficiente c: ") )

raizes = eq_seg_grau(a, b, c)
print(f"As raizes da equação são: ", (raizes[0]), "e", (raizes[1]))

"""
Desenvolva duas funções em Python:
2)bissexto(ano), que recebe um valor inteiro e retorna um valor booleano, informando se o ano é bissexto ou não.
"""
def bissexto(ano):
    return(ano % 4 ==0 and ano % 100 != 0 or ano % 400 == 0)

ano = float(input("Informe o ano: "))

print(bissexto(ano))

#AC2 - EXERCÍCIO 2 - salário
"""
Desenvolva uma função em Python cujo nome é calcula_salario. Essa função recebe dois parâmetros posicionais reais,
valor_hora e num_horas, que correspondem ao valor do salário por hora e o número de horas trabalhadas no mês, respectivamente.
Além disso, a função tem um parâmetro-chave irpf, que calcula o imposto de renda a ser deduzido, cujo valor padrão é 0.275.
A função retorna o salário líquido de um funcionário, calculado como o produto do valor por hora pelo número de horas,
reduzido o percentual do imposto de renda dado.
"""
def calcula_salario(valor_hora, num_horas, irpf=0.275):
    return(valor_hora * num_horas - (valor_hora * num_horas * irpf))

valor_hora = float(input("Informe o valor do salário por hora: "))
num_horas = float(input("Informe o número de horas trabalhadas no mês: "))


salario_liquido = calcula_salario(valor_hora, num_horas, irpf=0.275)
print(f"O seu salário líquido é: R$", (salario_liquido))
