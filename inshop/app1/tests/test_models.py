from django.test import TestCase
from app1.models import User
# Create your tests here.


class TestUserModel(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        User.objects.create(region='Kharkivska', city='Kharkiv', address="Bla-Bla_Bal 354d45556a 447",
                            delivery="asdd44a")
        print(User)

    def test_region_label(self):
        author = User.objects.get(id=1)
        field_label = author._meta.get_field('region').verbose_name
        self.assertEquals(field_label, 'region')

    def test_city_death_label(self):
        author = User.objects.get(id=1)
        field_label = author._meta.get_field('city').verbose_name
        self.assertEquals(field_label, 'city')

    def test_first_name_label(self):
        author = User.objects.get(id=1)
        field_label = author._meta.get_field('address').verbose_name
        self.assertEquals(field_label, 'address')

    def test_date_of_death_label(self):
        author = User.objects.get(id=1)
        field_label = author._meta.get_field('delivery').verbose_name
        self.assertEquals(field_label, 'delivery')

    def test_region_max_length(self):
        user = User.objects.get(id=1)
        max_length = user._meta.get_field('region').max_length
        self.assertEquals(max_length, 60)

    def test_city_max_length(self):
        user = User.objects.get(id=1)
        max_length = user._meta.get_field('city').max_length
        self.assertEquals(max_length, 60)

    def test_address_max_length(self):
        user = User.objects.get(id=1)
        max_length = user._meta.get_field('address').max_length
        self.assertEquals(max_length, 80)

    def test_delivery_max_length(self):
        user = User.objects.get(id=1)
        max_length = user._meta.get_field('delivery').max_length
        self.assertEquals(max_length, 80)


