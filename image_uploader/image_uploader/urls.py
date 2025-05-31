
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from django.http import HttpResponse
from django.urls import include


def home(request):
    return HttpResponse("Welcome to the Home Page")

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('image/', include('image_uploader.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

