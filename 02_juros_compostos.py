# %%
def juros_compostos(aporte:int, taxa:float, anos:int)->float:
    """
    juros_compostos serve para calcular o retorno funanceiro a partiri de um aporte. 
    Deve-se considerar o valor, a taxa de juros atual e o tempo (em anos) para
    cálculo do valor a ser retornado.  
    
    :param aporte: um número inteiro, que representa o valor em R$
    :param taxa: um número float entre 0 e 1 que representa o valor da taxa
    :param anos: um número inteiro >= 1 que representa o tempo que o investimento terá liquidez
    """
    return aporte * (1 + taxa) ** anos
# %%
juros_compostos(taxa=0.13, anos=5, aporte=1000)