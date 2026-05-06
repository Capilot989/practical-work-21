from typing import Optional


class AirConditioning:
    """
    A class representing an air conditioning system.

    This class manages the state (on/off) and temperature settings of an AC unit.
    Temperature can be set between 0 and 43 degrees Celsius (inclusive).
    Provides methods to control power, adjust temperature, and reset to default.

    Attributes:
        __status (bool): Current power state of the AC (True = on, False = off).
        __temperature (Optional[int]): Current target temperature in Celsius.
                                       None when AC is off.
    """
    def __init__(self) -> None:
        """
        Initialize an AirConditioning instance with default off state and no temperature.
        """
        self.__status = False
        self.__temperature = None

    @property
    def status(self) -> bool:
        """
        Get the current power status of the air conditioner.

        Returns:
            bool: True if the AC is on, False if it's off.
        """
        return self.__status

    @status.setter
    def status(self, value) -> None:
        """
        Set the power status of the air conditioner.

        Note: This is a passthrough setter that doesn't implement logic.
        Use switch_on() and switch_off() methods instead.

        Args:
            value (bool): The desired power state.
        """
        pass

    def __set_status(self, value) -> None:
        """
        Internal method to set the power status of the air conditioner.

        Args:
            value (bool): The desired power state (True = on, False = off).
        """
        self.__status = value

    @property
    def temperature(self) -> Optional[int]:
        """
        Get the current target temperature.

        Returns:
            Optional[int]: The current temperature in Celsius if AC is on,
                          None if AC is off.
        """
        return self.__temperature

    @temperature.setter
    def temperature(self, value) -> None:
        """
        Set the target temperature.

        Note: This is a passthrough setter that doesn't implement logic.
        Use __set_temperature() internal method instead.

        Args:
            value (Optional[int]): The desired temperature in Celsius.
        """

        pass

    def __set_temperature(self, value) -> None:
        """
        Internal method to set the target temperature with bounds checking.

        Clamps values outside the valid range (0-43) to the nearest bound.
        If AC is off, temperature should be None.

        Args:
            value (Optional[int]): The desired temperature in Celsius or None.
        """
        if value is None:
            self.__temperature = None

        elif 0 <= value <= 43:
            self.__temperature = value

        elif value < 0:
            self.__temperature = 0

        elif value > 43:
            self.__temperature = 43

    def switch_on(self) -> None:
        """
        Turn the air conditioner on.

        Sets the AC state to on and initializes the temperature to 18 degrees
        if it's currently off.
        """
        if not self.__status:
            self.__set_status(True)
            self.__set_temperature(18)

    def switch_off(self) -> None:
        """
        Turn the air conditioner off.

        Sets the AC state to off and clears the temperature setting (sets to None).
        """
        if self.__status:
            self.__set_status(False)
            self.__set_temperature(None)

    def reset(self) -> None:
        """
        Reset the temperature to the default value (18 degrees).

        Does nothing if the AC is off. Only affects the temperature when AC is on.
        """
        if self.__status:
            self.__set_temperature(18)

    def get_temperature(self) -> Optional[int]:
        """
        Get the current target temperature.

        Returns:
            Optional[int]: The current temperature in Celsius if AC is on,
                          None if AC is off.
        """
        return self.__temperature

    def raise_temperature(self) -> None:
        """
        Increase the temperature by 1 degree.

        Does nothing if the AC is off. The temperature will be clamped to
        the maximum allowed value (43 degrees).
        """

        if self.__status:
            self.__set_temperature(self.__temperature + 1)

    def lower_temperature(self) -> None:
        """
        Decrease the temperature by 1 degree.

        Does nothing if the AC is off. The temperature will be clamped to
        the minimum allowed value (0 degrees).
        """
        if self.__status:
            self.__set_temperature(self.__temperature - 1)

    def __str__(self) -> str:
        """
        Return a string representation of the air conditioner state.

        Returns:
            str: A human-readable string describing the AC state and temperature
                 if on, or just the off state message.
        """
        if self.__status:
            return (f'Кондиционер включен. '
                    f'Температурный режим: {self.__temperature} градусов.')
        return 'Кондиционер выключен.'

