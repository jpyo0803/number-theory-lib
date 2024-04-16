import build.ntl as ntl
import unittest
import random
import math
import singleton_timer as st


def IsPrimePy(x):
    if x <= 1:
        return False

    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


class NtlTest(unittest.TestCase):
    def test_uint32(self):
        num_test = 10
        pass_cnt = 0
        for _ in range(num_test):
            x = random.randint(0, 2**32 - 1)
            res = ntl.IsPrime_uint32(x)
            res_py = IsPrimePy(x)
            self.assertTrue(res == res_py)
            pass_cnt += 1
        print(f"'test_uint32' passed {pass_cnt} / {num_test}")

    def test_uint64(self):
        num_test = 3
        pass_cnt = 0
        for _ in range(num_test):
            x = random.randint(0, 2**48)
            res = ntl.IsPrime_uint64(x)
            res_py = IsPrimePy(x)
            self.assertTrue(res == res_py)
            pass_cnt += 1
        print(f"'test_uint64' passed {pass_cnt} / {num_test}")

    def test_latencies(self):
        timer = st.SingletonTimer()

        for _ in range(10):
            x = random.randint(0, 2**32 - 1)

            t = timer.start(tag="uint32", category="uint32")
            res32 = ntl.IsPrime_uint32(x)
            timer.end(t)

            t = timer.start(tag="uint64", category="uint64")
            res64 = ntl.IsPrime_uint64(x)
            timer.end(t)

            t = timer.start(tag="python version", category="python version")
            res_py = IsPrimePy(x)
            timer.end(t)
            self.assertTrue(res32 == res64 and res64 == res_py)

        timer.display_summary()


if __name__ == '__main__':
    unittest.main()
