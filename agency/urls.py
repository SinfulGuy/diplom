from django.urls import path
from . import views
from .views import RoomDetailView, CancelBookingView, AddReview


urlpatterns = [
    path('', views.hotel_list, name='hotel_list'),
    path('hotel/<int:pk>/', views.hotel_detail, name='hotel_detail'),
    path('room_list/', views.RoomListView, name='room_list'),
    path('room/<category>', RoomDetailView.as_view(), name='room_detail'),
    path('booking_list/', views.booking_list, name='booking_list'),
    path('booking/cancel/<pk>', CancelBookingView.as_view(), name='room_cancel'),
    path('search_hotels/', views.search_hotels, name='search_hotels'),
    path('user/', views.user_page, name='user_page'),
    path('hotel/<int:pk>/add_review/', AddReview.as_view(), name='add_review')
]
