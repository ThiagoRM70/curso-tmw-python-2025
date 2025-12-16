# Construa um program que realiza o sorteio de um número entre 1 e 15.
# O usuário terá 3 chances de acertar o valor.
# A cada tentativa você deve  informar se o chute e maior ou menor que o número sorteado.
# Caso o usuário acerte, dê os parabêns.

def get_input():
    while True:
        try:
            numero_usuario = int(input("Digite um número entre 1 e 15: "))
        except ValueError as err:
            print("Valor inválido!")
            continue

        if 1 <= numero_usuario <= 15:
            return numero_usuario
        
        print("Valor inválido! O valor deve ser entre 1 e 15")

def check_numbers(sorteio:int, usuario:int)->bool:
    if usuario == sorteio:
        print("Parabéns! Você se tornou um milionário!")
        return True

    elif sorteio > sorteio: 
        print(f"Número muito alto. Tente novamente")
        return False

    else:
        print(f"Número muito baixo. Tente novamente")
        return False

from random import randint

numero_sorteio = randint(1, 15)

for i in range(3):
    numero_usuario = get_input()
    
    if check_numbers(sorteio=numero_sorteio, usuario=numero_usuario):
        break

else:
    print("Suas tentativas acabaram!!")