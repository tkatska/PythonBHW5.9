import time
class benchmark(object):
    def __init__(self, name, num_runs=100):
        self.name = name
        self.num_runs = num_runs
    def __enter__(self):
        self.start = time.time()
        return self
    def __exit__ (self, *args, **kwargs):
        avg_time = (time.time() - self.start) / self.num_runs
        print("Среднее время выполнения, мкс = %.5f" % (avg_time * 1_000_000))


