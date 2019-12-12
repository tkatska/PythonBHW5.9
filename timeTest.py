from benchmark import benchmark

with benchmark(1000):
    def f():
        for j in range(1000000):
            pass
