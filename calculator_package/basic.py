class CalculatorInterface:
    def calculate(self, operation: str, a: float, b: float) -> float:
        """Abstract method that must be implemented by any child class."""
        pass


class BasicCalculator(CalculatorInterface):

    def __init__(self):
        self.__latest_result = 0.0

    # Getter method to safely access the private variable
    def get_latest_result(self):
        return self.__latest_result

    # Setter method to safely update the private variable internally
    def _update_result(self, value):
        self.__latest_result = value

    # Implementing the abstract method
    def calculate(self, operation: str, a: float, b: float):
        if operation == "add":
            self._update_result(a + b)
        elif operation == "subtract":
            self._update_result(a - b)
        elif operation == "multiply":
            self._update_result(a * b)
        elif operation == "Divide":
            self._update_result(a / b)
        elif operation == "modulus":
            self._update_result(a % b)
        elif operation == "floor_divide":
            self._update_result(a // b)
        else:
            raise ValueError(f"Operation '{operation}' not supported by BasicCalculator.")

        return self.get_latest_result()