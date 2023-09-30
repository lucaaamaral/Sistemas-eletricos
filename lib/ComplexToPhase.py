import logging
from math import pi, atan, sqrt

def ComplexToPhase(val:complex) -> (float, float):
    logger = logging.getLogger(__name__)
    if (val.real == 0):
        val = complex(0.000000001, val.imag)
    ang = atan(val.imag/val.real)*180/pi
    mod = sqrt((val.real**2)+(val.imag**2))

    if (val.real<0):
        ang+=180

    logger.debug(f"Converting {val} to {mod}/_{ang}")
    return mod, ang