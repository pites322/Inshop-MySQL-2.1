from django.test import SimpleTestCase
from app1.forms import ChangeUserInformation, AddBuy


class TestForms(SimpleTestCase):

    def test_change_user_data_form_valid(self):
        test_from = ChangeUserInformation(data={
            'first_name': 'asddddda',
            'last_name': 'jjfhhdhdha',
            'region': 'dkkaklsld',
            'city': 'asdddaa',
            'address': 'jkjajsdhjha',
            'delivery': 'kkaskdkdaksa'
        })
        self.assertTrue(test_from.is_valid())

    def test_change_user_data_form_valid_without_data(self):
        test_from = ChangeUserInformation(data={})
        self.assertTrue(test_from.is_valid())