#ifndef NUMBER_THEORY_LIB_CPP_NTL_H_
#define NUMBER_THEORY_LIB_CPP_NTL_H_

#include <cstdint>
#include <iostream> 

using namespace std;

namespace jpyo0803 {

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

}

#endif 