import build.ntl as ntl
import sys
import singleton_timer as st


def main(n: int):
    timer = st.SingletonTimer()
    t = timer.start(tag="eratosthenes sieve latency",
                    category="eratosthenes sieve latency")
    primes = ntl.eratosthenes_sieve(2 ** n)
    timer.end(t)

    for prime in primes:
        assert ntl.IsPrime_uint64(prime)

    filename = f'primes_upto_2^{n}.txt'
    with open(filename, 'w') as fout:
        for prime in primes:
            fout.write(f'{prime} ')

    timer.display_summary()


if __name__ == '__main__':
    main(int(sys.argv[1]))
