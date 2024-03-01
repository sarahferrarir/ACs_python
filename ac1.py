#AC1: exercício 1

print("Equaçao do 2o grau da forma: ax² + bx + c")
a = float( input("Informe o coeficiente a: ") )
b = float( input("Informe o coeficiente b: ") )
c = float( input("Informe o coeficiente c: ") )
delta = b * b - (4 * a * c)

raiz1 = (-b + (delta ** 0.5) ) / (2*a)
raiz2 = (-b - (delta ** 0.5) ) / (2*a)
print("As raizes da equação são: ",raiz1,"e",raiz2)

#AC1: exercício 2

ano = float(input("Informe o ano: "))
print(ano % 4 ==0 and ano % 100 != 0 or ano % 400 == 0)