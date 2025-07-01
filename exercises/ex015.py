d = int(input("Por quantos dias o carro foi alugado? "))
km = int(input("Quantos quilômetros o carro rodou? "))
p = (d * 60) + (km * 0.15)
print("O valor do aluguel é R${:.2f}" .format(p))
