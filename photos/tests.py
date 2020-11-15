from django.test import TestCase
from .models import Photo,Location,Category
# Create your tests here.

class TestPhoto(TestCase):
    def setUp(self):
        self.location = Location(name='Strath')
        self.location.save_location()
        self.category = Category(name='Bike')
        self.category.save_category()
        self.photo_test = Photo(id = 1,name = 'photo',description = 'to test the photo',location = self.location,category = self.category)

    def test_instance(self):
        self.assertTrue(isinstance(self.photo_test, Photo))

    def test_save_photo(self):
        self.image_test.save_photo()
        after = Photo.objects.all()
        self.assertTrue(len(after) > 0)

    def test_delete_photo(self):
        self.photo_test.delete_image()
        photos = Photo.objects.all()
        self.assertTrue(len(photos) == 0)

    def test_update_photo(self):
        self.photo_test.save_photo()
        self.photo_test.update_photo(self.photo_test.id, 'photos/test.jpg')
        changed_img = Photo.objects.filter(photo='photos/test.jpg')
        self.assertTrue(len(changed_img) > 0)

    def test_get_photo_by_id(self):
        found_photo = self.photo_test.get_photo_by_id(self.photo_test.id)
        photo = Photo.objects.filter(id=self.image_test.id)
        self.assertTrue(found_photo, photo)

    def test_search_photo_by_location(self):
        self.image_test.save_image()
        found_photo = self.photo_test.filter_by_location(location='Strath')
        self.assertTrue(len(found_photo) == 1)

    def test_search_photo_by_category(self):
        category = 'Bike'
        found_photo = self.photo_test.search_by_category(category)
        self.assertTrue(len(found_photo) > 1)

    def tearDown(self):
        Photo.objects.all().delete()
        Location.objects.all().delete()
        Category.objects.all().delete()

class CategoryTestClass(TestCase):
    def setUp(self):
        self.category = Category(name='Bike')
        self.category.save_category()

    def test_instance(self):
        self.assertTrue(isinstance(self.category, Category))

    def test_save_category(self):
        self.category.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)

    def test_delete_category(self):
        self.category.delete_category()
        category = Category.objects.all()
        self.assertTrue(len(category) == 0)

class TestLocation(TestCase):
    def setUp(self):
        self.location = Location(name='Strath')
        self.location.save_location()

    def test_instance(self):
        self.assertTrue(isinstance(self.location, Location))

    def test_save_location(self):
        self.location.save_location()
        locations = Location.get_locations()
        self.assertTrue(len(locations) > 0)

    def test_get_locations(self):
        self.location.save_location()
        locations = Location.get_locations()
        self.assertTrue(len(locations) > 1)

    def test_update_location(self):
        new_location = 'Mushroom'
        self.location.update_location(self.location.id, new_location)
        changed_location = Location.objects.filter(name='Mushroom')
        self.assertTrue(len(changed_location) > 0)

    def test_delete_location(self):
        self.location.delete_location()
        location = Location.objects.all()
        self.assertTrue(len(location) == 0)