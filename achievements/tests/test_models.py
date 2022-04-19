from django.test import TestCase
from achievements.models import Achievement, Category, Tag


class TestAchievement(TestCase):
    @classmethod
    def setUpTestData(cls):
        Achievement.objects.create(title='Test', description='Case')

    def test_title_label(self):
        achievement = Achievement.objects.last()
        field_label = achievement._meta.get_field('title').verbose_name
        self.assertEquals(field_label, 'title')

    def test_description_label(self):
        achievement = Achievement.objects.last()
        field_label = achievement._meta.get_field('description').verbose_name
        self.assertEquals(field_label, 'description')

    def test_title_max_length(self):
        achievement = Achievement.objects.last()
        max_length = achievement._meta.get_field('title').max_length
        self.assertEquals(max_length, 256)

    def test_description_max_length(self):
        achievement = Achievement.objects.last()
        max_length = achievement._meta.get_field('description').max_length
        self.assertEquals(max_length, 4096)

    def test_object_name_is_last_name_comma_first_name(self):
        achievement = Achievement.objects.last()
        expected_object_name = achievement.title
        self.assertEquals(expected_object_name, str(achievement))


class TestCategory(TestCase):
    @classmethod
    def setUpTestData(cls):
        Category.objects.create(title='Test', description='Case')

    def test_title_label(self):
        category = Category.objects.last()
        field_label = category._meta.get_field('title').verbose_name
        self.assertEquals(field_label, 'title')

    def test_description_label(self):
        category = Category.objects.last()
        field_label = category._meta.get_field('description').verbose_name
        self.assertEquals(field_label, 'description')

    def test_title_max_length(self):
        category = Category.objects.last()
        max_length = category._meta.get_field('title').max_length
        self.assertEquals(max_length, 256)

    def test_description_max_length(self):
        category = Category.objects.last()
        max_length = category._meta.get_field('description').max_length
        self.assertEquals(max_length, 4096)

    def test_object_name_is_last_name_comma_first_name(self):
        category = Category.objects.last()
        expected_object_name = category.title
        self.assertEquals(expected_object_name, str(category))


class TestTag(TestCase):
    @classmethod
    def setUpTestData(cls):
        Tag.objects.create(title='Test', description='Case')

    def test_title_label(self):
        tag = Tag.objects.last()
        field_label = tag._meta.get_field('title').verbose_name
        self.assertEquals(field_label, 'title')

    def test_description_label(self):
        tag = Tag.objects.last()
        field_label = tag._meta.get_field('description').verbose_name
        self.assertEquals(field_label, 'description')

    def test_title_max_length(self):
        tag = Tag.objects.last()
        max_length = tag._meta.get_field('title').max_length
        self.assertEquals(max_length, 256)

    def test_description_max_length(self):
        tag = Tag.objects.last()
        max_length = tag._meta.get_field('description').max_length
        self.assertEquals(max_length, 4096)

    def test_object_name_is_last_name_comma_first_name(self):
        tag = Tag.objects.last()
        expected_object_name = tag.title
        self.assertEquals(expected_object_name, str(tag))
