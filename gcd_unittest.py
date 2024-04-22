import build.ntl as ntl
import unittest
import random
import math

import singleton_timer as st


class GcdTest(unittest.TestCase):
    def test_gcd_uint32(self):
        timer = st.SingletonTimer()
        num_test = 10000
        pass_cnt = 0
        for _ in range(num_test):
            x = random.randint(0, 2**32 - 1)
            y = random.randint(0, 2**32 - 1)
            t = timer.start(tag='test_gcd_uint32', category='test_gcd_uint32')
            res = ntl.Gcd_uint32(x, y)
            timer.end(t)
            res_py = math.gcd(x, y)
            self.assertTrue(res == res_py)
            pass_cnt += 1
        print(f"'test_gcd_uint32' passed {pass_cnt} / {num_test}")
        timer.display_summary()

    def test_gcd_uint64(self):
        timer = st.SingletonTimer()
        num_test = 10000
        pass_cnt = 0
        for _ in range(num_test):
            x = random.randint(0, 2**64 - 1)
            y = random.randint(0, 2**64 - 1)
            t = timer.start(tag='test_gcd_uint64', category='test_gcd_uint64')
            res = ntl.Gcd_uint64(x, y)
            timer.end(t)
            res_py = math.gcd(x, y)
            self.assertTrue(res == res_py)
            pass_cnt += 1
        print(f"'test_gcd_uint64' passed {pass_cnt} / {num_test}")
        timer.display_summary()

    def test_std_gcd_uint32(self):
        timer = st.SingletonTimer()
        num_test = 10000
        pass_cnt = 0
        for _ in range(num_test):
            x = random.randint(0, 2**32 - 1)
            y = random.randint(0, 2**32 - 1)
            t = timer.start(tag='test_std_gcd_uint32', category='test_std_gcd_uint32')
            res = ntl.StdGcd_uint32(x, y)
            timer.end(t)
            res_py = math.gcd(x, y)
            self.assertTrue(res == res_py)
            pass_cnt += 1
        print(f"'test_std_gcd_uint32' passed {pass_cnt} / {num_test}")
        timer.display_summary()

    def test_std_gcd_uint64(self):
        timer = st.SingletonTimer()
        num_test = 10000
        pass_cnt = 0
        for _ in range(num_test):
            x = random.randint(0, 2**64 - 1)
            y = random.randint(0, 2**64 - 1)
            t = timer.start(tag='test_std_gcd_uint64', category='test_std_gcd_uint64')
            res = ntl.StdGcd_uint64(x, y)
            timer.end(t)
            res_py = math.gcd(x, y)
            self.assertTrue(res == res_py)
            pass_cnt += 1
        print(f"'test_std_gcd_uint64' passed {pass_cnt} / {num_test}")
        timer.display_summary()



if __name__ == '__main__':
    unittest.main()
