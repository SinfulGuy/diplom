from django import forms
from .models import Hotel, HotelBooking, Review
from django.contrib.auth.models import User


class HotelForm(forms.ModelForm):
    class Meta:
        model = Hotel
        fields = ('name', 'description', 'stars', 'location')


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')


class BookingForm(forms.ModelForm):
    class Meta:
        model = HotelBooking
        fields = ('check_in', 'check_out')


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('name', 'body')


class AvailabilityForm(forms.Form):
    check_in = forms.DateField(required=True, input_formats=["%Y-%m-%d", ])
    check_out = forms.DateField(required=True, input_formats=["%Y-%m-%d", ])


