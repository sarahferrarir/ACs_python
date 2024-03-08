#AC2 - EXERCÍCIO 1 - revisite a AC1
#AC1: exercício 1

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
print(f"As raizes da equação são: {raizes[0]} e {raizes[1]}")

#AC1: exercício 2

def bissexto(ano):
    return(ano % 4 ==0 and ano % 100 != 0 or ano % 400 == 0)

ano = float(input("Informe o ano: "))

print(bissexto(ano))

#AC2 - EXERCÍCIO 2 - salário

def calcula_salario(valor_hora, num_horas, irpf=0.275):
    return(valor_hora * num_horas - (valor_hora * num_horas * irpf))

valor_hora = float(input("Informe o valor do salário por hora: "))
num_horas = float(input("Informe o número de horas trabalhadas no mês: "))


salario_liquido = calcula_salario(valor_hora, num_horas, irpf=0.275)
print(f"O seu salário líquido é: R${salario_liquido}")
