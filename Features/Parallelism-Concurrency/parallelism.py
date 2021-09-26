import time
from multiprocessing import Pool


def increment(input):
    for i in range(10000000):
        input = input + 1


if __name__ == "__main__":
    inputs = [1] * 100
    pool = Pool(6)
    started = time.time()
    # sends the following inputs, to the function (increment)
    pool.map(increment, inputs)

    elapsed = time.time()
    print('Time taken MultiProcess :', elapsed - started)

    pool.close()

# Will use 100% of CPU for 14.7s [12 processes]
# When creating 4 processes utilization is about 75%, time taken 16.8s
# uses 100% cpu at 6 processes only giving 14.7s , it can be less depending upon thermal throttling and capacity.
