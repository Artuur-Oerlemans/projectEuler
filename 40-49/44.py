import math


class Calculator:
    pentagonal_numbers = []
    pentagonal_numbers_set = set()
    step_size = 1
    d_found = False
    d = -1
    max_i_declared = False
    max_i = -1

    def find_smallest_d(self) -> int:
        self.increase_pent_numbers()
        self.increase_pent_numbers()
        i = 1
        while not self.max_i_declared or i <= self.max_i:
            if len(self.pentagonal_numbers) <= i:
                self.increase_pent_numbers()
            j = i - 1
            while j > 0:
                maybe_d = self.pentagonal_numbers[i] - self.pentagonal_numbers[j]
                if self.d_found and maybe_d > self.d:
                    j = 0
                elif maybe_d in self.pentagonal_numbers_set:
                    sum_pent = self.pentagonal_numbers[i] + self.pentagonal_numbers[j]
                    self.increase_pent_number_enough(sum_pent)
                    if sum_pent in self.pentagonal_numbers_set:
                        print("found something", maybe_d)
                        self.d = maybe_d
                        self.d_found = True
                j -= 1
            i += 1

        return self.d

    def increase_pent_numbers(self):
        n = len(self.pentagonal_numbers) + 1
        self.pentagonal_numbers.append(n * (3 * n - 1) // 2)
        self.pentagonal_numbers_set.add(self.pentagonal_numbers[-1])
        if n > 1:
            step_size = self.pentagonal_numbers[n - 1] - self.pentagonal_numbers[n - 2]
            if self.d_found and not self.max_i_declared and step_size > self.d:
                self.max_i = n - 1
                print("max_", self.max_i)
                self.max_i_declared = True

    def increase_pent_number_enough(self, goal: int):
        while self.pentagonal_numbers[-1] < goal:
            self.increase_pent_numbers()


calc = Calculator()

print("found", calc.find_smallest_d())
