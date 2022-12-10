from __future__ import annotations
import math
from colors import gradient
rp = [-1029.86559098,  2344.5778132 , -1033.38786418,  -487.3693808 ,
         298.50245209,   167.25393272]
gp = [  551.32444915, -1098.30287507,   320.71732031,   258.50778539,
         193.11772901,    30.32958789]
bp = [  222.95535971, -1693.48546233,  2455.80348727,  -726.44075478,
         -69.61151887,    67.591787  ]

def sgn(a):
    return 1 if a>0 else -1

def is_prisonier(z0, c):
    for i in range(30):
        z0 = z0.pow(2) + c
        if abs(z0.rho) > 2:
            return False,gradient(i/30, rp, gp, bp)
    return True, (255,250,255)


class Complex:
    rho = None
    phi = None
    a = None
    b = None
    def __init__(self, rho: float, phi: float):
        self.rho = rho
        self.phi = phi
        self.a = self.rho * math.cos(self.phi)
        self.b = self.rho * math.sin(self.phi)

    def get_algebra(self):
        return self.a, self.b 

    def pow(self, n: int) -> Complex:
        return Complex(self.rho**n, self.phi*n)

    def __mul__(self, other: Complex):
        return Complex(self.rho*other.rho, self.phi+other.phi)

    def __add__(self, other: Complex):
        return Complex.from_algebra(self.a+other.a, self.b+other.b)

    def __str__(self):
        a,b = self.get_algebra()
        return f"{self.rho:.3g}cis({self.phi:.3g}) || {a:.3g}+{b:.3g}i"

    def from_trigo(rho: float, phi: float) -> Complex:
        return Complex(rho, phi)

    def from_algebra(a: float, b: float) -> Complex:
        module = math.sqrt(a**2 + b**2)
        if a == 0:
            arg = math.pi/2 * sgn(b)
        else:
            arg = math.atan(b/a)
        if a < 0:
            arg += math.pi
        c = Complex(module, arg)
        c.a = a
        c.b = b
        return c