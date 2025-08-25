cigarro = int(input("Quantos cigarros vc fuma por dia?: "))
anos = int(input("Há quantos anos vc fuma?: "))
total = ((cigarro*365*anos*10)/1440)
print(f"Vc perdeu cerca de {total:.2f} dias de vida fumando.")