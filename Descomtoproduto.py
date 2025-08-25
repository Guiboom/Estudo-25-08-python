produto = float(input("Qual o valor do produto?: "))
desconto = float(input("Qual a porcentagem de desconto?: "))
valorDesc = ((produto/100)*desconto)
total = produto - valorDesc
print(f"O novo preço do produto é de {total}R$,")
print(f"E o valor do desconto é de {valorDesc}R$")