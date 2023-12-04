from dataclasses import dataclass
import random

@dataclass
class Thermometer:
    is_on: bool = False
    temperature: float = 0.0

    rangeMin = 34.0
    rangeMax = 42.0

    def turn_on(self) -> None:
        if not self.is_on:
            self.is_on = True
    
    def turn_off(self) -> None:
        if self.is_on:
            self.is_on = False

    def measure_temperature(self) -> None:
        self.temperature = Thermometer.draw_temperature(self.rangeMin, self.rangeMax)
    
    def check_if_fever(self) -> str:
        if self.temperature >= 41.0:
            return f'Temperature: {self.temperature} CRITICAL TEMPERATURE'
        if self.temperature >= 37.0:
            return f'Temperature: {self.temperature} (fever)'
        return f'Temperature: {self.temperature}'
    
    def display_temperature(self) -> None:
        print(self.check_if_fever()) if self.is_on else print('Thermometer is off.')

    @staticmethod
    def draw_temperature(rangeMin: int, rangeMax: int) -> float:
        if rangeMin >= rangeMax:
            raise ValueError('Range is not correct!')
        return round(random.uniform(rangeMin, rangeMax), 1)

def main():
    thermometer = Thermometer()
    thermometer.turn_on()
    temperature = thermometer.measure_temperature()
    thermometer.display_temperature()
    thermometer.turn_off()
    thermometer.display_temperature()

if __name__ == '__main__':
    main()
    