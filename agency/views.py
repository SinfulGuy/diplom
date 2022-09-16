from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Hotel, HotelBooking, Room, Review
from .forms import HotelForm, BookingForm, AvailabilityForm, UserForm, ReviewForm
from django.views.generic import ListView, FormView, View, DeleteView, CreateView
from agency.booking.availability import check_availability
from django.urls import reverse, reverse_lazy
from django.core.paginator import Paginator
from .filters import HotelFilter


def user_page(request):
    user_form = UserForm(instance=request.user)
    return render(request=request, template_name='agency/profile_page.html',
                  context={'user': request.user, 'user_form': user_form})


def search_hotels(request):
    if request.method == "POST":
        search = request.POST['search']
        hotels = Hotel.objects.filter(name__contains=search)
        return render(request, 'agency/search_form.html', {'search': search, 'hotels': hotels})
    else:
        return render(request, 'agency/search_form.html', {})


def hotel_list(request):
    hotels = Hotel.objects.all()
    hotel_filter = HotelFilter(request.GET, queryset=hotels)
    pag = Paginator(Hotel.objects.all(), 2)
    page = request.GET.get('page')
    hotel = pag.get_page(page)
    return render(request, 'agency/hotel_list.html', {
        'hotels': hotels,
        'hotel': hotel,
        'hotel_filter': hotel_filter
    })


def hotel_detail(request, pk):
    hotel = get_object_or_404(Hotel, pk=pk)
    return render(request, 'agency/hotel_detail.html', {'hotel': hotel})


def booking_list(request):
    if request.user.is_staff:
        bookings = HotelBooking.objects.all()
        return render(request, 'agency/booking_list.html', {'bookings': bookings})
    else:
        bookings = HotelBooking.objects.filter(user=request.user)
        return render(request, 'agency/booking_list.html', {'bookings': bookings})


def RoomListView(request):
    room = Room.objects.all()[0]
    rooms = Room.objects.all()
    room_categories = dict(room.Room_Categories)
    room_values = room_categories.values()
    room_list = []
    for room_category in room_categories:
        room = room_categories.get(room_category)
        room_url = reverse('room_detail', kwargs={'category': room_category})
        room_list.append((room, room_url))
    context = {
        'room_list': room_list,
        'rooms': rooms
    }
    return render(request, 'agency/room_list.html', context)


class RoomDetailView(View):
    def get(self, request, *args, **kwargs):
        category = self.kwargs.get('category', None)
        form = AvailabilityForm()
        room_list = Room.objects.filter(category=category)
        if len(room_list):
            room = room_list[0]
            room_category = dict(room.Room_Categories).get(room.category, None)
            context = {
                'room_category': room_category,
                'form': form,
            }
            return render(request, 'agency/room_detail.html', context)
        else:
            return HttpResponse('Category does not exist')

    def post(self, request, *args, **kwargs):
        category = self.kwargs.get('category', None)
        room_list = Room.objects.filter(category=category)
        form = AvailabilityForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
        available_rooms = []
        for room in room_list:
            if check_availability(room, data['check_in'], data['check_out']):
                available_rooms.append(room)

        if len(available_rooms) > 0:
            room = available_rooms[0]
            booking = HotelBooking.objects.create(
                user=self.request.user,
                room=room,
                check_in=data['check_in'],
                check_out=data['check_out'],
            )
            booking.save()
            return HttpResponse(booking)
        else:
            return HttpResponse('All of this category of rooms are booked!')


class CancelBookingView(DeleteView):
    model = HotelBooking
    template_name = 'agency/booking_cancel.html'
    success_url = reverse_lazy('booking_list')


class AddReview(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'agency/review_form.html'

    def form_valid(self, form):
        form.instance.hotel_id = self.kwargs['pk']
        return super().form_valid(form)

    success_url = reverse_lazy('hotel_list')
