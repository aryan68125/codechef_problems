# codechef_problems
This is a repository that holds all the solutions to the codechef coding problems.

## Identify the errors
Identify and rectify the errors in the code provided to get the desired output.
```
one = "Coding"
two = "Chaf"
two = two[:2] + 'e' + two[3:]
print(one + " " + two)
```

Let's go through both versions of the code in great detail and explain the differences, why one works and the other doesn't, and why the modified code is valid.

### Code 1 (Problematic Version):
```python
one = "Coding"
two = "Chaf"
two[3] = 'e'  # This line causes an error
print(one + " " + two)
```

#### Key Concepts:

- **Strings are Immutable in Python**: In Python, strings are immutable, which means that once a string is created, you cannot change any of its individual characters directly.
  
  In this line of code:
  ```python
  two[3] = 'e'
  ```
  You are attempting to modify the character at index `3` of the string `two`. The string `two = "Chaf"` has the character `'f'` at index `3`. However, Python does not allow this kind of operation because strings cannot be modified in place. **This will raise a `TypeError`**:
  ```
  TypeError: 'str' object does not support item assignment
  ```

This error occurs because strings are immutable, and attempting to modify an element by its index (like `two[3] = 'e'`) is not allowed.

---

### Code 2 (Corrected Version):
```python
one = "Coding"
two = "Chaf"
two = two[:2] + 'e' + two[3:]  # This is valid
print(one + " " + two)
```

#### Key Concepts:

- **Slicing Strings**: In Python, you can use **string slicing** to create new strings from parts of an existing string. The syntax is:
  ```python
  string[start:end]  # Creates a new string from index 'start' to 'end-1'
  ```
  Slicing does not modify the original string but creates a new one.

#### Explanation of the Corrected Code:

1. `one = "Coding"`: This simply creates the string `one` with the value `"Coding"`.

2. `two = "Chaf"`: This creates the string `two` with the value `"Chaf"`.

3. `two = two[:2] + 'e' + two[3:]`:
   - `two[:2]`: This is slicing the string `two` from the beginning up to index `2` (not including index `2`), so it gives the substring `"Ch"`.
   - `'e'`: The character `'e'` is added between the slices. This is the character that will replace the `'a'` in the original string.
   - `two[3:]`: This slices the string `two` from index `3` to the end, giving `"f"`.
   
   So, the expression `two[:2] + 'e' + two[3:]` results in the string `"Chae"`, effectively replacing the `'a'` in `"Chaf"` with `'e'`.

4. `print(one + " " + two)`:
   - This combines the strings `one` and `two` (which is now `"Chae"`) with a space between them, and prints `"Coding Chae"`.

#### Why This Works:
- Instead of modifying the string directly (which is not allowed), we **create a new string** by combining slices of the original string and the new character `'e'`. This is a perfectly valid operation because strings are immutable, and slicing combined with concatenation produces a new string rather than altering the original string.

#### Final Output:
```
Coding Chae
```

---

### Summary of Differences Between the Two Codes:

- **Original Code (Error)**:
  ```python
  two[3] = 'e'
  ```
  This line tries to modify the character at index `3` of the string `two`. Since strings are immutable in Python, this raises a `TypeError`.

- **Corrected Code (Valid)**:
  ```python
  two = two[:2] + 'e' + two[3:]
  ```
  This line **creates a new string** by concatenating parts of the original string (`two`) and the character `'e'`. String slicing allows us to "extract" portions of the string, and since strings are immutable, this results in a new string without modifying the original.

In the corrected version, you are not modifying the original string directly. Instead, you create a new string using slices of the original string, which is allowed in Python. This is why the corrected code works, while the original code causes an error.

## ASCII sumission of characters
What is the output of the following code?

```
first, second = input().split()
print((ord(first) + ord(second)))
```

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