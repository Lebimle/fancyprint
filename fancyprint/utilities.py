from time import sleep
from fancyprint.controllers import DelayControllerBase, BetaDelayController

_default_delay_controller = None

def set_default_controller(controller: DelayControllerBase) -> None:
    """
    Sets the default controller to be used by fancy_print and fancy_input if no other controller is specified.

    Parameters:
    controller (DelayControllerBase): The controller to set as the default.
    """
    global _default_delay_controller
    _default_delay_controller = controller

def fancy_print(text: str, *, end: str = '', read_mode: bool = False, delay_controller: DelayControllerBase = None) -> None:

    """
    Prints text with a cool effect by introducing a random delay between characters

    Parameters:
    text (str): The text to print
    end (str): The string appended after the last character. Default is an empty string.
    read_mode (bool): If True, does not print the end string. Default is False.
    delay_controller (DelayControllerBase): An instance of DelayControllerBase to manage the delay behavior. If None, it attempts to use the global default delay controller. If the global default is also None, a default instance of BetaDelayController is created.
    instance is created.
    """

    if delay_controller is None:
        delay_controller = _default_delay_controller if _default_delay_controller is not None else BetaDelayController()


    for char in text:
        print(char, end = '', flush = True)
        sleep(delay_controller.get_delay())

    if not read_mode: print(end)




def fancy_input(text: str, *, end='', delay_controller: DelayControllerBase = None) -> str:

    """
    Displays a prompt with a typing effect and reads user input.

    Parameters:
    text (str): The prompt text to display.
    end (str): The string appended after the last character of the prompt. This is a keyword-only argument. Default is an empty string.
    delay_controller (DelayControllerBase): An instance of DelayControllerBase to manage the delay behavior. If None, it attempts to use the global default delay controller. If the global default is also None, a default instance of BetaDelayController is created.
    instance is created.

    Returns:
    str: The user input as a string.
    """

    fancy_print(text, end='', read_mode = True,delay_controller=delay_controller)
    user_input = input()
    return user_input