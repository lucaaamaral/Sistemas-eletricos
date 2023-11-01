from math import sqrt
from lib.PhaseToComplex import PhaseToComplex
from lib.ComplexToPhase import ComplexToPhase
import logging

def FaseLinha(delta):
    logger = logging.getLogger(__name__)

    var = PhaseToComplex(sqrt(3), 30)
    linha=[]
    for item in delta:
        tmp = item/var
        linha.append(tmp) # TODO: unballanced source
        logger.debug(f"PhaseToLine from {ComplexToPhase(item)} to {ComplexToPhase(tmp)}")

    return linha    