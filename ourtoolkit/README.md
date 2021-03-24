## Implemented Functions

### How to use the functions

Just import the function from the our-toolkit module:
```from ourtoolkit.MODULE-NAME import FUNCTION-NAME```


## Summary - Modules

- [Random Things](#random_things)
- [Is Value](#is_value)
- [Bogosort](#bogosort)
- [Measure Time](#measure_time)
---
## random_things

This module is focused in functions that play with the cold hands of destiny and fate (a.k.a. any random thing)

Return two options with 50% of chance each.

### Implemented functions:
- [flip_coin](#flip_coin)
#
### flip_coin

Simulate the flip of a coin, returning True/False or option_a/option_b 

#### Parameters

<b>return_string</b>

By default the function returns True or False, if you set ```return_string=True``` the function will return ```option_a``` or ```option_b```. If you change the default value from ```option_a``` or ```option_b```, the ```return_string``` value will be set to True automatically

<b>option_a</b>

Set the string value for option_a, by default it uses "heads".

<b>option_b</b>

Set the string value for option_a, by default it uses "tails".

#### Example

 ```python
from ourtoolkit.random_things import flip_coin

#Just return True or False with 50% chance each
if flip_coin(): 
    print("You win :)")
else:
    print("You lose =(")

#Return heads or tails
print(flip_coin(return_string=True))

#Return custom options
print(flip_coin(option_a="Win", option_b="Lose"))
```
---

## is_value

### Implemented functions:
- [is_zero](#is_zero)
#
### is_zero

Check if something is zero

#### Parameters

<b>number</b>

Number that will be compared with zero

#### Example

 ```python
from ourtoolkit.is_value import is_zero

if is_zero(0): 
    print("It works!")
else:
    print("Something is strange here...")
```

## bogosort

The infamous worst sort - that works, eventually. It shuffles a list randomly
until it is sorted.

### Parameters

* `list_` - a list to be sorted
* `key` - optional, a callable that returns an item's sorting key

### Usage

#### Simple Sorting

```python
from ourtoolkit.bogosort import sort
a = [0, 1, 10, 2]
sort(a)

# eventually this will give you [0, 1, 2, 10]
```

#### Keyed Sorting

Thanks to Python's `sorted`'s `key` property [[docs](https://docs.python.org/3/library/functions.html#sorted)]
we can actually customize our sorting strategy. For example:

##### Sorting by Last Word

```python
l = ['mouse', 'cat', 'dog']
sort(l, key=lambda x: x[-1])
# eventually this will give you ['mouse', 'dog', 'cat']
```

##### Sorting by Word Length

```python
l = ['mouse', 'cat', 'dog']
sort(l, key=lambda x: len(x))
# eventually this will give you either ['dog', 'cat', 'mouse'] or ['cat', 'dog', 'mouse']
```

## measure_time

Measure the time of your functions! The duration is calculated using ms

### Parameters

* `function` - your function reference (just call the function without the "( )")
* `verbose` - optional, if True prints a message with the duration and the name of the function (default: True)
* `*args and **kwargs` - optional, if your function needs to use parameters, you can pass them after the function

### Usage


```python
n = int(input("Choose a big number: "))
import random
randomlist = []
for i in range(0,n):
    randomlist.append(random.randint(1,n))

measure_time(randomlist.sort
```

#### Measuring functions with parameters

```python
measure_time(print, "Hello World", end='')
```