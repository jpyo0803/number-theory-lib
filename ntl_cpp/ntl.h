#ifndef NUMBER_THEORY_LIB_CPP_NTL_H_
#define NUMBER_THEORY_LIB_CPP_NTL_H_

#include <cstdint>
#include <iostream> 
#include <cmath>
#include <vector>
#include <cassert>
#include <random>
#include <numeric>

using namespace std;

namespace jpyo0803 {



std::vector<uint64_t> EratosthenesSieve(uint64_t n);

template <typename T>
T RepeatedSqrMod(T base, T exp, T mod) {
  if (exp == 0) {
    return 1;
  }

  T res = RepeatedSqrMod(base, exp / 2, mod);
  res *= res;
  res %= mod;

  if (exp % 2) res *= base;
  return res % mod;
}

template <typename T>
T RepeatedSqr(T base, T exp) {
  if (exp == 0) {
    return 1;
  }

  T res = RepeatedSqr(base, exp / 2);
  res *= res;

  if (exp % 2) res *= base;
  return res;
}

template <typename T>
T Gcd(T x, T y) {
  if (y == 0) return x;
  return Gcd(y, x % y);
}

template <typename T>
T StdGcd(T x, T y) {
  return std::gcd(x, y);
}


template <typename T>
T IsPrime(T x) {
  if (x <= 1) return false;

  for (T i = 2; i <= static_cast<T>(sqrt(x)); ++i) {
    if (x % i == 0) {
      return false;
    }
  }
  return true;
}

template <typename T>
T GenerateRandomCoprimeLessthanN(T n) {
  assert(n >= 1);

  static std::random_device rd;  // Non-deterministic random device
  static std::mt19937 rng(rd()); // Random-number engine used (Mersenne-Twister in this case)
  std::uniform_int_distribution<T> uni(1, n - 1);

  while (true) {
    T x = uni(rng);
    if (Gcd<T>(x, n) == 1) {
      return x;
    }
  }
}

uint64_t FindKeyInvModPrime(uint64_t key, uint64_t mod);

uint64_t FindKeyInvModNonPrime(uint64_t key, uint64_t mod, const std::vector<uint32_t>& factors);

}

#endif 