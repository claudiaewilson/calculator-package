"""
history.py

This module stores calculator operation history.
"""


class CalculatorHistory:
    """
    A simple calculator history tracker.
    """

    def __init__(self):
        self.history = []

    def add_record(self, operation, result):
        """
        Add a calculation record.

        Args:
            operation (str): Description of operation.
            result: Calculation result.
        """
        record = {
            "operation": operation,
            "result": result
        }
        self.history.append(record)

    def get_history(self):
        """
        Return all calculation records.

        Returns:
            list: Calculation history.
        """
        return self.history

    def clear_history(self):
        """
        Clear all calculation records.
        """
        self.history.clear()