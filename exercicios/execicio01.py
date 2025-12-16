# %%
palavra = str(input("Digite uma palavra: "))
contador_a = [x for x in palavra if x in 'aãâáAÂÃÁ']
contador = len(contador_a)
print(contador)