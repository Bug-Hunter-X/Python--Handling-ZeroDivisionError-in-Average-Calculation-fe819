# Python: Handling ZeroDivisionError in Average Calculation
This code demonstrates a common error in Python: the ZeroDivisionError that occurs when dividing by zero.  The `calculate_average` function is designed to handle this situation gracefully by returning 0 when the input list is empty.  The included tests showcase the function's behavior with both non-empty and empty input lists.

The solution is simple: explicitly check for an empty list before performing the division operation.  This robust handling of edge cases improves code reliability and prevents unexpected program crashes.