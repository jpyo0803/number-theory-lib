import build.ntl as ntl
import numpy as np
import unittest
import random


# This is for verification, written by chatgpt
def RepeatedSqrModPy(base, exp, mod):
    if mod == 1:  # As any number mod 1 is 0
        return 0
    if exp == 0:  # The base case: any number to the power of 0 is 1
        return 1
    if exp == 1:  # The base case: any number to the power of 1 is the number itself
        return base % mod

    # Recursive step: Reduce the problem size
    result = RepeatedSqrModPy(base, exp // 2, mod)
    result = (result * result) % mod  # Square the result of the smaller problem

    # If the exponent is odd, multiply one more time by the base
    if exp % 2 == 1:
        result = (result * base) % mod

    return result

class NtlTest(unittest.TestCase):
  def test_int32(self):
    num_test = 100
    pass_cnt = 0
    for _ in range(num_test):
      base = random.randint(-10, 10)
      exp = random.randint(0, 9)
      res = ntl.RepeatedSqr_int32(base, exp)
      self.assertTrue(res == (base ** exp))
      # print(f"'test_int32' pass, base = {base}, exp = {exp}")
      pass_cnt += 1
    print(f"'test_int32' passed {pass_cnt} / {num_test}")

  def test_int64(self):
    num_test = 100
    pass_cnt = 0
    for _ in range(num_test):
      base = random.randint(-10, 10)
      exp = random.randint(0, 18)
      res = ntl.RepeatedSqr_int64(base, exp)
      self.assertTrue(res == (base ** exp))
      # print(f"'test_int64' pass, base = {base}, exp = {exp}")
      pass_cnt += 1
    print(f"'test_int64' passed {pass_cnt} / {num_test}")
 
  def test_uint32(self):
    num_test = 100
    pass_cnt = 0
    for _ in range(num_test):
      base = random.randint(0, 10)
      exp = random.randint(0, 9)
      res = ntl.RepeatedSqr_uint32(base, exp)
      self.assertTrue(res == (base ** exp))
      # print(f"'test_int32' pass, base = {base}, exp = {exp}")
      pass_cnt += 1
    print(f"'test_uint32' passed {pass_cnt} / {num_test}")

  def test_uint64(self):
    num_test = 100
    pass_cnt = 0
    for _ in range(num_test):
      base = random.randint(0, 10)
      exp = random.randint(0, 18)
      res = ntl.RepeatedSqr_uint64(base, exp)
      self.assertTrue(res == (base ** exp))
      # print(f"'test_int64' pass, base = {base}, exp = {exp}")
      pass_cnt += 1
    print(f"'test_uint64' passed {pass_cnt} / {num_test}")

  def test_uint32_mod(self):
    num_test = 100
    pass_cnt = 0
    for _ in range(num_test):
      base = random.randint(0, 2**15)
      exp = random.randint(0, 2**15)
      mod = random.randint(1, 2**15)
      res = ntl.RepeatedSqr_uint32(base, exp, mod)
      self.assertTrue(res == ((base ** exp) % mod))
      pass_cnt += 1
    print(f"'test_uint32_mod' passed {pass_cnt} / {num_test}")

  def test_uint64_mod(self):
    num_test = 100
    pass_cnt = 0
    for _ in range(num_test):
      base = random.randint(0, 2**31)
      exp = random.randint(0, 2**63)
      mod = random.randint(1, 2**31)
      res = ntl.RepeatedSqrTest(base, exp, mod)
      res_py = RepeatedSqrModPy(base, exp, mod)
      self.assertTrue(res == res_py)
      pass_cnt += 1
    print(f"'test_uint64_mod' passed {pass_cnt} / {num_test}")

if __name__ == '__main__':
  unittest.main()