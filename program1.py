from lib.PhaseToComplex import PhaseToComplex
from lib.ComplexToPhase import ComplexToPhase
from lib.TensaoFase import TensaoFase
from lib.FaseLinha import FaseLinha
from lib.Correntes import Correntes
import lib.DeltaEstrela as DeltaEstrela
import lib.EstrelaDelta as EstrelaDelta
from lib.TensaoNeutro import TensaoNeutro
from math import sqrt

import logging

logging.basicConfig(
    level="INFO", 
    format='[%(levelname)s][%(name)s] - %(message)s', 
    datefmt='%H:%M:%S')

def main():
    logger = logging.getLogger(__name__)
    # Sa_ = (20 - 8.4j)/100
    # Sb_ = -(10 - 4j)/100
    # Sc_ = -(20 - 10.8j)/100
    # Sd_ = (0)
    # Se_ = (15 - 6j)/100


    # Va : complex = 1.05 + 0j
    # Vb : complex = ( (Sa_ / Va.conjugate()) - ( - 4.38j * Va ) ) / 4.38j
    # Vc : complex = ( (Sb_ / Vb.conjugate()) - ( 4.38j * Va ) - ( - 17.07j * Vb ) ) / 12.7j 
    # Vd : complex = ( (Sc_ / Vc.conjugate()) - ( 12.7j * Vb ) - ( - 28.57j * Vc ) ) / 15.87j 
    # Ve : complex = ( (Sd_ / Vd.conjugate()) - ( 15.87j * Vc ) - ( - 18.37j * Vd ) ) / 2.5j 
    
    # logger.info(ComplexToPhase(Va))
    # logger.info(ComplexToPhase(Vb))
    # logger.info(ComplexToPhase(Vc))
    # logger.info(ComplexToPhase(Vd))
    # logger.info(ComplexToPhase(Ve))


    # logger.info(ComplexToPhase( (100000/(sqrt(3)*138))*(Vb - Vc)/(0.25j*60/190.44) ) )

    Zm1 = PhaseToComplex(2.32, 36.87)
    Zm2 = PhaseToComplex(4.30, 36.87)
    Zm3 = PhaseToComplex(5.87, 31.79)
    Zm4 = PhaseToComplex(8.07, 31.41)

    Za = (Zm1*Zm2) / (Zm1+Zm2)
    Za += (0.1 + 0.02j) # + (0.5 + 0.1j)

    Zb = (Zm1*Zm3) / (Zm1+Zm3)
    Zb += (0.1 + 0.02j) # + (0.5 + 0.1j)

    Zc = (Zm1*Zm4) / (Zm1+Zm4)
    Zc += (0.1 + 0.02j) # + (0.5 + 0.1j)

    print(ComplexToPhase(Za))
    print(ComplexToPhase(Zb))
    print(ComplexToPhase(Zc))

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