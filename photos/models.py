from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()


class Location(models.Model):
    name = models.CharField(max_length=60)

    @classmethod
    def get_locations(cls):
        locations = Location.objects.all()
        return locations

    def __str__(self):
        return self.name

    @classmethod
    def update_location(cls, id, value):
        cls.objects.filter(id=id).update(image=value)

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()


class Photo(models.Model):
    photo = models.ImageField(upload_to='photos/')
    name = models.CharField(max_length=60)
    description = models.TextField()
    author = models.CharField(max_length=40, default='admin')
    date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category)
    location = models.ForeignKey(Location)

    @classmethod
    def filter_by_location(cls, location):
        photo_location = Photo.objects.filter(location__name=location).all()
        return photo_location

    @classmethod
    def update_photo(cls, id, value):
        cls.objects.filter(id=id).update(image=value)

    @classmethod
    def get_photo_by_id(cls, id):
        image = cls.objects.filter(id=id).all()
        return image

    @classmethod
    def search_by_category(cls, category):
        photos = cls.objects.filter(category__name__icontains=category)
        return photos

    def __str__(self):
        return self.name

    def save_photo(self):
        self.save()

    def delete_photo(self):
        self.delete()

    class Meta:
        ordering = ['date']