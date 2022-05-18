from django.test import TestCase
from blog import models


class PostTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        models.Post.objects.create(title='Test', description='Case')

    def test_title_label(self):
        post = models.Post.objects.last()
        field_label = post._meta.get_field['title'].verbose_name
        self.assertEquals(field_label, 'title')

    def test_description_label(self):
        achievement = models.Post.objects.last()
        field_label = achievement._meta.get_field('description').verbose_name
        self.assertEquals(field_label, 'description')

    def test_title_max_length(self):
        achievement = models.Post.objects.last()
        max_length = achievement._meta.get_field('title').max_length
        self.assertEquals(max_length, 256)

    def test_description_max_length(self):
        achievement = models.Post.objects.last()
        max_length = achievement._meta.get_field('description').max_length
        self.assertEquals(max_length, 4096)

    def test_object_name_is_last_name_comma_first_name(self):
        achievement = models.Post.objects.last()
        expected_object_name = achievement.title
        self.assertEquals(expected_object_name, str(achievement))


class TestComment(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        models.Comment.objects.create(text='text')

    def test_text_label(self):
        achievement = models.Comment.objects.last()
        field_label = achievement._meta.get_field('text').verbose_name
        self.assertEquals(field_label, 'text')

    def test_description_max_length(self):
        achievement = models.Comment.objects.last()
        max_length = achievement._meta.get_field('text').max_length
        self.assertEquals(max_length, 4096)

    def test_object_name_is_last_name_comma_first_name(self):
        achievement = models.Comment.objects.last()
        expected_object_name = achievement.text
        self.assertEquals(expected_object_name, str(achievement))
