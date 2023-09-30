from math import sqrt
from lib.Correntes import Correntes

import logging

def TensaoNeutro(tensao: list[complex], impedancias: list[complex]) -> complex:
    logger = logging.getLogger(__name__)

    correntes = Correntes(tensao, impedancias)
    SomaCorr = sum(correntes)
    SomaCorr = sqrt(( SomaCorr * SomaCorr.conjugate() ).real) # module
    Reatancia = []

    for imp in impedancias:
        Reatancia.append(((1 + 0j) / imp))

    SomaReatancia = sum(Reatancia)

    Vno = SomaCorr / SomaReatancia
    
    return Vno