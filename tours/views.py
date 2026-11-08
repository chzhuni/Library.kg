from django.shortcuts import render
from tours.models import Tour, Booking


def tour_list_view(request):
    if request.method == 'GET':
        tours = Tour.objects.all().order_by('-id')
        bookings = Booking.objects.all().order_by('visit_date')
        return render(request, 'tours/tour_list.html', {'tours': tours, 'bookings': bookings})