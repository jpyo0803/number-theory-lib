import ntl
import unittest
import singleton_timer as st
import random


class NtlTest(unittest.TestCase):
    def test_uint64(self):
        timer = st.SingletonTimer()

        num_test = 10000
        for i in range(num_test):
            if i == 0:
              n = 4294967291
            else:
              n = random.randint(2, 2**32 - 1)
            t = timer.start(tag='factorize latency',
                            category='factorize latency')
            factors = ntl.Factorize(n)
            timer.end(t)

        timer.display_summary()


if __name__ == '__main__':
    unittest.main()
