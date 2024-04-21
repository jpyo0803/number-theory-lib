import build.ntl as ntl_cpp
import random
from sympy import primefactors
import singleton_timer as st


def GenerateRandomCoprimeLessthanN(n: int):
    assert n >= 1
    num_tries = 0
    while True:
        x = random.randint(1, n)
        num_tries += 1
        if ntl_cpp.Gcd_uint64(x, n) == 1:
            return x, num_tries


def Factorize(n: int):
    assert n >= 2

    factors = primefactors(n)
    return factors


def FindKeyInvModPrime(key: int, mod: int):
    assert key >= 1  # key is always larger or equal to 1
    assert mod >= 1

    # if mod is prime, apply Fermat's Little Theorem
    return ntl_cpp.RepeatedSqrMod_uint64(key, mod - 2, mod)


factors = None
phi = None


# Fastest
def FindKeyInvModNonPrime(key: int, mod: int):
    assert key >= 1  # key is always larger or equal to 1
    assert mod >= 1
    global factors
    global phi  # compute phi only once
    if factors is None:
        factors = primefactors(mod)
        phi = mod
        for factor in factors:
            phi //= factor
        for factor in factors:
            phi *= (factor - 1)
    return ntl_cpp.RepeatedSqrMod_uint64(key, phi - 1, mod)


if __name__ == '__main__':
    pass
