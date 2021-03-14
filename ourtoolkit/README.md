## Implemented Functions

### Flip a Coin

Return two options with 50% of chance each.

#### How to use it

Just import the function from the our-toolkit module:
```from ourtoolkit.flip_coin import flip_coin```

#### Parameters

<b>return_string</b>

By default the function returns True or False, if you set ```return_string=True``` the function will return ```option_a``` or ```option_b```. If you change the default value from ```option_a``` or ```option_b```, the ```return_string``` value will be set to True automatically

<b>option_a</b>

Set the string value for option_a, by default it uses "heads".

<b>option_b</b>

Set the string value for option_a, by default it uses "tails".

#### Example

 ```python
from ourtoolkit.flip_coin import flip_coin

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