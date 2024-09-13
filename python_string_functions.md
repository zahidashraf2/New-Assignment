
# Python String Functions

Python provides a lot of built-in string functions, which allow us to manipulate and operate on strings.

## 1. `len()`
- **Usage:** `len(string)`
- **Description:** Returns the length of the string (i.e., number of characters).
```python
string = "Hello"
print(len(string))  # Output: 5
```

## 2. `lower()`
- **Usage:** `string.lower()`
- **Description:** Converts all characters of the string to lowercase.
```python
string = "Hello"
print(string.lower())  # Output: "hello"
```

## 3. `upper()`
- **Usage:** `string.upper()`
- **Description:** Converts all characters of the string to uppercase.
```python
string = "Hello"
print(string.upper())  # Output: "HELLO"
```

## 4. `capitalize()`
- **Usage:** `string.capitalize()`
- **Description:** Capitalizes the first character of the string and converts the rest to lowercase.
```python
string = "hello world"
print(string.capitalize())  # Output: "Hello world"
```

## 5. `title()`
- **Usage:** `string.title()`
- **Description:** Converts the first character of each word to uppercase.
```python
string = "hello world"
print(string.title())  # Output: "Hello World"
```

## 6. `strip()`
- **Usage:** `string.strip()`
- **Description:** Removes any leading (spaces at the beginning) and trailing (spaces at the end) characters (spaces are default).
```python
string = "  hello  "
print(string.strip())  # Output: "hello"
```

## 7. `replace()`
- **Usage:** `string.replace(old, new)`
- **Description:** Replaces all occurrences of a substring with another substring.
```python
string = "Hello world"
print(string.replace("world", "Python"))  # Output: "Hello Python"
```

## 8. `find()`
- **Usage:** `string.find(substring)`
- **Description:** Returns the index of the first occurrence of the substring. If not found, it returns -1.
```python
string = "Hello world"
print(string.find("world"))  # Output: 6
```

## 9. `split()`
- **Usage:** `string.split(delimiter)`
- **Description:** Splits the string into a list where each word is a list item. By default, it splits by spaces.
```python
string = "Hello world"
print(string.split())  # Output: ['Hello', 'world']
```

## 10. `join()`
- **Usage:** `delimiter.join(list)`
- **Description:** Joins the elements of a list into a single string, separated by the delimiter.
```python
words = ["Hello", "world"]
print(" ".join(words))  # Output: "Hello world"
```

## 11. `startswith()`
- **Usage:** `string.startswith(substring)`
- **Description:** Returns `True` if the string starts with the specified substring, otherwise `False`.
```python
string = "Hello world"
print(string.startswith("Hello"))  # Output: True
```

## 12. `endswith()`
- **Usage:** `string.endswith(substring)`
- **Description:** Returns `True` if the string ends with the specified substring, otherwise `False`.
```python
string = "Hello world"
print(string.endswith("world"))  # Output: True
```

## 13. `count()`
- **Usage:** `string.count(substring)`
- **Description:** Returns the number of occurrences of the substring in the string.
```python
string = "Hello world world"
print(string.count("world"))  # Output: 2
```

## 14. `isalpha()`
- **Usage:** `string.isalpha()`
- **Description:** Returns `True` if all characters in the string are alphabetic and there is at least one character, otherwise `False`.
```python
string = "Hello"
print(string.isalpha())  # Output: True
```

## 15. `isdigit()`
- **Usage:** `string.isdigit()`
- **Description:** Returns `True` if all characters in the string are digits and there is at least one character, otherwise `False`.
```python
string = "12345"
print(string.isdigit())  # Output: True
```

These are some of the most commonly used string functions in Python, each serving a specific purpose in string manipulation.
