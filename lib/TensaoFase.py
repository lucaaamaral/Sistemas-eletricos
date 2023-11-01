from lib.ComplexToPhase import ComplexToPhase
from lib.PhaseToComplex import PhaseToComplex
from math import pi as pi
import logging

def TensaoFase (tensaoRef: complex, numFases: int=3):
    
    logger = logging.getLogger(__name__)

    a=360/numFases
    logger.debug(f"Phase ofset set to {a}")

    mod, ang = ComplexToPhase(tensaoRef)

    tensoes=[]
    for i in range(numFases):
        logger.debug(f"Phase tension {i} is {mod}/_{ang+a*i}")
        tensoes.append(PhaseToComplex(mod, ang+a*i))
    
    return tensoes

