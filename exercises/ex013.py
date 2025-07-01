m = float(input("Qual o salário? R$"))
d = float(input("Qual a porcentagem (%) de aumento? (0-100): "))
pf = m + (m * d / 100)
print("O salário cujo valor era R${} após um aumento de {:.1f}% terá o valor de R${:.2f}" .format(m, d, pf))
