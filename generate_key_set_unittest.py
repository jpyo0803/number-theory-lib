

import ntl
import build.ntl as ntl_cpp
import unittest
import random
import singleton_timer as st


class NtlTest(unittest.TestCase):
    def test_generate_key_set_a(self):
        timer = st.SingletonTimer()

        num_test = 1000
        pass_cnt = 0
        mod = 2**32
        N = 2*14
        for _ in range(num_test):
            t = timer.start(tag="Generate key set a latency",
                            category="Generate key set a latency")
            key_set = ntl_cpp.GenerateKeySetA(mod, N)
            timer.end(t)
            for key in key_set:
                self.assertTrue(key < mod and ntl_cpp.Gcd_uint64(key, mod))
            pass_cnt += 1

        print(f"'test_generate_key_set_a' passed {pass_cnt} / {num_test}")
        timer.display_summary()

    def test_generate_key_set_b(self):
        timer = st.SingletonTimer()

        num_test = 1000
        pass_cnt = 0
        mod = 2**32
        N = 2*14
        for _ in range(num_test):
            t = timer.start(tag="Generate key set b latency",
                            category="Generate key set b latency")
            key_set = ntl_cpp.GenerateKeySetA(mod, N)
            timer.end(t)
            for key in key_set:
                self.assertTrue(key >= 0 and key < mod)
            pass_cnt += 1

        print(f"'test_generate_key_set_b' passed {pass_cnt} / {num_test}")
        timer.display_summary()



if __name__ == '__main__':
    unittest.main()
