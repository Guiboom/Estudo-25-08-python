dias = float(input("Digite quantos dias: "))
horas = float(input("Digite quantos horas: "))
minutos = float(input("Digite quantos minutos: "))
segundos = float(input("Digite quantos segundos: "))
total = (dias*86400)+(horas*3600)+(minutos*60)+segundos
print(f"A soma total é {total} segundos")