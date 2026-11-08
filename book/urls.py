from django.urls import path
from . import views
from .views import about_me, my_favourite_writers, sayings_of_great_poets, book_list_view, book_detail_view

urlpatterns = [
    path("", views.about_me),
    path("writers/", views.my_favourite_writers),
    path("sayings/", views.sayings_of_great_poets),
    path('books/', views.book_list_view, name='book_list'),
    path('books/<int:id>/', views.book_detail_view, name='book_detail'),
]

