# %%
cont = soma = 0
while True:
    altura = float(input(f"Digite a {cont+1}º altura: "))
    soma += altura
    cont += 1
    if cont == 4:
        break
print(f"A soma das 4 alturas são: {soma:.2f}m")