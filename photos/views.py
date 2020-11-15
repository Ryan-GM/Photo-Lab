from django.shortcuts import render
from .models import Location,Photo
# Create your views here.
def photo_location(request, location):
    photos = Photo.filter_by_location(location)
    print(photos)
    return render(request,'photos/locale.html',{'location_photos':photos})

def index(request):
    photos = Photo.objects.all()
    locations = Location.get_locations()
    print(locations)
    return render(request, 'photos/index.html', {'photos':photos[::-1],'locations': locations})
