m = float(input("Qual o valor do produto? "))
d = float(input("Qual a porcentagem (%) de desconto? (0-100): "))
pf = m - (m * d / 100)
print("O produto cujo valor era R${} após um desconto de {:.1f}% terá o valor de R${:.2f}" .format(m, d, pf))
