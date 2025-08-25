velocidade = int(input("Qual a velocidade do carro em km/h?: "))
if velocidade > 80:
    multa = (velocidade-80)*5
    print(f"Vc foi multado em {multa}R$.")
if velocidade <= 80:
    print("Vc não levou multa :)")