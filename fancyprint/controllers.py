from abc import ABC, abstractmethod
from random import betavariate

class DelayControllerBase(ABC):
    """
    Abstract base class for delay controllers.
    """
    @abstractmethod
    def get_delay(self) -> float:
        pass


class BetaDelayController(DelayControllerBase):

    """
    A controller for generating delays based on the beta distribution.

    Attributes:
    min_time (float): The minimum time in milliseconds for the delay. Default is 10.
    max_time (float): The maximum time in milliseconds for the delay. Default is 500.
    alpha (float): The alpha parameter of the beta distribution.
    beta (float): The beta parameter of the beta distribution.

    Methods:
    get_delay() -> float: Calculates a delay based on the beta distribution and the given time range.

    """

    def __init__(self,min_time:float = 10, max_time:float = 500,alpha = 12, beta = 1) -> None:

        """
        Initializes the DelayController with the given parameters.

        Parameters:
        min_time (float): The minimum time in milliseconds for the delay. Default is 10.
        max_time (float): The maximum time in milliseconds for the delay. Default is 500.
        alpha (float): The alpha parameter of the beta distribution. Default is 12.
        beta (float): The beta parameter of the beta distribution. Default is 1.

        Raises:
        ValueError: If min_time is greater than max_time.
        """

        if min_time > max_time:
            raise ValueError("'min_time' must be smaller than or equal to 'max_time'")
        
        self.alpha = alpha
        self.beta = beta
        self.min_time = min_time
        self.max_time = max_time

    def get_delay(self) -> float:

        """
        Calculates a random delay based on the beta distribution.

        Returns:
        float: A delay in seconds, calculated based on the beta distribution and the given time range.
        """

        rand = betavariate(self.alpha, self.beta)
        return 1e-3 * (self.min_time * rand + (1 - rand) * self.max_time)