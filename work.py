# Реализуйте класс-итератор Primes, который принимает максимальное число N и выдаёт все простые числа
# от 1 до N.
#
# Основной код:

class Primes:

    def __init__(self, N):
        self.N = N
        self.num = 1
        self.prime_number = []

    def __iter__(self):
        return self

    def __next__(self):
        while self.num <= self.N:
            self.num += 1
            for prime in self.prime_number:
                if self.num % prime == 0:
                    break
            else:
                self.prime_number.append(self.num)
                return self.num
        raise StopIteration


prime_nums = Primes(50)

for i_elem in prime_nums:
    print(i_elem, end=' ')

#
# Ожидаемый результат кода:
#
# 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47