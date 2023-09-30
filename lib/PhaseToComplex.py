import logging
from math import pi, sin, cos

def PhaseToComplex(mod:float, ang:float) -> complex:
    logger = logging.getLogger(__name__)

    new_ang = ang*pi/180

    real = mod*cos(new_ang)
    img = mod*sin(new_ang)

    logger.debug(f"Converting {mod}/_{new_ang} to {complex(real, img)}")
    return complex(real, img)