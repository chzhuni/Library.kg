from django.urls import path
from . import views
from .views import about_me, my_favourite_writers, sayings_of_great_poets

urlpatterns = [
    path("", views.about_me),
    path("writers/", views.my_favourite_writers),
    path("sayings/", views.sayings_of_great_poets),
]

