# -*- coding: utf-8 -*-
import math


def deg2grad(deg):
    """
    deg2grad(90.00) --> 100.0
    """

    return deg * (10/9.0)


def grad2deg(grad):
    """
    grad2deg(100.00) --> 90.0
    """

    return grad * (9.0/10)


def grad2rad(grad):
    """
    grad2rad(100.0) --> 1.5707963267948968
    """

    return grad * (1.5707963267948968/100)


def rad2grad(rad):
    """
    rad2grad(1.5707963267948968) --> 100.0
    """

    return rad * (100/1.5707963267948968)


# ======================== for 3


def decimal_deg2rad(decimal_deg):
    """
    decimal_deg(1.5707963267948968) --> 90
    """

    return decimal_deg * (1.5707963267948968/90)


def rad2decimal_deg(rad):
    """
    rad2decimal_deg(1.5707963267948968) --> 90
    """

    return rad *(90/1.5707963267948968)


# ======================== for 4
