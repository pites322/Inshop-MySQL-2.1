from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    region = models.CharField(max_length=60, help_text="Oblast Vashego projivaia", blank=True)
    city = models.CharField(max_length=60, help_text="Gorod Vashego projivaia", blank=True)
    address = models.CharField(max_length=80, help_text="Adress Vashego projivaia", blank=True)
    delivery = models.CharField(max_length=80, help_text="Predpochitaemaya slujba dostavki i nomer otdelenia",
                                blank=True)


class ShoppingList (models.Model):
    buyer = models.ForeignKey('User', on_delete=models.CASCADE)
    product = models.ForeignKey("Product", on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    data_of_buy = models.DateTimeField(auto_now_add=True)
    payed_or_not = models.CharField(max_length=80, default="No")
    product_name = models.CharField(max_length=80)


class Product(models.Model):
    MANUFACT = (
        ("SN", "Sony"),
        ("SM", "Samsung"),
        ("PS", "Panasonic"),
        ("SW", "Swen"),
        ("AP", "Apple"),
        ("SE", "Sony Ericson"),
        ("XM", "Xiaomi"),
    )

    COLOR = (
        ("BL", "Black"),
        ("WT", "White"),
        ("BE", "Blue"),
        ("GR", "Green"),
        ("PN", "Pink"),
    )

    TYPE = (
        ("BL", "Bluetooth"),
        ("WR", "Wire"),
    )

    TYPE_CONNECTOR = (
        ("3.5", "Mini-jack 3.5 mm"),
        ("LG", "Lightning"),
        ("2.0", "Bluetooth 2.0"),
        ("2.1", "Bluetooth 2.1"),
        ("3.0", "Bluetooth 3.0"),
    )

    name = models.CharField(max_length=60)
    manufacturer = models.CharField(max_length=10, choices=MANUFACT)
    color = models.CharField(max_length=10, choices=COLOR)
    bluetooth_or_wire = models.CharField(max_length=10, choices=TYPE)
    connection_range = models.CharField(max_length=60, blank=True, default="0")
    work_time = models.CharField(max_length=60, blank=True, default="0")
    warranty = models.IntegerField()
    wire_lenght = models.DecimalField(max_digits=4, decimal_places=1, blank=True, default="0", )
    type_connector = models.CharField(max_length=10, choices=TYPE_CONNECTOR)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    photo = models.ImageField(blank=True, upload_to="media/", default="None")

    def __str__(self):
        return self.name