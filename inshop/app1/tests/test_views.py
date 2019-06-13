from django.test import TestCase, Client
from django.urls import reverse
import json


class TestViews(TestCase):

    fixtures = [
        'app1/fixtures/forbasket.json'
    ]

    def setUp(self):
        self.client = Client()

    def test_HomePage_GET(self):
        response = self.client.get(reverse('bits in bytes'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "app1/Main.html")

    def test_Search_GET(self):
        response = self.client.get(reverse('searching'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "app1/search.html")

    def test_Profile_GET(self):
        self.client.login(username='pitess1', password="Pit80953293293")
        response = self.client.get(reverse('profile'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "app1/profile.html")

    def test_ProductDetails_GET(self):
        response = self.client.get(reverse('product_details',kwargs={'pk': 1}))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "app1/prod_detail.html")

    def test_ProductDetails_GET_404(self):
        response = self.client.get(reverse('product_details', kwargs={'pk': 10}))
        self.assertEquals(response.status_code, 404)

    def test_UserChangeInfo_GET(self):
        self.client.login(username='pitess1', password="Pit80953293293")
        response = self.client.get(reverse('profile_correct'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "app1/profile_correct.html")

    def test_Basket_GET(self):
        response = self.client.get(reverse('basket'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "app1/basket.html")

    def test_BuyOneProduct_GET(self):
        response = self.client.get(reverse('product_buy_one', kwargs={'pk': 8}))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "app1/buy_one.html")

    def test_BuyOneProduct_GET_404(self):
        response = self.client.get(reverse('product_buy_one', kwargs={'pk': 115}))
        self.assertEquals(response.status_code, 404)

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
