import logging

def Impedancia(delta: list[complex]) -> list[complex]:

    logger = logging.getLogger(__name__)

    soma: complex = sum(delta)
    
    R1 = (delta[0] * delta[2]) / soma
    logger.debug(f"R1: {R1}")

    R2 = (delta[0] * delta[1]) / soma
    logger.debug(f"R2: {R2}")

    R3 = (delta[1] * delta[2]) / soma
    logger.debug(f"R3: {R3}")
    
    return [R1, R2, R3]