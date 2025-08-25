kmperc = int(input("Quantos km foram percorridos com o carro alugado?: "))
dias = int(input("Quantos dias o carro foi alugado?: "))
preco = (dias*60)+(kmperc*0.15)
print(f"O valor total com {kmperc}Km e {dias} dias é de {preco}R$")