
from django.test import TestCase
from my_app.forms import MyModelForm

class MyModelFormTestCase(TestCase):
    def test_form_is_valid_with_correct_data(self):
        form_data = {'name': 'John', 'age': 30}
        form = MyModelForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_form_is_invalid_with_incorrect_data(self):
        form_data = {'name': '', 'age': -5}
        form = MyModelForm(data=form_data)
        self.assertFalse(form.is_valid())
