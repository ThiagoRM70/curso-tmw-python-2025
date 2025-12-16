# %%
saldo_total = 0
while True:
    saldo = input("Digite o seu saldo: ")
    if saldo == "":
        break
    saldo_total += float(saldo)
print(f"O saldo total foi de {saldo_total:.2f}")