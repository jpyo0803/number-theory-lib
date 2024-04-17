#include "ntl.h"

namespace jpyo0803 {
  
// uint64_t FindKeyInvMod(uint64_t k, uint64_t p) {
//   bool is_prime = IsPrime<uint64_t>(p);

//   uint64_t res;
//   if (is_prime) {
//     res = RepeatedSqrMod<uint64_t>(k, p - 2, p);
//   } else {
//     // res = 
//   }

//   return 0;
// }

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


}