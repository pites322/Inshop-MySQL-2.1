from django.test import TestCase
from app1.models import User
# Create your tests here.


class testUserModel(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        User.objects.create(region='Kharkivska', city='Kharkiv', address="Bla-Bla_Bal 354d45556a 447",
                            delivery="asdd44a", password="asdff5844", login="Stenniss", emali="kokojambo@mail.ru")
        print(User)

    def region_max_length(self):
        user = User.objects.get(id=1)
        max_length = user._meta.get_field('region').max_length
        self.assertEquals(max_length, 60)

    def city_max_length(self):
        user = User.objects.get(id=1)
        max_length = user._meta.get_field('city').max_length
        self.assertEquals(max_length, 60)

    def address_max_length(self):
        user = User.objects.get(id=1)
        max_length = user._meta.get_field('address').max_length
        self.assertEquals(max_length, 60)

    def delivery_max_length(self):
        user = User.objects.get(id=1)
        max_length = user._meta.get_field('delivery').max_length
        self.assertEquals(max_length, 60)


# class ShoppingListModelTest(TestCase):
#
#     @classmethod
#     def setUpTestData(cls):
#         ShoppingList.objects.create(buyer=1, product=1)
#
#     def price_max_digits(self):
#         shopinglist = ShoppingList.objects.get(id=1)
#         max_length = shopinglist._meta.get_field('region').max_length
#         self.assertEquals(max_length, 60)
#
#     def city_max_length(self):
#         author = Author.objects.get(id=1)
#         max_length = author._meta.get_field('city').max_length
#         self.assertEquals(max_length, 60)
#
#     def address_max_length(self):
#         author = Author.objects.get(id=1)
#         max_length = author._meta.get_field('address').max_length
#         self.assertEquals(max_length, 60)
#
#     def delivery_max_length(self):
#         author = Author.objects.get(id=1)
#         max_length = author._meta.get_field('delivery').max_length
#         self.assertEquals(max_length, 60)