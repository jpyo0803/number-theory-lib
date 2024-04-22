#include "ntl.h"
#include <random>

namespace jpyo0803 {
  
std::vector<uint64_t> EratosthenesSieve(uint64_t n) {
  assert(n >= 2); // 'n' needs to be at least 2 

  std::vector<bool> prime_arr(n + 1, true);
  for (uint64_t i = 2; i * i <= n; ++i) {
    if (prime_arr[i]) {
      for (uint64_t j = i * i; j <= n; j += i) {
        prime_arr[j] = false;
      }
    }
  }

  std::vector<uint64_t> primes;
  for (uint64_t i = 2; i <= n; ++i) {
    if (prime_arr[i]) {
      primes.push_back(i);
    }
  }

  return primes;
}

uint64_t FindKeyInvModPrime(uint64_t key, uint64_t mod) {
  assert(key >= 1);
  assert(mod >= 1);
  return RepeatedSqrMod<uint64_t>(key, mod - 2, mod);
}

uint64_t FindKeyInvModNonPrime(uint64_t key, uint64_t mod, const std::vector<uint32_t>& factors) {
    assert(key >= 1);
    assert(mod >= 1);

    static bool first = true;
    static uint64_t phi;
    if (first) {
      phi = mod;
      for (auto factor : factors) {
          phi /= factor;
      }
      for (auto factor : factors) {
          phi *= (factor - 1);
      }
      first = false;
    }
    return RepeatedSqrMod<uint64_t>(key, phi - 1, mod);
}

}