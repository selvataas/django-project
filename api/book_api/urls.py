from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path('', views.books),
    path('<int:id>', views.book),
]

