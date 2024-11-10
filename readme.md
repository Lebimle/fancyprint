# Fancyprint

Fancyprint is a Python package for printing text with fancy effects.


## Overview
This project provides a set of utilities for printing text with a cool typing effect and reading user input with a similar effect. It includes customizable delay controllers based on beta distributionw with support for new user-defined controllers.


## Features
- **Fancy Print:** Print text with a typing effect.
- **Fancy Input:** Display a prompt with a typing effect and read user input.
- **Delay Controllers:** Customize delays using beta distribution and create custom controllers.


## Installation
You can install the package using pip:

```bash
pip install path/to/Fancyprint
``` 

Replace ```path/to/Fancyprint``` with the actual path to ```fancyprint_package_vx.x.x```

## Usage

### Importing the package
```python
from fancyprint import fancy_print, fancy_input, set_default_controller
```

### Minimal example
Here's a minimal example of how to use Fancyprint:

```python
from fancyprint import fancy_print

fancy_print("Hello, fancy World!")
```
### Specifying print time
You can specify the minimum and maximum delay in milliseconds by creating a delay controller. Parse minimum- and maximum delay as the first two arguments:
```python
from fancyprint import fancy_print, BetaDelayController

my_delay_controller = BetaDelayController(1000,2000)
fancy_print('This text will be rendered much slower', delay_controller = my_delay_controller)
```
### Setting a default controller
You can set a default delay controller to be used by fancy_print and fancy_input if no other controller is specified:
```python
from fancyprint import set_default_controller, BetaDelayController

my_controller = BetaDelayController(10, 500)
set_default_controller(my_controller)
```
### Using fancy input
```python
from fancyprint import fancy_input

user_input = fancy_input("Enter your name: ")
```
```fancy_input``` supports using custom controllers and respects the default controller if no specific controller is provided. This means you can customize the typing effect for the input prompt just like you do with fancy_print.

#### Example with custom controller
```python
from fancyprint import fancy_input, BetaDelayController

# Create a custom delay controller
custom_controller = BetaDelayController(50, 200, 2, 2)

# Use fancy_input with the custom controller
user_input = fancy_input("Enter your name: ", delay_controller=custom_controller)
print(f"Hello, {user_input}!")
```

#### Example with default controller
```python
from fancyprint import set_default_controller, BetaDelayController, fancy_input

# Set a default delay controller
my_controller = BetaDelayController(499, 500)
set_default_controller(my_controller)

# Use fancy_input without specifying a controller
user_input = fancy_input("Enter your name: ")
print(f"Hello, {user_input}!")
```

### Further customizing the delay

You can further customize the delay by modifying the alpha and beta parameters of the Beta distribution used in the `BetaDelayController`. This allows you to control the shape of the distribution and, consequently, the typing effect.

```python
from fancyprint import fancy_print, BetaDelayController

# Create a BetaDelayController with custom alpha and beta values
custom_controller = BetaDelayController(min_delay=10, max_delay=500, alpha=2.0, beta=5.0)

# Use the custom controller with fancy_print
fancy_print("This text has a custom delay distribution.", controller=custom_controller)
```

In this example, `alpha` and `beta` parameters are set to 2.0 and 5.0, respectively. Adjust these values to achieve the desired typing effect.

### Creating a custom delay controller class

You can also create your own custom delay controller class by implementing the `DelayControllerBase` interface. This allows you to define your own logic for controlling the delay.

```python
from fancyprint import fancy_print, DelayControllerBase

class CustomDelayController(DelayControllerBase):
    def __init__(self, min_delay, max_delay):
        self.min_delay = min_delay
        self.max_delay = max_delay

    def get_delay(self):
        # Implement your custom delay logic here
        return (self.min_delay + self.max_delay) / 2

# Use the custom delay controller with fancy_print
custom_controller = CustomDelayController(min_delay=10, max_delay=500)
fancy_print("This text uses a custom delay controller.", controller=custom_controller)
```

In this example, `CustomDelayController` implements the `DelayControllerBase` interface and defines custom logic for the delay.

## License
This project is licensed under the terms of the MIT license.Please see [LICENSE](LICENSE) for details.