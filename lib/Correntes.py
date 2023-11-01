from math import pi as pi

import logging

def Correntes(tensao, impedancias):
    logger = logging.getLogger(__name__)
    
    if (len(tensao) != len(impedancias)):
        raise Exception('Tensão e impedâncias não têm mesmo tamanho')
    
    corr = []

    for i in range(len(tensao)):
        corr.append(tensao[i]/impedancias[i])
    
    return corr