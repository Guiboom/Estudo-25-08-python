salario = float(input("Qual é o seu salario?: "))
aumento = float(input("Qual é a porcentagem de aumento: "))
novosalaio = ((salario/100)*aumento)+salario
print(f"Com o aumento de {aumento}%, o seu novo salário é de {novosalaio}R$")