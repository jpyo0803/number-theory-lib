import ntl
import build.ntl as ntl_cpp
import unittest
import random
import singleton_timer as st
from sympy import primefactors


class NtlTest(unittest.TestCase):
    def test_key_inv_arr(self):
        timer = st.SingletonTimer()

        num_test = 5
        pass_cnt = 0
        mod = 2**32
        M = 2**5
        N = 2**5
        for _ in range(num_test):
            t = timer.start(tag='Generate Key', category='Generate Key')
            key_set_a1 = ntl_cpp.GenerateKeySetA(mod, M)
            key_set_a2 = ntl_cpp.GenerateKeySetA(mod, N)
            timer.end(t)

            t = timer.start(tag='Generate Key Inv',
                            category='Generate Key Inv')
            for i in range(M):
                for j in range(N):
                    key_inv = ntl.FindKeyInvModNonPrime(
                        key_set_a1[i] * key_set_a2[j], mod)
                    self.assertEqual(
                        (key_set_a1[i] * key_set_a2[j] * key_inv) % mod, 1)
            timer.end(t)
            pass_cnt += 1
        print(f"'test_key_inv_arr' passed {pass_cnt} / {num_test}")
        timer.display_summary()


if __name__ == '__main__':
    unittest.main()
