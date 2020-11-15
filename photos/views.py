from django.shortcuts import render
from .models import Location,Photo
from .forms import PhotoForm
from cloudinary.forms import cl_init_js_callbacks

# Create your views here.
def photo_location(request, location):
    photos = Photo.filter_by_location(location)
    print(photos)
    return render(request,'photos/locale.html',{'location_photos':photos})

def index(request):
    form = PhotoForm()
    photos = Photo.objects.all()
    locations = Location.get_locations()
    print(locations)
    return render(request, 'photos/index.html', {'photos':photos[::-1],'locations': locations,'form': form})

def search_results(request):
    if 'photosearch' in request.GET and request.GET["photosearch"]:
        category = request.GET.get("photosearch")
        searched_photos = Photo.search_by_category(category)
        message = f"{category}"
        print(searched_photos)
        return render(request, 'photos/search.html',{"message":message,"photos":searched_photos})
    else:
        message = "You haven't searched for any photo category"
        return render(request, 'photos/search.html', {"message": message})