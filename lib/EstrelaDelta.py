import logging

def Impedancia(estrela):
    logger = logging.getLogger(__name__)

    somaPonderada = (estrela[0] * estrela[1]) + (estrela[1] * estrela[2]) + (estrela[0] * estrela[2])
    
    logger.debug(f"SomaPonderada: {somaPonderada}")

    R1 = somaPonderada / estrela[2]
    logger.debug(f"R1: {R1}")
    
    R2 = somaPonderada / estrela[0]
    logger.debug(f"R2: {R2}")
    
    R3 = somaPonderada / estrela[1]
    logger.debug(f"R3: {R3}")

    return [R1, R2, R3]