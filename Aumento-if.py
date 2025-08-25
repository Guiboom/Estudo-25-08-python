salariobase = float(input("Digite o seu salario: "))
salario = salariobase
if salario > 1250:
    nvsalario = (salario*1.10)
    nvsalario2 = nvsalario
    aumento = nvsalario-salario
    salario = salariobase
if salario <= 1250:
    nvsalario = (salario*1.15)
    nvsalario2 = nvsalario
    aumento = nvsalario-salario
    salario = salariobase
    
print(f"O seu novo salario é {nvsalario2:.2f}R$, com aumento de {aumento:.2f}R$.")