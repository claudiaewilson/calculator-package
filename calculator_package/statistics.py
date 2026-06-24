from collections import Counter

class StatisticsCalculator:
    """
    A class to calculate various statistics for a list of numbers.
    """

    def mean(self, numbers: list) -> float:
        """
        Calculate the mean of a list of numbers.

        Args:
            numbers (list): List of numbers.

        Returns:
            float: Mean value.

        Raises:
            ValueError: If list is empty.
        """
        if not numbers:
            raise ValueError("List cannot be empty.")
        return sum(numbers) / len(numbers)

    def median(self, numbers: list) -> float:
        """
        Calculate the median of a list of numbers.

        Args:
            numbers (list): List of numbers.

        Returns:
            float: Median value.

        Raises:
            ValueError: If list is empty.
        """
        if not numbers:
            raise ValueError("List cannot be empty.")

        sorted_numbers = sorted(numbers)
        length = len(sorted_numbers)
        middle = length // 2

        if length % 2 == 0:
            return (sorted_numbers[middle - 1] + sorted_numbers[middle]) / 2

        return float(sorted_numbers[middle])

    def mode(self, numbers: list):
        """
        Calculate the mode of a list of numbers.

        Args:
            numbers (list): List of numbers.

        Returns:
            int or float: Most common number.

        Raises:
            ValueError: If list is empty.
        """
        if not numbers:
            raise ValueError("List cannot be empty.")

        counter = Counter(numbers)
        most_common = counter.most_common(1)

        return most_common[0][0]

    def minimum(self, numbers: list):
        """
        Return the smallest number in a list.

        Args:
            numbers (list): List of numbers.

        Returns:
            int or float: Smallest number.

        Raises:
            ValueError: If list is empty.
        """
        if not numbers:
            raise ValueError("List cannot be empty.")
        return min(numbers)

    def maximum(self, numbers: list):
        """
        Return the largest number in a list.

        Args:
            numbers (list): List of numbers.

        Returns:
            int or float: Largest number.

        Raises:
            ValueError: If list is empty.
        """
        if not numbers:
            raise ValueError("List cannot be empty.")
        return max(numbers)

    def data_range(self, numbers: list):
        """
        Calculate the range of a list of numbers.

        Args:
            numbers (list): List of numbers.

        Returns:
            int or float: Difference between maximum and minimum values.

        Raises:
            ValueError: If list is empty.
        """
        if not numbers:
            raise ValueError("List cannot be empty.")
        return max(numbers) - min(numbers)