import time


def increment(input):
    for i in range(10000000):
        input = input + 1


if __name__ == "__main__":
    inputs = [1] * 100

    started = time.time()
    for i in inputs:
        increment(i)

    elapsed = time.time()

    print('Time taken Sequential:', elapsed - started)

# Uses about 25% processor thus proving 4 coures in cpu. Takes 38.8s, around thrice as much time
