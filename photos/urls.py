from django.urls import path
from django.urls.conf import re_path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'photos'

urlpatterns = [
    path(r'^$', views.index, name='index'),
    path(r'^search/', views.search_results, name='search'),
    re_path(r'^location/(?P<location>\w+)/', views.photo_location, name='location'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    