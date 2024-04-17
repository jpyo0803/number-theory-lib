import build.ntl as ntl
import random
from sympy import primefactors
import singleton_timer as st

def GenerateRandomCoprimeLessthanN(n: int):
    assert n >= 1
    num_tries = 0
    while True:
        x = random.randint(1, n)
        num_tries += 1
        if ntl.Gcd_uint64(x, n) == 1:
            return x, num_tries

def Factorize(n: int):
    assert n >= 2

    factors = primefactors(n)
    return factors

if __name__ == '__main__':
    pass

