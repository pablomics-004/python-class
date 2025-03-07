import math
import sys

def calc_area(r):
    """
    DESCRIPTION: 
        Calcula el área de una circunferencia.
    ARGS:
        - r: radio del círculo proporionado por el usuario.
    RETURN:
        Área del círculo en u².
    """
    area = math.pi * r**2
    return area

# Cálculo del área del círculo
radius = 5
area = calc_area(radius)
print(f"\nArea of circle: {area} u².\n")