#ifndef NUMBER_THEORY_LIB_CPP_NTL_H_
#define NUMBER_THEORY_LIB_CPP_NTL_H_

#include <cstdint>
#include <iostream> 
#include <cmath>
#include <vector>
#include <cassert>

using namespace std;

namespace jpyo0803 {

// NOTE(jpyo0803): Use Fermat's little theorem
// This algorithm only works when p is prime
// and k is not a multiple of p. That is gcd(k, p) == 1
// uint64_t FindKeyInvMod(uint64_t k, uint64_t p);

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
T IsPrime(T x) {
  if (x <= 1) return false;

  for (T i = 2; i <= static_cast<T>(sqrt(x)); ++i) {
    if (x % i == 0) {
      return false;
    }
  }
  return true;
}

}

#endif 