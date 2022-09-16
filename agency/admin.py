from django.contrib import admin
from .models import Hotel, HotelBooking, HotelImage, Room, Review

admin.site.register(Hotel)
admin.site.register(HotelBooking)
admin.site.register(HotelImage)
admin.site.register(Room)
admin.site.register(Review)
