from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Hotel(models.Model):
    Cities = (
        ('Minsk', 'Minsk'),
        ('Brest', 'Brest'),
        ('Vitebsk', 'Vitebsk'),
        ('Mogilev', 'Mogilev'),
        ('Gomel', 'Gomel'),
        ('Grodno', 'Grodno'),
    )
    name = models.CharField(max_length=255)
    description = models.TextField()
    stars = models.IntegerField()
    location = models.CharField(max_length=10, choices=Cities)
    price = models.IntegerField(default=10)
    room_count = models.IntegerField(default=5)
    images = models.ImageField(upload_to="hotels/")

    def __str__(self):
        return f'{self.name}'


class Review(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='reviews')
    name = models.CharField(max_length=255)
    body = models.TextField()
    date_add = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, related_name="author", on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.hotel} - {self.name}'


class Room(models.Model):
    Room_Categories = (
        ('YAC', 'AC'),
        ('NAC', 'NON-AC'),
        ('DEL', 'DELUXE'),
        ('KIN', 'KING'),
    )
    number = models.IntegerField()
    category = models.CharField(max_length=3, choices=Room_Categories)
    beds = models.IntegerField()
    capacity = models.IntegerField()
    hotel = models.ForeignKey(Hotel, related_name='hotel_name', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.number}. {self.category} with {self.beds} beds for {self.capacity} people'


class HotelImage(models.Model):
    hotel = models.ForeignKey(Hotel, related_name="hotel_images", on_delete=models.CASCADE)
    images = models.ImageField(upload_to="images/")


class HotelBooking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="user_booking", on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()

    def __str__(self):
        return f'{self.user} booking {self.room}'

    def cancel_booking(self):
        return reverse('room_cancel', args=[self.pk, ])
