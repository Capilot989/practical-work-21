from typing import Union
from barcode_info import barcode_data
import json


class Product:
    """
    A class representing a product with its attributes.

    This class stores product information such as name, price, country of origin,
    and barcode. It provides validation for barcode existence and read-only
    access to product attributes.

    Attributes:
        __name (str): The product name.
        __price (float): The product price.
        __country (str): The country of origin.
        __barcode (int): The product barcode.
    """
    def __init__(self, barcode: int) -> None:
        """
        Initialize a Product instance using its barcode.

        Args:
            barcode (int): The product's barcode number.

        Raises:
            ValueError: If the barcode is not found in the barcode_data.
        """
        product_data = Product.get_info_from_barcode(barcode)
        self.__name = product_data['name']
        self.__price = product_data['price']
        self.__country = product_data['country']
        self.__barcode = barcode

    @property
    def name(self) -> str:
        """
        Get the product name.

        Returns:
            str: The product name.
        """
        return self.__name

    @property
    def price(self) -> float:
        """
        Get the product price.

        Returns:
            float: The product price.
        """
        return self.__price

    @property
    def country(self) -> str:
        """
        Get the country of origin.

        Returns:
            str: The country where the product was made.
        """
        return self.__country

    @property
    def barcode(self) -> int:
        """
        Get the product barcode.

        Returns:
            int: The product barcode number.
        """
        return self.__barcode

    @staticmethod
    def get_info_from_barcode(barcode: str) -> dict[str: Union[str, float]]:
        """
        Retrieve product information from a barcode.

        Args:
            barcode (str): The barcode to look up.

        Returns:
            dict[str, Union[str, float]]: A dictionary containing product information
                                         with keys 'name', 'price', and 'country'.

        Raises:
            ValueError: If the barcode is not found in the barcode_data.
        """
        if barcode not in barcode_data:
            raise ValueError("Товар с таким штрих-кодом не найден")
        return barcode_data[barcode]

    def __repr__(self) -> str:
        """
        Return a string representation of the product.

        Returns:
            str: A formatted string with product name, price, and country.
        """
        return f'{self.name} | {self.price} | {self.country}'


class ShoppingBasket:
    """
    A class representing a shopping basket for managing products.

    This class handles adding and removing products, recalculating total price,
    saving/loading basket state to a JSON file, and displaying basket contents.

    Attributes:
        _basket (list[Product]): List of products in the basket.
        _total_price (float): Total price of all products in the basket.
        _filename (str): Name of the JSON file for persistent storage.
    """
    def __init__(self, filename: str) -> None:
        """
        Initialize a ShoppingBasket instance.

        Args:
            filename (str): Name of the JSON file for saving/loading basket data.
        """
        self._basket = []
        self._total_price = 0
        self._filename = filename

    @property
    def basket(self) -> list['Product']:
        """
        Get the list of products in the basket.

        Returns:
            list[Product]: A copy of the internal basket list (note: returns reference).
        """
        return self._basket

    @property
    def total_price(self) -> float:
        """
        Get the total price of all products in the basket.

        Returns:
            float: The total price.
        """
        return self._total_price


    def add_product(self, barcode: str) -> None:
        """
        Add a product to the basket by its barcode.

        Args:
            barcode (str): The barcode of the product to add.
        """
        self._basket.append(Product(barcode))
        self.__recalculate()
        self.__save()

    def delete_product(self, barcode: str) -> None:
        """
        Remove all products with the given barcode from the basket.

        Args:
            barcode (str): The barcode of products to remove.
        """
        self._basket = [p for p in self._basket if p.barcode != barcode]
        self.__recalculate()

    def __recalculate(self) -> None:
        """
        Recalculate the total price of all products in the basket.
        """
        self._total_price = sum(p.price for p in self._basket)

    def __save(self) -> None:
        """
        Save the current basket state to a JSON file.

        Creates a JSON file containing barcode, name, and price for each product.
        """
        data = [
            {
                "barcode": p.barcode,
                "name": p.name,
                "price": p.price,
            }
            for p in self._basket
        ]
        with open(self._filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def load(self) -> None:
        """
        Load basket state from a JSON file.

        If the file doesn't exist, initializes an empty basket.
        """
        try:
            with open(self._filename, "r", encoding="utf-8") as f:
                data = json.load(f)
                self._basket= [
                    Product(item["barcode"])
                    for item in data
                ]
                self._recalculate()
        except FileNotFoundError:
            self._basket = []
            self._total_price = 0.0

    def show(self):
        """
        Display the contents of the basket.

        Shows each product in the basket followed by the total price.
        If the basket is empty, prints a message indicating so.
        """
        if not self._basket:
            print("Корзина пуста")
        else:
            for p in self._basket:
                print(p)
            print(f"Итого: {self._total_price}")
