from lib.PhaseToComplex import PhaseToComplex
from lib.ComplexToPhase import ComplexToPhase
from lib.TensaoFase import TensaoFase
from lib.FaseLinha import FaseLinha
from lib.Correntes import Correntes
import lib.DeltaEstrela as DeltaEstrela
import lib.EstrelaDelta as EstrelaDelta
from lib.TensaoNeutro import TensaoNeutro

import logging

logging.basicConfig(
    level="INFO", 
    format='[%(levelname)s][%(name)s] - %(message)s', 
    datefmt='%H:%M:%S')

def main():
    logger = logging.getLogger(__name__)

    Vref = 110 + 0j

    delta = TensaoFase(Vref)
    logger.info(f"Tensões de fase:\n\t{delta}")
    
    linha = FaseLinha(delta)
    logger.info(f"Tensões de linha:\n\t{linha}")

    Zy = DeltaEstrela.Impedancia([ 16 -28j, 14.8 -6.4j, 14+8j ])
    logger.info(f"Impedância transformada para estrela: \n\t{Zy}")

    Zd = EstrelaDelta.Impedancia(Zy)
    logger.info(f"Impedância transformada para delta: \n\t{Zd}")

    CorrLinha = Correntes(linha, Zy)
    logger.info(f"Corrente de linha do sistema: \n\t{CorrLinha}")
  
    # Vno calculo lembrar de por o menos
    Vno = TensaoNeutro(linha, Zy)
    logger.info(f"Tensão de neutro do sistema: \n\t{Vno}")

    Vfase=[]
    for i in range(len(linha)):
        Vfase.append( sum([linha[i], Vno]))
    logger.info(f"Tensoes de fase na carga: \n\t{Vfase}")

    CorrCorrigida = Correntes(Vfase, Zy)
    logger.info(f"Corrente de linha real do sistema: \n\t{CorrCorrigida}")

    Pot = [ (Vfase[0] * CorrCorrigida[0]), (Vfase[1] * CorrCorrigida[1]), (Vfase[2] * CorrCorrigida[2])]
    logger.info(f"Potência por linha do sistema: \n\t{Pot}")

    PotTot = sum(Pot)
    logger.info(f"Potência total do sistema: \n\t{PotTot}")


    
if __name__ == "__main__":
    main()