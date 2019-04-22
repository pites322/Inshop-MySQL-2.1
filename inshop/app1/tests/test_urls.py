from django.test import TestCase
from django.urls import reverse, resolve
from app1.views import HomePage, product_details, Profile, user_change_info, basket, Search, buy_one_product


class TestUrlApp1(TestCase):
    def test_HomePage_resolved(self):
        url = reverse("bits in bytes")
        self.assertEquals(resolve(url).func.view_class, HomePage)

    def test_product_details_resolved(self):
        url = reverse("product_details", args=['1'])
        self.assertEquals(resolve(url).func, product_details)

    def test_Profile_resolved(self):
        url = reverse("profile")
        self.assertEquals(resolve(url).func.view_class, Profile)

    def test_change_data_resolved(self):
        url = reverse("profile_correct")
        self.assertEquals(resolve(url).func, user_change_info)

    def test_basket_resolved(self):
        url = reverse("basket")
        self.assertEquals(resolve(url).func, basket)

    def test_Search_resolved(self):
        url = reverse("searching")
        self.assertEquals(resolve(url).func.view_class, Search)

    def test_buy_one_product_resolved(self):
        url = reverse("product_buy_one", args=['1'])
        self.assertEquals(resolve(url).func, buy_one_product)

