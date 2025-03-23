"""
This program implements a caching Fibonacci function using recursion, calculates 
Fibonacci numbers by storing previously computed values in a cache.
"""

def caching_fibonacci():                        # Функція побудована на основі псевдокоду, що був заданий в умові задачі
    cache={}                                    # Задано кешування для оптимізації обчислень
    def fibonacci(n):
        if n <= 0: return 0
        if n == 1: return 1
        if n in cache: return cache[n]
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]
    return fibonacci


if __name__=="__main__":                        # Перевіряємо лише всередині цього файлу
    fib = caching_fibonacci()
    print(fib(10))
    print(fib(15))