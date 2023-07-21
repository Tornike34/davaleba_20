from django.test import TestCase
from my_app.models import MyModel


class MyModelTestCase(TestCase):
    def setUp(self):
        self.obj = MyModel.objects.create(name='John', age=30)

    def test_model_can_be_saved(self):
        initial_count = MyModel.objects.count()
        obj = MyModel(name='Jane', age=25)
        obj.save()
        new_count = MyModel.objects.count()
        self.assertEqual(new_count, initial_count + 1)

    def test_model_can_be_retrieved(self):
        obj_from_db = MyModel.objects.get(name='John')
        self.assertEqual(obj_from_db.age, self.obj.age)

    def test_model_can_be_updated(self):
        updated_name = 'Jane'
        self.obj.name = updated_name
        self.obj.save()
        obj_from_db = MyModel.objects.get(pk=self.obj.pk)
        self.assertEqual(obj_from_db.name, updated_name)

    def test_model_can_be_deleted(self):
        initial_count = MyModel.objects.count()
        self.obj.delete()
        new_count = MyModel.objects.count()
        self.assertEqual(new_count, initial_count - 1)
