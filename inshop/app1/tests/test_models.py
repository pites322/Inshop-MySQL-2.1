from django.test import TestCase
from app1.models import User, ShoppingList, Product
# Create your tests here.


class TestUserModel(TestCase):

    fixtures = [
        'app1/fixtures/users.json'
    ]

    def setUp(self):
        pass

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


class TestShoppingListModel(TestCase):

    fixtures = [
        'app1/fixtures/forbasket.json'
    ]

    def setUp(self):
        pass

    def test_buyer_verbose_name(self):
        data = ShoppingList.objects.get(id=8)
        field_label = data._meta.get_field('buyer').verbose_name
        self.assertEquals(field_label, 'buyer')

    def test_payed_or_not_verbose_name(self):
        data = ShoppingList.objects.get(id=8)
        field_label = data._meta.get_field('payed_or_not').verbose_name
        self.assertEquals(field_label, 'payed or not')

    def test_product_name_max_length(self):
        data = ShoppingList.objects.get(id=8)
        max_length = data._meta.get_field('product_name').max_length
        self.assertEquals(max_length, 80)

    def test_price_max_digits_decimal_places(self):
        data = ShoppingList.objects.get(id=8)
        max_digits = data._meta.get_field('price').max_digits
        decimal_places = data._meta.get_field('price').decimal_places
        self.assertEquals(decimal_places, 2)
        self.assertEquals(max_digits, 6)


class TestProductModel(TestCase):

    fixtures = [
        'app1/fixtures/products.json'
    ]

    def setUp(self):
        pass

    def test_name_max_length(self):
        data = Product.objects.first()
        max_length = data._meta.get_field('name').max_length
        self.assertEquals(max_length, 60)

    def test_manufacturer_max_length(self):
        data = Product.objects.first()
        max_length = data._meta.get_field('manufacturer').max_length
        self.assertEquals(max_length, 10)

    def test_manufacturer_get_choices(self):
        data = Product.objects.first()
        max_choices = len(data._meta.get_field('manufacturer').choices)
        sec_elem = data._meta.get_field('manufacturer').choices[1][1]
        self.assertEquals(max_choices, 7)
        self.assertEquals(sec_elem, 'Samsung')

    def test_bluetooth_or_wire_max_length(self):
        data = Product.objects.first()
        max_length = data._meta.get_field('bluetooth_or_wire').max_length
        self.assertEquals(max_length, 10)

    def test_bluetooth_or_wire_get_choices(self):
        data = Product.objects.first()
        max_choices = len(data._meta.get_field('bluetooth_or_wire').choices)
        sec_elem = data._meta.get_field('bluetooth_or_wire').choices[0][1]
        self.assertEquals(max_choices, 2)
        self.assertEquals(sec_elem, 'Bluetooth')

    def test_connection_range_max_length_default(self):
        data = Product.objects.first()
        max_length = data._meta.get_field('connection_range').max_length
        default = data._meta.get_field('connection_range').default
        self.assertEquals(max_length, 60)
        self.assertEquals(default, '0')

    def test_connection_range_max_blank_null(self):
        data = Product.objects.first()
        self.assertTrue(data._meta.get_field('connection_range').blank)
        self.assertTrue(data._meta.get_field('connection_range').null)

    def test_work_time_max_length_default(self):
        data = Product.objects.first()
        max_length = data._meta.get_field('work_time').max_length
        default = data._meta.get_field('work_time').default
        self.assertEquals(max_length, 60)
        self.assertEquals(default, '0')

    def test_work_time_max_blank_null(self):
        data = Product.objects.first()
        self.assertTrue(data._meta.get_field('work_time').blank)
        self.assertTrue(data._meta.get_field('work_time').null)

    def test_wire_lenght_max_digits_decimal_places(self):
        data = Product.objects.first()
        max_digits = data._meta.get_field('wire_lenght').max_digits
        decimal_places = data._meta.get_field('wire_lenght').decimal_places
        self.assertEquals(decimal_places, 1)
        self.assertEquals(max_digits, 4)

    def test_wire_lenght_default_blank_null(self):
        data = Product.objects.first()
        default = data._meta.get_field('wire_lenght').default
        self.assertEquals(default, '0')
        self.assertTrue(data._meta.get_field('wire_lenght').blank)
        self.assertTrue(data._meta.get_field('wire_lenght').null)

    def test_type_connector_get_choices(self):
        data = Product.objects.first()
        max_choices = len(data._meta.get_field('type_connector').choices)
        sec_elem = data._meta.get_field('type_connector').choices[2][1]
        self.assertEquals(max_choices, 5)
        self.assertEquals(sec_elem, 'Bluetooth 2.0')

    def test_price_max_digits_decimal_places(self):
        data = Product.objects.first()
        max_digits = data._meta.get_field('price').max_digits
        decimal_places = data._meta.get_field('price').decimal_places
        self.assertEquals(decimal_places, 2)
        self.assertEquals(max_digits, 6)



