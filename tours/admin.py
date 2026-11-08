from django.contrib import admin
from tours.models import Person, Booking, CategoryTour, CommetTour, Tour

admin.site.register(Person)
admin.site.register(Booking)
admin.site.register(CategoryTour)
admin.site.register(CommetTour)
admin.site.register(Tour)