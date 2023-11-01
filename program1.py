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

    z2 = ComplexToPhase(complex(20,-8.4)/(1.05*100))
    logger.info(z2)
    # z2 = PhaseToComplex(31.11, 33.16)
    # logger.info(z2)
    # z2 = PhaseToComplex(36.28, 10.76)
    # logger.info(z2)

    # Vref = 380 + 0j

    # TFase = TensaoFase(Vref)
    # logger.info(f"Tensões de fase:\n\t{TFase}")
    
    # TFase[1] = 0j

    # linha = FaseLinha(TFase)
    # logger.info(f"Tensões de linha:\n\t{linha}")

    # Zy = DeltaEstrela.Impedancia([ PhaseToComplex(1.358, 40.281), 
    #                                PhaseToComplex(1.711, 433.665), 
    #                                PhaseToComplex(1.221, 1.774) ])
    # logger.info(f"Impedância transformada para estrela: \n\t{Zy}")

    # # Zd = EstrelaDelta.Impedancia(Zy)
    # # logger.info(f"Impedância transformada para delta: \n\t{Zd}")

    # CorrLinha = Correntes(linha, Zy)
    # logger.info(f"Corrente de linha do sistema: \n\t{CorrLinha}")
  
    # # Vno calculo lembrar de por o menos
    # Vno = TensaoNeutro(linha, Zy)
    # logger.info(f"Tensão de neutro do sistema: \n\t{Vno}")

    # Vfase=[]
    # for i in range(len(linha)):
    #     Vfase.append( sum([linha[i], Vno]))
    # logger.info(f"Tensoes de fase na carga: \n\t{Vfase}")

    # CorrCorrigida = Correntes(Vfase, Zy)
    # logger.info(f"Corrente de linha real do sistema: \n\t{CorrCorrigida}")

    # Pot = [ (Vfase[0] * CorrCorrigida[0]), (Vfase[1] * CorrCorrigida[1]), (Vfase[2] * CorrCorrigida[2])]
    # logger.info(f"Potência por linha do sistema: \n\t{Pot}")

    # PotTot = sum(Pot)
    # logger.info(f"Potência total do sistema: \n\t{PotTot}")


    
if __name__ == "__main__":
    main()