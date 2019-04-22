from django.test import TestCase, Client
from django.urls import reverse
from app1.models import ShoppingList, Product, Image, Color, User
import json


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()

    @classmethod
    def setUpTestData(cls):
        User.objects.create_user(username='pshdjsakdas', password="asdsadsad", email="sdswwwqad@gmail.com")
        Product.objects.create(name='asdsddaa', manufacturer="ksakasskd", price=154.56, warranty=54)
        user = User.objects.first()
        prod = Product.objects.first()
        ShoppingList.objects.create(buyer=user, product=prod, price=154.56)

    def test_HomePage_GET(self):
        responde = self.client.get(reverse('bits in bytes'))
        self.assertEquals(responde.status_code, 200)
        self.assertTemplateUsed(responde, "app1/Main.html")

    def test_Search_GET(self):
        responde = self.client.get(reverse('searching'))
        self.assertEquals(responde.status_code, 200)
        self.assertTemplateUsed(responde, "app1/search.html")

    def test_Profile_GET(self):
        self.client.login(username='pshdjsakdas', password="asdsadsad")
        responde = self.client.get(reverse('profile'))
        self.assertEquals(responde.status_code, 200)
        self.assertTemplateUsed(responde, "app1/profile.html")

    def test_product_details_GET(self):
        responde = self.client.get(reverse('product_details', args="1"))
        self.assertEquals(responde.status_code, 200)
        self.assertTemplateUsed(responde, "app1/prod_detail.html")

    def test_product_details_GET_404(self):
        responde = self.client.get(reverse('product_details', args="5"))
        self.assertEquals(responde.status_code, 404)

    def test_user_change_info_GET(self):
        self.client.login(username='pshdjsakdas', password="asdsadsad")
        responde = self.client.get(reverse('profile_correct'))
        self.assertEquals(responde.status_code, 200)
        self.assertTemplateUsed(responde, "app1/profile_correct.html")

    def test_basket_GET(self):
        responde = self.client.get(reverse('basket'))
        self.assertEquals(responde.status_code, 200)
        self.assertTemplateUsed(responde, "app1/basket.html")

    def test_buy_one_product_GET(self):
        responde = self.client.get(reverse('product_buy_one', args="1"))
        self.assertEquals(responde.status_code, 200)
        self.assertTemplateUsed(responde, "app1/buy_one.html")

    def test_buy_one_product_GET_404(self):
        responde = self.client.get(reverse('product_buy_one', args="5"))
        self.assertEquals(responde.status_code, 404)

    # def test_profile_correct_POST_correct_data(self):
    #     self.client.login(username='pshdjsakdas', password="asdsadsad")
    #     user = User.objects.first()
    #     profile_correct = self.client.get(reverse('profile_correct'))
    #     print(profile_correct, 12233)
    #     responde = self.client.post('profile_correct', {
    #         'first_name': ['asddasd'],
    #         'last_name': ['Ramsey'],
    #         'region': ["jsjadlaslas"],
    #         'city': ["asddsadas"],
    #         'address': ['sadasddasads'],
    #         'delivery': ['asdasdddddaasaaa']
    #     })
    #     self.assertEquals(responde.status_code, 302)
    #     self.assertEquals(user.city, "asddsadas")

    # def test_profile_correct_POST_correct_data(self):
    #     self.client.login(username='pshdjsakdas', password="asdsadsad")
    #     profile_correct = self.client.get(reverse('product_details', args='1'))
    #     print(profile_correct)
    #     responde = self.client.post(profile_correct)
    #     # prod = ShoppingList.objects.get(id=2)
    #     self.assertEquals(responde.status_code, 302)
    #     self.assertEquals(prod.buyer, "1")

    @classmethod
    def tearDownTestData(cls):
        User.objects.all().delete()
        Product.objects.all().delete()
        ShoppingList.objects.all().delete()