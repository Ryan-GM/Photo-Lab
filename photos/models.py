from django.db import models

# Create your models here.

class Photos(models.Mode):
    photo = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=60)
    description = models.TextField()
    author = models.CharField(max_length=40, default='admin')
    date = models.DateTimeField(auto_now_add=True)
    type = models.ForeignKey(Type)
    location = models.ForeignKey(Location)

    @classmethod
    def get_photo_by_id(cls,id):
        photo = cls.objects.filter(id = id).all()
        return photo

    @classmethod 
    def filter_by_location(cls,location):
        photo_location = Photos.objects.filter(location__name = location).all()
        return photo_location

    