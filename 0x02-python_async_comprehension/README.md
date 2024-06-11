# 0x02. Python - Async Comprehension

This project is about understanding and implementing asynchronous programming in Python.

## Tasks

### 0. Async Generator

Write a coroutine called `async_generator` that takes no arguments.

The coroutine will loop 10 times, each time asynchronously wait 1 second, then yield a random number between 0 and 10. Use the random module.

### 1. Async Comprehensions

Import `async_generator` from the previous task and then write a coroutine called `async_comprehension` that takes no arguments.

The coroutine will collect 10 random numbers using an async comprehending over `async_generator`, then return the 10 random numbers.

### 2. Run time for four parallel comprehensions

Import `async_comprehension` from the previous file and write a `measure_runtime` coroutine that will execute `async_comprehension` four times in parallel using `asyncio.gather`.

`measure_runtime` should measure the total runtime and return it. Notice that the total runtime is roughly 10 seconds, this is because even though we are running four `async_comprehension` coroutines in parallel, each coroutine waits for 1 second ten times. Since all coroutines run in parallel, the total time should be roughly equal to the time taken by one coroutine, which is 10 seconds.

## How to Run

This project requires Python 3.7+ and uses the `asyncio` and `random` modules from the Python Standard Library.
