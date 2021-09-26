# Parallelism & Concurrency

## Parallelism

Parallel processing involves running a process in each of the cores of a machine. No memory sharing.
(Map, reduce)
More Useful in case of CPU bound operations.
Each subprocess has its own private memory, Python interpreter, GIL and a single main thread.

## Concurrency

Concurrency uses multithreading, a part of input is computed seperately in a thread. More useful in case of IO bound operations. It prevents locks created due to waiting for input. Uses GIL (global interpreter lock) to make sure only 1 thread can run the interpreter at a given instance and hence access shared memory space. As each process has GIL to control the execution of thread we go for multi processes over multi thread to speed up CPU bound operations.

src : <https://medium.com/fintechexplained/advanced-python-concurrency-and-parallelism-82e378f26ced>(Link)
