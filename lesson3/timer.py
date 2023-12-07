"""
Напишите класс Timer, который будет вычислять время выполнения блока кода. Класс должен иметь следующие методы:

- __enter__(self): магический метод, который запускает таймер;
- __exit__(self, exc_type, exc_val, exc_tb): магический метод, который останавливает таймер
и выводит время выполнения блока кода.
"""
import time
from time import perf_counter


class Timer:

    def __enter__(self):
        self.start = perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = perf_counter()
        return self.end

    @property
    def elapsed_time(self):
        return self.end - self.start


with Timer() as timer:
    time.sleep(1)
    x = 2 + 2

# код для проверки
print("Execution time:", timer.elapsed_time)
