from django.test import TestCase
from app1.models import User, ShoppingList, Product
# Create your tests here.


class TestUserModel(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        User.objects.create(region='Kharkivska', city='Kharkiv', address="Bla-Bla_Bal 354d45556a 447",
                            delivery="asdd44a")

    def test_region_label(self):
        data = User.objects.get(id=1)
        field_label = data._meta.get_field('region').verbose_name
        self.assertEquals(field_label, 'region')

    def test_city_death_label(self):
        data = User.objects.get(id=1)
        field_label = data._meta.get_field('city').verbose_name
        self.assertEquals(field_label, 'city')

    def test_first_name_label(self):
        data = User.objects.get(id=1)
        field_label = data._meta.get_field('address').verbose_name
        self.assertEquals(field_label, 'address')

    def test_date_of_death_label(self):
        data = User.objects.get(id=1)
        field_label = data._meta.get_field('delivery').verbose_name
        self.assertEquals(field_label, 'delivery')

    def test_region_max_length(self):
        data = User.objects.get(id=1)
        max_length = data._meta.get_field('region').max_length
        self.assertEquals(max_length, 60)

    def test_city_max_length(self):
        data = User.objects.get(id=1)
        max_length = data._meta.get_field('city').max_length
        self.assertEquals(max_length, 60)

    def test_address_max_length(self):
        data = User.objects.get(id=1)
        max_length = data._meta.get_field('address').max_length
        self.assertEquals(max_length, 80)

    def test_delivery_max_length(self):
        data = User.objects.get(id=1)
        max_length = data._meta.get_field('delivery').max_length
        self.assertEquals(max_length, 80)


# class TestShoppingListModel(TestCase):
#
#     def setUp(self):
#         User.objects.create_user(username='pshdjsakdas', password="asdsadsad", email="sdswwwqad@gmail.com")
#         Product.objects.create(name='asdsddaa', manufacturer="ksakasskd", price=154.56, warranty=54)
#         user = User.objects.first()
#         prod = Product.objects.first()
#         self.product_buy = ShoppingList.objects.create(buyer=user, product=prod, price=154.56, payed_or_not="sadads",
#                                                        product_name="sadda")
#
#     def test_price_correct(self):
#         field_label = self.product_buy._meta.get_field('price').verbose_name
#         self.assertEquals(field_label, 'price')
#
#     # def test_price_incorrect(self):
#     #     data = ShoppingList.objects.first()
#     #     field_label = data._meta.get_field('buyer').verbose_name
#     #     self.assertEquals(field_label, 'buyer')
#
#     # def test_region_max_length(self):
#     #     data = User.objects.get(id=1)
#     #     max_length = data._meta.get_field('region').max_length
#     #     self.assertEquals(max_length, 60)
#     #
#     # def test_city_max_length(self):
#     #     data = User.objects.get(id=1)
#     #     max_length = data._meta.get_field('city').max_length
#     #     self.assertEquals(max_length, 60)
#     #
#     # def test_payed_or_not_max_length(self):
#     #     data = ShoppingList.objects.get(id=1)
#     #     max_length = data._meta.get_field('payed_or_not').max_length
#     #     self.assertEquals(max_length, 80)
#     #
#     # def test_product_name_max_length(self):
#     #     data = ShoppingList.objects.get(id=1)
#     #     max_length = data._meta.get_field('product_name').max_length
#     #     self.assertEquals(max_length, 80)
#
#     def tearDown(self):
#         User.objects.all().delete()
#         Product.objects.all().delete()
#         ShoppingList.objects.all().delete()

