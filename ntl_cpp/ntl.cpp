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

std::vector<uint64_t> GenerateKeySetA(uint64_t mod, int n) {
  if (n <= 1) {
    throw std::invalid_argument("The upper bound must be greater than 1 to include at least one possible return value.");
  }

  std::vector<uint64_t> key_set(n);

  for (int i = 0; i < n; ++i) {
    key_set[i] = GenerateRandomCoprimeLessthanN<uint64_t>(mod);
  }

  return key_set;
}

std::vector<uint64_t> GenerateKeySetB(uint64_t mod, int n) {
  if (n <= 1) {
    throw std::invalid_argument("The upper bound must be greater than 1 to include at least one possible return value.");
  }

  static std::random_device rd;  // Non-deterministic random device
  static std::mt19937 rng(rd()); // Random-number engine used (Mersenne-Twister in this case)
  std::uniform_int_distribution<uint64_t> uni(0, mod - 1);

  std::vector<uint64_t> key_set(n);

  for (int i = 0; i < n; ++i) {
    key_set[i] = uni(rng);
  }

  return key_set;
}

// std::vector<std::vector<uint32_t>> FindKeyInvModNonPrimeArray2D(const std::vector<uint32_t>& key_set_a1, const std::vector<uint32_t>& key_set_a2, uint64_t mod, const std::vector<uint32_t>& factors) {
//   assert(mod == (1LL << 32)); // for now I only use 2^32

//   int M = key_set_a1.size();
//   int N = key_set_a2.size();
//   std::vector<std::vector<uint32_t>> key_inv_arr(M, std::vector<uint32_t>(N));

//   for (int i = 0; i < M; ++i) {
//     for (int j = 0; j < N; ++j) {
//       key_inv_arr[i][j] = static_cast<uint32_t>(FindKeyInvModNonPrime(static_cast<uint64_t>(key_set_a1[i]) * key_set_a2[j], mod, factors));
//     }
//   }
//   return key_inv_arr;
// }

}