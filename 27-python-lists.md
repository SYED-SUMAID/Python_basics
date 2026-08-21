# 27 - Python Lists

## Practical: Lists and List Functions in Python

---

## Objective

To understand Python Lists and perform different operations using list functions and methods.

---

## 1. Creating a List

### Description

A list is an ordered and mutable collection of elements in Python. Lists can contain multiple values of different data types.

### Code

```python
fruits = ["Apple", "Banana", "Mango", "Orange"]

print(fruits)
```

### Output

```text
['Apple', 'Banana', 'Mango', 'Orange']
```

### Syntax

```python
list_name = [element1, element2, element3]
```

### Screenshot
![alt text](<Screenshot (541)(1).png>)


---

## 2. Accessing List Elements

### Description

List elements can be accessed using their index number. Python uses zero-based indexing, where the first element has index `0`.

### Code

```python
fruits = ["Apple", "Banana", "Mango", "Orange"]

print(fruits[0])
print(fruits[2])
```

### Output

```text
Apple
Mango
```

### Syntax

```python
list_name[index]
```

`fruits[0]` accesses the first element, while `fruits[2]` accesses the third element.

### Screenshot
![alt text](<Screenshot (542)(1).png>)

---

## 3. Modifying List Elements

### Description

List elements can be modified by assigning a new value to an existing index.

### Code

```python
fruits = ["Apple", "Banana", "Mango", "Orange"]

fruits[1] = "Grapes"

print(fruits)
```

### Output

```text
['Apple', 'Grapes', 'Mango', 'Orange']
```

### Syntax

```python
list_name[index] = new_value
```

The element at index `1` is changed from `"Banana"` to `"Grapes"`.

![alt text](<Screenshot (543)(1).png>)



---

## 4. append() Method

### Description

The `append()` method is used to add a new element at the end of a list.

### Code

```python
fruits = ["Apple", "Banana", "Mango", "Orange"]

fruits.append("Pineapple")

print(fruits)
```

### Output

```text
['Apple', 'Banana', 'Mango', 'Orange', 'Pineapple']
```

### Syntax

```python
list_name.append(element)
```

`fruits.append("Pineapple")` adds `"Pineapple"` to the end of the list.

![alt text](<Screenshot (544)(1).png>)


---

## 5. insert() Method

### Description

The `insert()` method is used to add an element at a specific position in a list.

### Code

```python
fruits = ["Apple", "Banana", "Mango", "Orange"]

fruits.insert(1, "Watermelon")

print(fruits)
```

### Output

```text
['Apple', 'Watermelon', 'Banana', 'Mango', 'Orange']
```

### Syntax

```python
list_name.insert(index, element)
```

`fruits.insert(1, "Watermelon")` adds `"Watermelon"` at index `1`.

![alt text](<Screenshot (546)(1).png>)



---

## 6. extend() Method

### Description

The `extend()` method is used to add multiple elements from another list to the existing list.

### Code

```python
fruits = ["Apple", "Banana", "Mango", "Orange"]

more_fruits = ["Kiwi", "Papaya"]

fruits.extend(more_fruits)

print(fruits)
```

### Output

```text
['Apple', 'Banana', 'Mango', 'Orange', 'Kiwi', 'Papaya']
```

### Syntax

```python
list_name.extend(another_list)
```

`fruits.extend(more_fruits)` adds all elements of `more_fruits` to `fruits`.

![alt text](<Screenshot (547)(1).png>)


---

## 7. remove() Method

### Description

The `remove()` method is used to remove a specific element from a list.

### Code

```python
fruits = ["Apple", "Banana", "Mango", "Orange"]

fruits.remove("Banana")

print(fruits)
```

### Output

```text
['Apple', 'Mango', 'Orange']
```

### Syntax

```python
list_name.remove(element)
```

`fruits.remove("Banana")` removes the first occurrence of `"Banana"` from the list.

![alt text](<Screenshot (548)(1).png>)

---

## 8. pop() Method

### Description

The `pop()` method is used to remove an element from a list using its index.

### Code

```python
fruits = ["Apple", "Banana", "Mango", "Orange"]

removed_fruit = fruits.pop(2)

print("Removed Element:", removed_fruit)
print(fruits)
```

### Output

```text
Removed Element: Mango
['Apple', 'Banana', 'Orange']
```

### Syntax

```python
list_name.pop(index)
```

`fruits.pop(2)` removes and returns the element at index `2`.

Without an index, `pop()` removes the last element.

```python
fruits = ["Apple", "Banana", "Mango", "Orange"]

fruits.pop()

print(fruits)
```

### Output

```text
['Apple', 'Banana', 'Mango']
```

![alt text](<Screenshot (549)(1).png>)
![alt text](<Screenshot (550)(1).png>)


---

## 9. del Keyword

### Description

The `del` keyword is used to delete an element from a list using its index.

### Code

```python
fruits = ["Apple", "Banana", "Mango", "Orange"]

del fruits[1]

print(fruits)
```

### Output

```text
['Apple', 'Mango', 'Orange']
```

### Syntax

```python
del list_name[index]
```

`del fruits[1]` deletes the element at index `1`

![alt text](<Screenshot (551)(1).png>)

---

## 10. clear() Method

### Description

The `clear()` method is used to remove all elements from a list.

### Code

```python
fruits = ["Apple", "Banana", "Mango", "Orange"]

fruits.clear()

print(fruits)
```

### Output

```text
[]
```

### Syntax

```python
list_name.clear()
```

`fruits.clear()` removes all elements from the list.

![alt text](<Screenshot (552)(1)(1)-1.png>)


---

## 11. len() Function

### Description

The `len()` function is used to find the total number of elements present in a list.

### Code

```python
fruits = ["Apple", "Banana", "Mango", "Orange"]

print(len(fruits))
```

### Output

```text
4
```

### Syntax

```python
len(list_name)
```

`len(fruits)` returns the total number of elements in the list.

![alt text](<Screenshot (554)(1).png>)


---

## 12. sort() Method

### Description

The `sort()` method is used to arrange the elements of a list in ascending or descending order.

### Code

```python
fruits = ["Orange", "Apple", "Mango", "Banana"]

fruits.sort()

print(fruits)
```

### Output

```text
['Apple', 'Banana', 'Mango', 'Orange']
```

### Syntax

```python
list_name.sort()
```

`fruits.sort()` arranges the elements in ascending order by default.

For descending order:

```python
fruits.sort(reverse=True)

print(fruits)
```

### Output

```text
['Orange', 'Mango', 'Banana', 'Apple']
```

### Syntax for Descending Order

```python
list_name.sort(reverse=True)
```

![alt text](<Screenshot (556)(1).png>)


---

## 13. reverse() Method

### Description

The `reverse()` method is used to reverse the order of elements in a list.

### Code

```python
fruits = ["Apple", "Banana", "Mango", "Orange"]

fruits.reverse()

print(fruits)
```

### Output

```text
['Orange', 'Mango', 'Banana', 'Apple']
```

### Syntax

```python
list_name.reverse()
```

`fruits.reverse()` reverses the order of elements in the list.

![alt text](<Screenshot (557)(1).png>)


---

## 14. count() Method

### Description

The `count()` method is used to count how many times a specific element appears in a list.

### Code

```python
fruits = ["Apple", "Banana", "Apple", "Mango", "Apple"]

print(fruits.count("Apple"))
```

### Output

```text
3
```

### Syntax

```python
list_name.count(element)
```

`fruits.count("Apple")` returns the number of times `"Apple"` appears in the list.

![alt text](<Screenshot (560)(1).png>)

---

## 15. index() Method

### Description

The `index()` method is used to find the position of a specific element in a list.

### Code

```python
fruits = ["Apple", "Banana", "Mango", "Orange"]

print(fruits.index("Mango"))
```

### Output

```text
2
```

### Syntax

```python
list_name.index(element)
```

`fruits.index("Mango")` returns the index of `"Mango"`.

![alt text](<Screenshot (561)(1).png>)



---

## 16. copy() Method

### Description

The `copy()` method is used to create a copy of an existing list.

### Code

```python
fruits = ["Apple", "Banana", "Mango", "Orange"]

fruits_copy = fruits.copy()

print("Original List:", fruits)
print("Copied List:", fruits_copy)
```

### Output

```text
Original List: ['Apple', 'Banana', 'Mango', 'Orange']
Copied List: ['Apple', 'Banana', 'Mango', 'Orange']
```

### Syntax

```python
list_name.copy()
```

`fruits.copy()` creates a separate copy of the original list.

![alt text](<Screenshot (562)(1).png>)


---

## Conclusion

In this practical, we studied Python Lists and performed various operations using list functions and methods such as `append()`, `insert()`, `extend()`, `remove()`, `pop()`, `del`, `clear()`, `len()`, `sort()`, `reverse()`, `count()`, `index()`, and `copy()`.

These operations are useful for creating, accessing, modifying, organizing, and managing collections of data in Python.