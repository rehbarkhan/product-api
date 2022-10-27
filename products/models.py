from unicodedata import category
from django.db import models

#Product Model

class Product(models.Model):
    order_date = models.DateField()
    region = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    product = models.CharField(max_length=255)
    quantity = models.IntegerField()
    unit_price = models.DecimalField(decimal_places = 2,max_digits = 10)

    def __str__(self):
        return self.product




""""OrderDate": "01/10/2020",
            "Region": "East",
            "City": "New York",
            "Category": "Cookies",
            "Product": "Chocolate Chip",
            "Quantity": "82",
            "UnitPrice": "1.87",
"""