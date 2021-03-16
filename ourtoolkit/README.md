## Implemented Functions

### How to use the functions

Just import the function from the our-toolkit module:
```from ourtoolkit.MODULE-NAME import FUNCTION-NAME```


## Summary - Modules

- [Random Things](#random_things)
- [Is Value](#is_value)
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

