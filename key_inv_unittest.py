
import ntl
import build.ntl as ntl_cpp
import unittest
import random
import singleton_timer as st
from sympy import primefactors


class NtlTest(unittest.TestCase):
    def test_keyinvmod_composite_mod(self):
        timer = st.SingletonTimer()

        num_test = 100
        pass_cnt = 0
        mod = 2**32
        for _ in range(num_test):
            while True:
                key = random.randint(1, mod - 1)
                if ntl_cpp.Gcd_uint64(key, mod) == 1:
                    break
            t = timer.start(tag="comp. keyinvmod latency",
                            category="comp. keyinvmod latency")
            key_inv = ntl.FindKeyInvModNonPrime(key, mod)
            timer.end(t)
            self.assertEqual((key * key_inv) % mod, 1)
            pass_cnt += 1

        print(f"'test_keyinvmod_composite_mod' passed {pass_cnt} / {num_test}")
        timer.display_summary()

    def test_keyinvmod_prime_mod(self):
        timer = st.SingletonTimer()

        num_test = 100
        pass_cnt = 0
        mod = 4294967291
        for _ in range(num_test):
            assert ntl_cpp.IsPrime_uint64(mod)
            key = random.randint(1, mod - 1)
            t = timer.start(tag="prime. keyinvmod latency",
                            category="prime. keyinvmod latency")
            key_inv = ntl.FindKeyInvModPrime(key, mod)
            timer.end(t)
            self.assertEqual((key * key_inv) % mod, 1)
            pass_cnt += 1

        print(f"'test_keyinvmod_prime_mod' passed {pass_cnt} / {num_test}")
        timer.display_summary()

    # def test_keyinvmod_random_mod(self):
    #     timer = st.SingletonTimer()

    #     num_test = 100
    #     pass_cnt = 0
    #     for _ in range(num_test):
    #         mod = random.randint(2, 2**32)
    #         if not ntl_cpp.IsPrime_uint64(mod):
    #             while True:
    #                 key = random.randint(1, mod - 1)
    #                 if ntl_cpp.Gcd_uint64(key, mod) == 1:
    #                     break
    #         else:
    #             key = random.randint(1, mod - 1)
    #         t = timer.start(tag="random keyinvmod latency",
    #                         category="random keyinvmod latency")
    #         key_inv = ntl.FindKeyInvMod(key, mod)
    #         timer.end(t)
    #         self.assertEqual((key * key_inv) % mod, 1)
    #         pass_cnt += 1

    #     print(f"'test_keyinvmod_random_mod' passed {pass_cnt} / {num_test}")
    #     timer.display_summary()

    def test_keyinvmod_non_prime_cpp(self):
        timer = st.SingletonTimer()

        num_test = 100
        pass_cnt = 0

        mod = 2**32

        factors = primefactors(mod)
        for _ in range(num_test):
            key, _ = ntl.GenerateRandomCoprimeLessthanN(mod)
            t = timer.start(tag="KeyInvMod Non Prime cpp latency",
                            category="KeyInvMod Non Prime cpp latency")
            key_inv = ntl_cpp.FindKeyInvModNonPrime(key, mod, factors)
            timer.end(t)
            self.assertEqual((key * key_inv) % mod, 1)
            pass_cnt += 1
        print(f"'test_keyinvmod_non_prime_cpp' passed {pass_cnt} / {num_test}")
        timer.display_summary()

    def test_keyinvmod_prime_cpp(self):
        timer = st.SingletonTimer()

        num_test = 100
        pass_cnt = 0
        mod = 4294967291

        for _ in range(num_test):
            self.assertTrue(ntl_cpp.IsPrime_uint64(mod))
            key = random.randint(1, mod - 1)
            t = timer.start(tag="KeyInvMod Prime cpp latency",
                            category="KeyInvMod Prime cpp latency")
            factors = primefactors(mod)
            key_inv = ntl_cpp.FindKeyInvModPrime(key, mod)
            timer.end(t)
            self.assertEqual((key * key_inv) % mod, 1)
            pass_cnt += 1
        print(f"'test_keyinvmod_non_prime_cpp' passed {pass_cnt} / {num_test}")
        timer.display_summary()


if __name__ == '__main__':
    unittest.main()
