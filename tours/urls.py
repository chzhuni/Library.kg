from django.urls import path
from tours.views import tour_list_view

urlpatterns = [
    path('tours/', tour_list_view, name='tour_list')
]
