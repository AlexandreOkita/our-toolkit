# Our ToolKit - Python3 Library
Open source python library focused on learning about how to contribute to open source process and sharing some "useless" and funny functions

![our-toolkit](https://i.kym-cdn.com/entries/icons/original/000/034/467/Communist_Bugs_Bunny_Banner.jpg)

## Implemented Funcionts

### Flip a Coin

Return two options with 50% of chance each.

#### How to use it

Just import the function from the our-toolkit module:
```from our-toolkit import flip-coin```

#### Parameters

<b>return_string</b>

By default the function returns True or False, if you set ```return_string=True``` the function will return ```option_a``` or ```option_b```. If you change the default value from ```option_a``` or ```option_b```, the ```return_string``` value will be set to True automatically

<b>option_a</b>

Set the string value for option_a, by default it uses "heads".

<b>option_b</b>

Set the string value for option_a, by default it uses "tails".

#### Example

 ```python
from ourtoolkit import flip_coin

#Just return True or False with 50% chance each
if flip_coin(): 
    print("You win :)")
else:
    print("You lose D=")

#Return heads or tails
print(flip_coin(return_string=True))

#Return custom options
print(flip_coin(option_a="Win", option_b="Lose"))
```