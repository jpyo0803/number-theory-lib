#ifndef NUMBER_THEORY_LIB_CPP_NTL_H_
#define NUMBER_THEORY_LIB_CPP_NTL_H_

#include <cstdint>
#include <iostream> 

using namespace std;

namespace jpyo0803 {

template <typename T>
T RepeatedSqr(T base, T exp, T mod = 0) {
  if (exp == 0) {
    return 1;
  }

  T res = RepeatedSqr(base, exp / 2, mod);
  res *= res;

  if (mod != 0) res %= mod;
  if (exp % 2) res *= base;
  if (mod != 0) res %= mod;
  return res;
}

uint64_t RepeatedSqrTest(uint64_t base, uint64_t exp, uint64_t mod = 0) {
  if (exp == 0) {
    return 1;
  }


  uint64_t res = RepeatedSqrTest(base, exp / 2, mod);
  res *= res;

  if (mod != 0) res %= mod;
  if (exp % 2) res *= base;
  if (mod != 0) res %= mod;
  return res;
}

}

#endif 