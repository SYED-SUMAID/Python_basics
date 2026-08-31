# Python Dictionaries

## Practical: Dictionaries and Dictionary Functions in Python

---

## Objective

To understand Python Dictionaries and perform essential operations using dictionary functions, methods, and operators.

---

## 1. Creating a Dictionary

### Description

A dictionary is an ordered and mutable collection of data stored in `key-value` pairs. Each key is used to access its corresponding value.

### Code

```python
student = {
    "name": "Sumaid",
    "age": 21,
    "course": "Python",
    "city": "Srinagar"
}

print(student)
```

### Output

```text
{'name': 'Sumaid', 'age': 21, 'course': 'Python', 'city': 'Srinagar'}
```

### Syntax

```python
dictionary_name = {
    "key": "value"
}
```

![alt text](<Screenshot (563).png>)


---

## 2. Accessing Dictionary Values

### Description

Dictionary values can be accessed using their corresponding keys.

### Code

```python
student = {
    "name": "Sumaid",
    "age": 21,
    "course": "Python",
    "city": "Srinagar"
}

print(student["name"])
print(student["course"])
```

### Output

```text
Sumaid
Python
```

### Syntax

```python
dictionary_name["key"]
```

`student["name"]` accesses the value associated with the `"name"` key.

![alt text](<Screenshot (565).png>)



---

## 3. Adding a Key-Value Pair

### Description

A new key-value pair can be added to a dictionary by assigning a value to a new key.

### Code

```python
student = {
    "name": "Sumaid",
    "age": 21,
    "course": "Python"
}

student["city"] = "Srinagar"

print(student)
```

### Output

```text
{'name': 'Sumaid', 'age': 21, 'course': 'Python', 'city': 'Srinagar'}
```

### Syntax

```python
dictionary_name["new_key"] = value
```

![alt text](<Screenshot (566).png>)

---

## 4. Modifying Dictionary Values

### Description

An existing dictionary value can be modified by assigning a new value to its key.

### Code

```python
student = {
    "name": "Sumaid",
    "age": 21,
    "course": "Python"
}

student["age"] = 22

print(student)
```

### Output

```text
{'name': 'Sumaid', 'age': 22, 'course': 'Python'}
```

### Syntax

```python
dictionary_name["key"] = new_value
```

![alt text](<Screenshot (567).png>)


---

## 5. get() Method

### Description

The `get()` method is used to access the value of a specified key.

### Code

```python
student = {
    "name": "Sumaid",
    "age": 21,
    "course": "Python"
}

print(student.get("name"))
```

### Output

```text
Sumaid
```

### Syntax

```python
dictionary_name.get("key")
```

The `get()` method returns the value associated with the specified key.


![alt text](<Screenshot (568).png>)


---

## 6. keys() Method

### Description

The `keys()` method is used to retrieve all the keys present in a dictionary.

### Code

```python
student = {
    "name": "Sumaid",
    "age": 21,
    "course": "Python"
}

print(student.keys())
```

### Output

```text
dict_keys(['name', 'age', 'course'])
```

### Syntax

```python
dictionary_name.keys()
```

![alt text](<Screenshot (569).png>)


---

## 7. values() Method

### Description

The `values()` method is used to retrieve all the values present in a dictionary.

### Code

```python
student = {
    "name": "Sumaid",
    "age": 21,
    "course": "Python"
}

print(student.values())
```

### Output

```text
dict_values(['Sumaid', 21, 'Python'])
```

### Syntax

```python
dictionary_name.values()
```

![alt text](<Screenshot (570).png>)


---

## 8. update() Method

### Description

The `update()` method is used to add new key-value pairs or modify existing values in a dictionary.

### Code

```python
student = {
    "name": "Sumaid",
    "age": 21,
    "course": "Python"
}

student.update({"age": 22, "city": "Srinagar"})

print(student)
```

### Output

```text
{'name': 'Sumaid', 'age': 22, 'course': 'Python', 'city': 'Srinagar'}
```

### Syntax

```python
dictionary_name.update({"key": value})
```

![alt text](<Screenshot (571).png>)

---

## 9. pop() Method

### Description

The `pop()` method is used to remove a specific key-value pair from a dictionary using its key.

### Code

```python
student = {
    "name": "Sumaid",
    "age": 21,
    "course": "Python",
    "city": "Srinagar"
}

student.pop("city")

print(student)
```

### Output

```text
{'name': 'Sumaid', 'age': 21, 'course': 'Python'}
```

### Syntax

```python
dictionary_name.pop("key")
```

![alt text](<Screenshot (572).png>)


---

## 10. del Keyword

### Description

The `del` keyword is used to delete a specific key-value pair from a dictionary.

### Code

```python
student = {
    "name": "Sumaid",
    "age": 21,
    "course": "Python"
}

del student["age"]

print(student)
```

### Output

```text
{'name': 'Sumaid', 'course': 'Python'}
```

### Syntax

```python
del dictionary_name["key"]
```

![alt text](<Screenshot (573).png>)


---

## 11. clear() Method

### Description

The `clear()` method is used to remove all key-value pairs from a dictionary.

### Code

```python
student = {
    "name": "Sumaid",
    "age": 21,
    "course": "Python"
}

student.clear()

print(student)
```

### Output

```text
{}
```

### Syntax

```python
dictionary_name.clear()
```

![alt text](<Screenshot (574).png>)


---

## 12. Checking if a Key Exists

### Description

The `in` operator is used to check whether a specific key exists in a dictionary.

### Code

```python
student = {
    "name": "Sumaid",
    "age": 21,
    "course": "Python"
}

print("name" in student)
print("city" in student)
```

### Output

```text
True
False
```

### Syntax

```python
"key" in dictionary_name
```

The expression returns `True` if the key exists and `False` if it does not.

![alt text](<Screenshot (575).png>)

---

## Conclusion

In this practical, we studied Python Dictionaries and performed essential operations such as creating dictionaries, accessing and modifying values, adding key-value pairs, retrieving keys and values, updating data, removing elements, clearing dictionaries, and checking for existing keys.

These operations provide the basic foundation for working with key-value data in Python.