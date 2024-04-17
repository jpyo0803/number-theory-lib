import build.ntl as ntl
import unittest
import random
import math

import singleton_timer as st


class NtlTest(unittest.TestCase):
    def test_uint32(self):
        num_test = 10000
        pass_cnt = 0
        for _ in range(num_test):
            x = random.randint(0, 2**32 - 1)
            y = random.randint(0, 2**32 - 1)
            res = ntl.Gcd_uint32(x, y)
            res_py = math.gcd(x, y)
            self.assertTrue(res == res_py)
            pass_cnt += 1
        print(f"'test_uint32' passed {pass_cnt} / {num_test}")

    def test_uint64(self):
        num_test = 10000
        pass_cnt = 0
        for _ in range(num_test):
            x = random.randint(0, 2**64 - 1)
            y = random.randint(0, 2**64 - 1)
            res = ntl.Gcd_uint64(x, y)
            res_py = math.gcd(x, y)
            self.assertTrue(res == res_py)
            pass_cnt += 1
        print(f"'test_uint64' passed {pass_cnt} / {num_test}")

    def test_latencies(self):
        timer = st.SingletonTimer()

        for _ in range(1000):
            x = random.randint(0, 2**32 - 1)
            y = random.randint(0, 2**32 - 1)

            t = timer.start(tag="uint32", category="uint32")
            res = ntl.Gcd_uint32(x, y)
            timer.end(t)
            
            t = timer.start(tag="uint64", category="uint64")
            res = ntl.Gcd_uint64(x, y)
            timer.end(t)

            t = timer.start(tag="python version", category="python version")
            res_py = math.gcd(x, y)
            timer.end(t)

        timer.display_summary()


if __name__ == '__main__':
    unittest.main()
