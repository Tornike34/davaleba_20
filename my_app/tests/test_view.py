
from django.test import TestCase
from django.urls import reverse
from my_app.models import MyModel


class MyModelUpdateViewTestCase(TestCase):
    def setUp(self):
        self.obj = MyModel.objects.create(name='John', age=30)
        self.updated_name = 'Jane'

    def test_view_returns_status_code_200(self):
        url = reverse('myapp:update_view', kwargs={'pk': self.obj.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_view_updates_object_correctly(self):
        url = reverse('myapp:update_view', kwargs={'pk': self.obj.pk})
        data = {'name': self.updated_name, 'age': 28}
        response = self.client.post(url, data)
        self.obj.refresh_from_db()
        self.assertEqual(self.obj.name, self.updated_name)

    def test_view_returns_correct_template(self):
        url = reverse('myapp:update_view', kwargs={'pk': self.obj.pk})
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'myapp/my_model_form.html')


class MyModelDeleteViewTestCase(TestCase):
    def setUp(self):
        self.obj = MyModel.objects.create(name='John', age=30)

    def test_view_returns_status_code_302(self):
        url = reverse('myapp:delete_view', kwargs={'pk': self.obj.pk})
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)

    def test_view_deletes_object_correctly(self):
        url = reverse('myapp:delete_view', kwargs={'pk': self.obj.pk})
        response = self.client.post(url)
        exists = MyModel.objects.filter(pk=self.obj.pk).exists()
        self.assertFalse(exists)
