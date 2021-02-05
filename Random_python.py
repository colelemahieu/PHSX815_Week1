#! /usr/bin/env python

import sys
import numpy as np
import matplotlib.pyplot as plt

class Random:
    """A random number generator class"""
    m_v = 4101842887655102017
    m_w = 1
    m_u = 1

    def __init__(self, seed = 5555):
        self.seed = seed
        self.m_v = np.uint64(4101842887655102017)
        self.m_w = np.uint64(1)
        self.m_u = np.uint64(1)

        self.m_u = np.uint64(self.seed) ^ self.m_v
        self.int64()
        self.m_v = self.m_u
        self.int64()
        self.m_w = self.m_v
        self.int64()

    def int64(self):
        self.m_u = np.uint64(self.m_u * 2862933555777941757) + np.uint64(7046029254386353087)
        self.m_v ^= self.m_v >> np.uint64(17)
        self.m_v ^= self.m_v << np.uint64(31)
        self.m_v ^= self.m_v >> np.uint64(8)
        self.m_w = np.uint64(np.uint64(4294957665)*(self.m_w & np.uint64(0xffffffff))) + np.uint64((self.m_w >> np.uint64(32)))
        x = np.uint64(self.m_u ^ (self.m_u << np.uint64(21)))
        x ^= x >> np.uint64(35)
        x ^= x << np.uint64(4)
        with np.errstate(over='ignore'):
            return (x + self.m_v)^self.m_w

    def rand(self):
        return 5.42101086242752217E-20 * self.int64()

if __name__ == "__main__":
    if '-h' in sys.argv or '--help' in sys.argv:
        print ("Usage: %s [-seed number]" % sys.argv[0])
        print
        sys.exit(1)

    # Fixing random state for reproducibility
    np.random.seed(5555)

    seed = 5555

    if '-seed' in sys.argv:
        p = sys.argv.index('-seed')
        seed = sys.argv[p+1]
        np.random.seed(5555)

    np.random.seed(seed)
    random = Random(seed)

    # data
    x = np.random.rand(10000)
    N = 10000
    x = np.random.rand(N)
    myx = []
    for i in range(0,N):
        myx.append(random.rand())

    # the histogram of the data
    n, bins, patches = plt.hist(x, 50, density=True, facecolor='g', alpha=0.75)
    n, bins, patches = plt.hist(myx, 50, density=True, facecolor='g', alpha=0.75)

    plt.xlabel('x')
    plt.ylabel('Probability')
    plt.title('Uniform random number')
    plt.grid(True)
    plt.show()
