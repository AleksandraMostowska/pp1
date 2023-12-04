from dataclasses import dataclass, field

@dataclass
class Statistics:
    numbers: int = field(default_factory=list)

    def __str__(self) -> str:
        return f"Numbers: {' '.join([str(n) for n in self.numbers])}"

    def add(self) -> None:
        try:
            self.numbers.append(int(input('Enter number to be added: ')))
        except ValueError:
            print('Wrong input type.')

    def get_greatest(self) -> int:
        return max(self.numbers)
    
    def get_smallest(self) -> int:
        return min(self.numbers)
    
    def get_mean(self) -> float:
        return sum(self.numbers) / len(self.numbers)
    
    def get_median(self) -> int:
        sorted_nums = sorted(self.numbers)
        n = len(sorted_nums)
        return sorted_nums[n // 2] if n % 2 != 0 else (sorted_nums[n // n - 1] + sorted_nums[n // 2]) / 2
    
    def display_stats(self) -> None:
        print(f'Maximum: {self.get_greatest()}')
        print(f'Minimum: {self.get_smallest()}')
        print(f'Mean: {self.get_mean()}')
        print(f'Median: {self.get_median()}')