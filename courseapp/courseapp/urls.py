from django.contrib import admin
from django.urls import path
from django.urls import path, include




urlpatterns = [
    path('', include('pages.urls')),
    path('kurslar/', include('courses.urls')),
    path('admin/', admin.site.urls),
]
