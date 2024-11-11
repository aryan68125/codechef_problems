'''
This code takes two single-character inputs, calculates the Unicode values (or ASCII values, for characters in the ASCII range) of those characters, adds them together, and prints the result.

Here's a step-by-step explanation:

1. **Input Split**:
   ```python
   first, second = input().split()
   ```
   - `input().split()` takes a single line of input and splits it into separate parts based on spaces.
   - The `split()` method returns a list of strings, and each element of this list is assigned to the variables `first` and `second`.
   - For example, if you input `"A B"`, `first` will be `"A"` and `second` will be `"B"`.

2. **Unicode (ASCII) Value Calculation**:
   ```python
   print((ord(first) + ord(second)))
   ```
   - `ord(character)` is a built-in function in Python that takes a single character (like `'A'` or `'B'`) and returns its Unicode code point as an integer.
   - In the ASCII range, the Unicode code points are the same as ASCII values. For instance:
     - `ord('A')` returns `65`
     - `ord('B')` returns `66`

3. **Sum and Output**:
   - The code adds the Unicode values of `first` and `second` and then prints the sum.
   - For example, if `first` is `'A'` (65) and `second` is `'B'` (66), the output would be:
     ```python
     131
     ```

### Example Input and Output
- **Input**:
  ```
  A B
  ```

- **Output**:
  ```
  131
  ```

### Explanation of `ord`
The `ord` function converts a character to its Unicode (or ASCII) code point, which allows you to get the numerical representation of the character. This is particularly useful for processing text or characters numerically.
'''
first, second = input().split()
print((ord(first) + ord(second)))